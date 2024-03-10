Chat AI API Project
This is a Django-based API project for a Chat AI system integrated with Langchain, RAG (Retrieval-Augmented Generation), and OpenAI technologies.

Overview
The Chat AI API project allows users to interact with a conversational AI system through HTTP requests. The system utilizes advanced natural language processing techniques provided by
Langchain, RAG, and OpenAI to generate contextually relevant responses to user queries.

Features
Conversational Interface: Users can engage in conversations with the AI system by sending HTTP requests with their queries.
Integration with Langchain: Langchain technology is utilized for text processing and analysis, enabling the AI to understand and respond appropriately to user inputs.
RAG (Retrieval-Augmented Generation): The system leverages RAG for improved response generation by retrieving relevant information from a large knowledge base.
OpenAI Integration: OpenAI's language models enhance the conversational capabilities of the AI, allowing for more natural and contextually relevant responses.
API Endpoints
1. User Registration
Endpoint: /register
Method: POST
Description: Register a new user account.
Parameters:
username: User's username
password: User's password
password2: password confirmation
Response: JSON object indicating success or failure.
3. User Login
Endpoint: /login
Method: POST
Description: Log in an existing user.
Parameters:
username: User's username
password: User's password
Response: JSON object indicating success or failure.
4. Start Conversation
Endpoint: /chatai
Method: POST
Description: Initiate a conversation with the AI.
Parameters:
question: User's query or message
Response: JSON object containing the AI's response.
5. List Conversation Topics
Endpoint: /chatai/topics/
Method: GET
Description: Retrieve a list of conversation topics for the authenticated user.
Authentication: Required
Response: JSON object containing the list of conversation topics.
6. Retrieve Conversation Messages
Endpoint: /chatai/messages/<int:topic_id>/
Method: GET
Description: Retrieve conversation messages for a specific topic.
Parameters:
topic_id: ID of the conversation topic
Authentication: Required
Response: JSON object containing the conversation messages.
Usage
To use the Chat AI API, follow these steps:

Register a new user account using the /register endpoint.
Log in with your registered credentials using the /login endpoint.
Initiate a conversation with the AI by sending a POST request to the /chatai/ endpoint with your query.
Retrieve conversation topics and messages using the respective endpoints.
Technologies Used
Django: Web framework for building the API
Langchain: Text processing and analysis
RAG (Retrieval-Augmented Generation): Enhanced response generation
OpenAI: Language models for conversational AI
Contributors
PythonProdigy - SyreCollins

License
This project is licensed under the MIT License.
