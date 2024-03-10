from dotenv import load_dotenv
import os
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_community.chat_models import ChatOpenAI

cwd = os.getcwd()
folder_name = 'data/pdfs'
path = os.path.join(cwd, folder_name)
store_u = []
store_a =[]

def get_pdf_txt(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        read_pdf = PdfReader(pdf)
        for page in read_pdf.pages:
            text += page.extract_text()
    return text

def texts_to_chunks(text):
    text_splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=200, length_function=len)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vectorstore(text_chunks):
    try:
        # Try initializing with OpenAIEmbeddings
        embeddings = OpenAIEmbeddings()  # You might need to pass API key or other parameters
        vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
        return vectorstore, "Vector store created successfully using OpenAIEmbeddings."
    except Exception as e_openai:
        try:
            # Try initializing with HuggingFaceInstructEmbeddings
            embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
            vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
            return vectorstore, "Vector store created successfully using HuggingFaceInstructEmbeddings."
        except Exception as e_huggingface:
            return None, f"Error creating vector store: e_openai, {e_huggingface}"


def get_conv_chain(vectorstore):
    try:
        llms = ChatOpenAI()
        memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
        conv_chain = ConversationalRetrievalChain.from_llm(
            llm=llms,
            retriever=vectorstore.as_retriever(),
            memory=memory
        )
        return conv_chain, "Conversation chain created successfully."
    except Exception as e:
        return None, f"Error creating conversation chain: {e}"

def handle_userinput(user_question):
    response = conversation({'question': user_question})
    store_u.append(user_question)
    print(response)

def main():
    load_dotenv()
    pdf_docs = [os.path.join(path, file_name) for file_name in os.listdir(path) if file_name.endswith('.pdf')]

    raw_text = get_pdf_txt(pdf_docs)

    text_chunks = texts_to_chunks(raw_text)

    vectorstore, vectorstore_message = get_vectorstore(text_chunks)
    if vectorstore is None:
        return vectorstore_message

    conversation, conversation_message = get_conv_chain(vectorstore)
    if conversation is None:
        return conversation_message

    user_question = input("What is your question?: ")
    if user_question:
        handle_userinput(user_question)


if __name__ == "__main__":
    result = main()
    print(result)
