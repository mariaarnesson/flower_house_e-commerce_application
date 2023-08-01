from django.shortcuts import render

from .models import BlogPost, BlogCategory


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
        queryset = BlogPost.objects.filter(blog_category__name=selected_category, status=1).order_by("-created_on")
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