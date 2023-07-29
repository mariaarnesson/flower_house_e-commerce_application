from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category, ProductsFavorites
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    is_favorite = False
    if request.user.is_authenticated:
        is_favorite = ProductsFavorites.objects.filter(user=request.user, product=product).exists()


    context = {
        'product': product,
        'is_favorite': is_favorite,
    }

    return render(request, 'products/product_detail.html', context)

@login_required
def favorites(request):
    favorite_products = Product.objects.filter(productsfavorites__user=request.user)

    context = {
        'favorite_products': favorite_products
    }
    return render(request, 'products/favorites.html', context)


@login_required
def add_to_favorites(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    user = request.user

    if user.productsfavorites_set.filter(product=product).exists():
        messages.warning(request, 'The product is already in your favorites.')
    else:
        ProductsFavorites.objects.create(user=user, product=product)
        messages.success(request, 'The product has been added to your favorites.')

    return redirect('product_detail', product_id=product.id)


@login_required
def remove_from_favorites(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    user = request.user

    favorites_item = user.productsfavorites_set.filter(product=product).first()

    if favorites_item:
        favorites_item.delete()
        messages.success(request, 'The product has been removed from your favorites.')
    else:
        messages.warning(request, 'The product was not in your favorites.')

    return redirect('product_detail', product_id=product_id)