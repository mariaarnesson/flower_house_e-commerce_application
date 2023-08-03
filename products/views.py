from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product, Category, ProductsFavorites, Review
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from .forms import ProductForm, ReviewForm
from django.core.paginator import Paginator


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
                messages.error(
                    request,
                    "You didn't enter any search criteria!"
                )
                return redirect(reverse('products'))

            queries = (
                Q(name__icontains=query) |
                Q(description__icontains=query)
            )
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

    form = ReviewForm()
    reviews = product.reviews.filter()

    is_favorite = False
    if request.user.is_authenticated:
        is_favorite = ProductsFavorites.objects.filter(
            user=request.user,
            product=product
        ).exists()

    context = {
        'product': product,
        'form': 'form',
        'reviews': reviews,
        'is_favorite': is_favorite,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail',  args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.'
            )
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request,
                           ('Failed to update product. '
                            'Please ensure the form is valid.'))
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def favorites(request):
    favorite_products = Product.objects.filter(
        productsfavorites__user=request.user
    )
    paginator = Paginator(favorite_products, 8)
    page_number = request.GET.get('page')
    favorite_products_page = paginator.get_page(page_number)
    context = {
        'favorite_products': favorite_products_page
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
        messages.success(
            request,
            'The product has been added to your favorites.'
        )

    return redirect('product_detail', product_id=product.id)


@login_required
def remove_from_favorites(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    user = request.user

    favorites_item = user.productsfavorites_set.filter(product=product).first()

    if favorites_item:
        favorites_item.delete()
        messages.success(
            request,
            'The product has been removed from your favorites.'
        )
    else:
        messages.warning(request, 'The product was not in your favorites.')

    return redirect('product_detail', product_id=product_id)


def render_reviews(request):
    reviews = Review.objects.all()
    form = ReviewForm()

    context = {'reviews': reviews, 'review_form': form}
    return render(request, 'product_detail.html', context)


@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST or None)
        if review_form.is_valid():
            data = review_form.save(commit=False)
            data.user = request.user
            data.product = product
            data.save()
            messages.success(request, 'Successfully added review!')
            return redirect(reverse('product_detail',
                                    args=[product.id]))
        else:
            form = ReviewForm()
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')

    context = {'form': form}

    return render(request, context)


@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    product = review.product

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.info(request, 'Your review has been edited!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Error! Please try again.')
    else:
        form = ReviewForm(instance=review)
        messages.info(request, 'Your review is now edited!')

    context = {
        'form': form,
        'review': review,
        'product': product,
        'edit': True,
    }

    return render(request, 'product_detail.html', context)


def delete_review(request, review_id):

    review = get_object_or_404(Review, pk=review_id)
    product = review.product
    review.delete()
    messages.success(request, 'Your review is now deleted!')
    return redirect(reverse('product_detail', args=[product.id]))
