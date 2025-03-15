from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text'] #确保只提交评论文本
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4, 'cols': 50, 'placeholder': '请输入您的评论...'}),
        }