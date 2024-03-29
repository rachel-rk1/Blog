from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post
from .forms import CommentForm

# class based views to map urls from each.


class Postlist(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1)
    template_name = "Blog/index.html"


def post_detail(request, slug):
    template_name = "Blog/post_detail.html"
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(
        request,
        template_name,
        {
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
        },
    )

