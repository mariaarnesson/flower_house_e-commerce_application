from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from .models import BlogPost, BlogCategory, Comment
from .forms import CommentForm
from products.models import Product


def blog_category(request):
    categories = BlogCategory.objects.all()
    template_name = "blog_category.html"

    return render(
        request,
        template_name,
        {
            "categories": categories,
        }
    )


def post_list(request):
    categories = BlogCategory.objects.all()
    selected_category = request.GET.get('category')

    if selected_category:
        queryset = BlogPost.objects.filter(
            blog_category__name=selected_category,
            status=1
        ).order_by("-created_on")
    else:
        queryset = BlogPost.objects.filter(status=1).order_by("-created_on")

    template_name = "florist_blog.html"
    paginate_by = 6

    return render(
        request,
        template_name,
        {
            "post_list": queryset,
            "categories": categories,
            "selected_category": selected_category,
        }
    )


def post_detail(request, slug):
    queryset = BlogPost.objects.filter(status=1)
    blog_post = get_object_or_404(queryset, slug=slug)
    comments = blog_post.comments.filter(approved=True).order_by("-created_on")
    liked = False
    if blog_post.likes.filter(id=request.user.id).exists():
        liked = True

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.blog_post = blog_post
            comment.save()
    else:
        comment_form = CommentForm()

    return render(
        request,
        "post_detail.html",
        {
            "blog_post": blog_post,
            "comments": comments,
            "commented": True if request.method == "POST" else False,
            "comment_form": comment_form,
            "liked": liked,

        },
    )


def post_like(request, slug):
    blog_post = get_object_or_404(BlogPost, slug=slug)
    if blog_post.likes.filter(id=request.user.id).exists():
        blog_post.likes.remove(request.user)
    else:
        blog_post.likes.add(request.user)

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def products_list(request):
    name = request.GET.get('name')
    description = request.GET.get('description')

    queryset = Product.objects.filter(name=name, description=description)

    template_name = "products.html"

    return render(
        request,
        template_name,
        {
            "products": queryset,
        }
    )
