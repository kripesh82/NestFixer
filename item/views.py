from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Item, category
from django.contrib.auth.decorators import login_required
from .forms import NewItemForm, EditItemForm
from django.db.models import Avg


def items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('Category' , 0)
    categories = category.objects.all()
    items = Item.objects.filter(is_available=True)

    if category_id:
        items = items.filter(Category__id=category_id)
    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query) )

    return render(request, 'item/items.html', {
        'items':items,
        'query': query,
        'categories':categories,
        'category_id': int(category_id),
    })

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(Category=item.Category, is_available=True).exclude(pk=pk)[0:3]

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('item:detail', pk=item.id)

    else:
        form = NewItemForm()

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New Item'
    })

@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    return redirect('dashboard:index')



@login_required
def edit(request,pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES , instance=item)

        if form.is_valid():
            form.save()
            return redirect('item:detail', pk=item.id)

    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit item'
    })




# views.py
from .forms import CommentForm, ReviewForm

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(Category=item.Category, is_available=True).exclude(pk=pk)[0:3]

    comment_form = CommentForm()
    review_form = ReviewForm()

    if request.method == 'POST':
        if 'comment_submit' in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.user = request.user
                comment.item = item
                comment.save()
        elif 'review_submit' in request.POST:
            review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.user = request.user
                review.item = item
                review.save()

    # Calculate average rating
    avg_rating = item.reviews.aggregate(Avg('rating'))['rating__avg']

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items,
        'comment_form': comment_form,
        'review_form': review_form,
        'avg_rating': avg_rating,
    })


# views.py
from .forms import CommentForm, ReviewForm

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(Category=item.Category, is_available=True).exclude(pk=pk)[0:3]

    comment_form = CommentForm()
    review_form = ReviewForm()

    if request.method == 'POST':
        if 'comment_submit' in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.user = request.user
                comment.item = item
                comment.save()
        elif 'review_submit' in request.POST:
            review_form = ReviewForm(request.POST)
            if review_form.is_valid():
                review = review_form.save(commit=False)
                review.user = request.user
                review.item = item
                review.save()

    # Calculate average rating
    avg_rating = item.reviews.aggregate(Avg('rating'))['rating__avg']

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items,
        'comment_form': comment_form,
        'review_form': review_form,
        'avg_rating': avg_rating,
    })



# views.py
from django.shortcuts import redirect

@login_required
def new_comment(request, pk):
    item = get_object_or_404(Item, pk=pk)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.item = item
            comment.save()

    return redirect('item:detail', pk=pk)
