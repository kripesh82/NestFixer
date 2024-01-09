from django.shortcuts import redirect, render
from item.models import category, Item
from .forms import SignupForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from .forms import EditProfileForm
from django.contrib import messages
from .forms import EditProfileForm, CustomPasswordChangeForm
from django.contrib.auth import logout


# Create your views here.
def index(request):
    items = Item.objects.filter(is_available=True).order_by('-id')[:4]  # Assuming 'is_available' filters availability
    categories = category.objects.all()  # Retrieve all categories

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')

def faq(request):
    return render(request ,'core/faq.html')

def privacy(request):
    return render(request ,'core/privacy.html')

def terms(request):
    return render(request ,'core/terms.html')

def signup(request):
    if request.method=='POST':
        form = SignupForm (request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login')
    
    else:
        form=SignupForm()

    form = SignupForm()
    return render(request, 'core/signup.html', {
        'form':form
    })
    
@login_required
def edit_profile(request):
    if request.method == 'POST':
        if 'change_user_info' in request.POST:
            user_form = EditProfileForm(request.POST, instance=request.user)
            if user_form.is_valid():
                user_form.save()
                messages.success(request, 'Your profile information was successfully updated.')
                return redirect('core:index')
            else:
                messages.error(request, 'Please correct the errors below.')
        elif 'change_password' in request.POST:
            password_form = CustomPasswordChangeForm(user=request.user, data=request.POST)
            if password_form.is_valid():
                password_form.save()
                update_session_auth_hash(request, password_form.user)
                messages.success(request, 'Your password was successfully updated.')
                return redirect('core:index')
            else:
                messages.error(request, 'Please correct the errors below.')
    else:
        user_form = EditProfileForm(instance=request.user)
        password_form = CustomPasswordChangeForm(user=request.user)

    return render(request, 'core/edit_profile.html', {
        'user_form': user_form,
        'password_form': password_form,
    })



@login_required
def delete_account(request):
    if request.method == 'POST':
        request.user.delete()
        logout(request)
        messages.success(request, 'Your account has been successfully deleted.')
        return redirect('core:index')

    user_form = EditProfileForm(instance=request.user)
    password_form = CustomPasswordChangeForm(user=request.user)

    return render(request, 'core/edit_profile.html', {
        'user_form': user_form,
        'password_form': password_form,
    })