from django.urls import path
from mailapp.apps import MailappConfig
from mailapp.views import (
    LetterListView,
    LetterDetailView,
    LetterCreateView,
    LetterUpdateView,
    LetterDeleteView,
    MessageListView,
    MessageDetailView,
    MessageCreateView,
    MessageUpdateView,
    MessageDeleteView,
    ClientListView,
    ClientDetailView,
    ClientCreateView,
    ClientUpdateView,
    ClientDeleteView,
)

app_name = MailappConfig.name

urlpatterns = [
    path("", LetterListView.as_view(), name="letter_list"),
    path("mailapp/<int:pk>/", LetterDetailView.as_view(), name="letter_detail"),
    path("mailapp/create", LetterCreateView.as_view(), name="letter_create"),
    path("mailapp/<int:pk>/update/", LetterUpdateView.as_view(), name="letter_update"),
    path("mailapp/<int:pk>/delete/", LetterDeleteView.as_view(), name="letter_delete"),
    path("message_list/", MessageListView.as_view(), name="message_list"),
    path(
        "message_service/<int:pk>/", MessageDetailView.as_view(), name="message_detail"
    ),
    path("message_create/", MessageCreateView.as_view(), name="message_create"),
    path(
        "message_update/<int:pk>/update/",
        MessageUpdateView.as_view(),
        name="message_update",
    ),
    path(
        "message_delete/<int:pk>/delete/",
        MessageDeleteView.as_view(),
        name="message_delete",
    ),
    path("client_list/", ClientListView.as_view(), name="client_list"),
    path("client_service/<int:pk>/", ClientDetailView.as_view(), name="client_detail"),
    path("client_create/", ClientCreateView.as_view(), name="client_create"),
    path(
        "client_update/<int:pk>/update/",
        ClientUpdateView.as_view(),
        name="client_update",
    ),
    path(
        "client_delete/<int:pk>/delete/",
        ClientDeleteView.as_view(),
        name="client_delete",
    ),
]
