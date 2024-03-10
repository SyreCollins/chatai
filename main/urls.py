from django.urls import path
from .views import ChatAIAPIView, ConversationTopicListAPIView, ConversationMessageListAPIView, RegisterAPIView, LoginAPIView

urlpatterns = [
    path('chatai', ChatAIAPIView.as_view(), name='ai-conversation'),
    path('chatai/topics/', ConversationTopicListAPIView.as_view(), name='conversation-topic-list'),
    path('chatai/messages/<int:topic_id>/', ConversationMessageListAPIView.as_view(), name='conversation-message-list'),
    path('login', LoginAPIView.as_view(), name='login'),
    path('register', RegisterAPIView.as_view(), name='register'),
]
