from django.contrib import admin

from mailapp.models import Client, Message, NewsLetter, Attempt


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'comment',)
    list_filter = ('name', 'email',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('letter_subject', 'body',)


@admin.register(NewsLetter)
class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'end_time', 'frequency', 'status',)
    list_filter = ('status',)


@admin.register(Attempt)
class AttemptAdmin(admin.ModelAdmin):
    list_display = ('time', 'status', 'server_response',)
    list_filter = ('status',)