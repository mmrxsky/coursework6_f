from django.forms import ModelForm, BooleanField

from mailapp.models import Message, Client, NewsLetter


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = "form-check-input"
            else:
                fild.widget.attrs['class'] = "form-control"


class NewsLetterForm(StyleFormMixin, ModelForm):
    class Meta:
        model = NewsLetter
        fields = '__all__'


class NewsLetterModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = NewsLetter
        exclude = ('owner', 'count')


class MessageForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Message
        fields = '__all__'


class ClientForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Client
        fields = '__all__'