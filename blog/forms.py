from .models import Comment, BlogPost
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

        labels = {
            'body': 'Your Comment',
        }
        widgets = {
            'body': forms.Textarea(attrs={
                'placeholder': 'Write your comment here...',
                'rows': 4,
                'class': 'form-control',
            }),
        }

    def clean_body(self):
        body = self.cleaned_data['body']

        return body
