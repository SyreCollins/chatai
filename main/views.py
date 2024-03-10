from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import ConvTopicSerializer, ConvMessageSerializer
from .ai import get_pdf_txt, texts_to_chunks, get_vectorstore, get_conv_chain, handle_userinput
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework import status

class RegisterAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        #email = request.data.get('email')
        password = request.data.get('password')
        password2 = request.data.get('password2')

        if password == password2:
            #if User.objects.filter(email=email).exists():
                #return Response({'message': 'Email Already Exists'}, status=status.HTTP_400_BAD_REQUEST)
            if User.objects.filter(username=username).exists():
                return Response({'message': 'Username Already Exists'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                user = User.objects.create_user(username=username, email=None, password=password)
                user.save()
                return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'The two passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Authentication failed'}, status=status.HTTP_401_UNAUTHORIZED)

class ConversationTopicListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        topics = ConversationTopic.objects.filter(user=request.user)
        serializer = ConversationTopicSerializer(topics, many=True)
        return Response(serializer.data)

class ConversationMessageListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, topic_id):
        messages = ConversationMessage.objects.filter(topic_id=topic_id)
        serializer = ConversationMessageSerializer(messages, many=True)
        return Response(serializer.data)

class ChatAIAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        user_question = request.data.get('question')
        if user_question:
            # Create or retrieve conversation topic
            topic = ConversationTopic.objects.get_or_create(user=request.user, topic="AI Conversation")
            # Save user question
            ConversationMessage.objects.create(topic=topic, user=request.user, message=user_question)
            # Get AI response
            ai_response = handle_userinput(request.user, user_question)
            # Save AI response
            ConversationMessage.objects.create(topic=topic, user=None, message=ai_response)

            return Response({"response": ai_response}, status=200)
        else:
            return Response({"error": "No question provided"}, status=400)
