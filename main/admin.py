from django.contrib import admin
from .models import ConversationTopic, ConversationMessage

# Register your models here.

admin.site.register(ConversationTopic)
admin.site.register(ConversationMessage)
