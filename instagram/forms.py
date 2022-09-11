from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['message','is_public']

# form = PostForm(request.POST)
# if form.is_valid():
#     post = form.save(commit=False)
#     post.author = request.author
#     post.ip = request.META['REMOTE_ADDR']
#     post.save()