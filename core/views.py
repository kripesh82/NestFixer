from django.shortcuts import redirect, render
from item.models import category, Item
from .forms import SignupForm

# Create your views here.
def index(request):
    items=Item.objects.filter(is_available=True)[0:6]
    categories= category.objects.all()


    return render(request, 'core/index.html',{
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
    
