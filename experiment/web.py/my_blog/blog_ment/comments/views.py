from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from .models import Comment
from .forms import CommentForm

# Create your views here.

@login_required
def add_comment(request, content_type_id, object_id):
    content_type = get_object_or_404(ContentType, id=content_type_id)
    content_object = content_type.get_object_for_this_type(id=object_id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.content_type = content_type
            comment.object_id = object_id
            comment.save()
            return redirect(request.POST.get('next', '/'))
    else:
        form = CommentForm()
    
    return render(request, 'comments/add_comment.html', {
        'form': form,
        'content_object': content_object,
    })