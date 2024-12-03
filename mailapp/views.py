from random import sample

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
)

from blog.models import Blog
from mailapp.forms import (
    NewsLetterForm,
    NewsLetterModeratorForm,
    MessageForm,
    ClientForm,
)
from mailapp.models import NewsLetter, Client, Message


class LetterListView(ListView):
    model = NewsLetter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_newsletters"] = NewsLetter.objects.count()
        context["active_newsletters"] = NewsLetter.objects.filter(
            status="CREATED"
        ).count()
        context["unique_clients"] = Client.objects.distinct().count()
        all_posts = list(Blog.objects.filter(is_published=True))
        context["random_posts"] = sample(all_posts, min(len(all_posts), 3))
        return context


class LetterDetailView(DetailView):
    model = NewsLetter


class LetterCreateView(CreateView, LoginRequiredMixin):
    model = NewsLetter
    form_class = NewsLetterForm
    success_url = reverse_lazy("mailapp:letter_list")

    def form_valid(self, form):
        letter = form.save()
        user = self.request.user
        letter.owner = user
        letter.save()
        return super().form_valid(form)


class LetterUpdateView(LoginRequiredMixin, UpdateView):
    model = NewsLetter
    form_class = NewsLetterForm
    success_url = reverse_lazy("mailapp:letter_list")

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return NewsLetterForm
        if user.has_perm("mailapp.can_delete_newsletter") and user.has_perm(
            "mailapp.can_view_newsletter"
        ):
            return NewsLetterModeratorForm
        raise PermissionDenied


class LetterDeleteView(DeleteView):
    model = NewsLetter
    success_url = reverse_lazy("mailapp:letter_list")


# crud для сообщения
class MessageListView(ListView):
    model = Message


class MessageDetailView(DetailView):
    model = Message


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy("mailapp:message_list")


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy("mailapp:message_list")

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return NewsLetterForm
        if (
            user.has_perm("mail_service.can_delete_newsletter")
            and user.has_perm("mailapp.can_view_newsletter")
            and user.has_perm("mailapp.can_delete_client")
            and user.has_perm("mailapp.can_view_client")
        ):
            return NewsLetterModeratorForm
        raise PermissionDenied


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy("mailapp:message_list")


# crud для клиента
class ClientListView(ListView):
    model = Client

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["client_count"] = Client.objects.count()
        return context


class ClientDetailView(DetailView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy("mailapp:client_list")


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy("mailapp:client_list")

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return NewsLetterForm
        if (
            user.has_perm("mail_service.can_delete_newsletter")
            and user.has_perm("mail_service.can_view_newsletter")
            and user.has_perm("mailapp.can_delete_client")
            and user.has_perm("mailapp.can_view_client")
        ):
            return NewsLetterModeratorForm
        raise PermissionDenied


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy("mailapp:client_list")


def index_data(request):
    count_mailing_items = NewsLetter.objects.count()
    count_active_mailing_items = NewsLetter.objects.filter(status="STARTED").count()
    count_unic_clients = Client.objects.values_list("email", flat=True).count()
    random_blogs = Blog.objects.order_by("?")[:3]
    context = {
        "count_mailing_items": count_mailing_items,
        "count_active_mailing_items": count_active_mailing_items,
        "count_unic_clients": count_unic_clients,
        "random_blogs": random_blogs,
    }

    return context


def index_data(request):
    newsletter_count = NewsLetter.objects.count()
    count_active_mailing_items = NewsLetter.objects.filter(status="STARTED").count()
    client_count = Client.objects.count()
    random_blogs = Blog.objects.order_by("?")[:3]
    context = {
        "count_mailing_items": newsletter_count,
        "count_active_mailing_items": count_active_mailing_items,
        "count_unic_clients": client_count,
        "random_blogs": random_blogs,
    }

    return render(request, "mailapp/base.html", context)
