from django.shortcuts import render, redirect
from .models import Product, Stuff, NewArrivals, BestSellers, FeaturedProduct, TopProduct
from .forms import ProductForm
from itertools import chain
from django.core.paginator import Paginator
from .forms import RegisterUserForm, LoginForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def about_me(request):
  return render(request, 'about_me.html')


def about(request):
  return render(request, 'about.html')


def contact(request):
  return render(request, 'contact.html')


def shop(request):
  return render(request, 'shop.html')


def sign_up(request):
  if request.method == "POST":
    form = RegisterUserForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data['username']
      password = form.cleaned_data['password1']
      user = authenticate(username=username, password=password)
      login(request, user)
      return redirect("index")
  else:
    form = RegisterUserForm()
  return render(request, 'registration/sign_up.html', {'form': form})


def my_login(request):
  form = LoginForm()
  if request.method == 'POST':
    form = LoginForm(request, data=request.POST)
    if form.is_valid():
      username = request.POST.get('username')
      password = request.POST.get('password')
      user = authenticate(request, username=username, password=password)
      if user is not None:
        auth.login(request, user)
        return redirect("index")
  context = {'loginform': form}
  return render(request, "registration/login.html", context=context)


def index(request):
  products = Product.objects.all()
  stuff = Stuff.objects.all()
  featured_products = FeaturedProduct.objects.all()
  top_products = TopProduct.objects.all()
  newarrivals = list(NewArrivals.objects.all())
  bestsellers = list(BestSellers.objects.all())
  combined_list = list(chain(newarrivals, bestsellers))

  paginator = Paginator(combined_list, 2)
  page = request.GET.get('page')
  paginated_list = paginator.get_page(page)

  visits = int(request.COOKIES.get('visits', '0'))
  visits += 1

  response = render(request, 'index.html', {
    'products': products,
    'stuff': stuff,
    'newarrivals': newarrivals,
    'paginated_list': paginated_list,
    'bestsellers': bestsellers,
    'featured_products': featured_products,
    'top_products': top_products,
    'visits': visits
  })
  response.set_cookie('visits', visits)
  return response


@login_required
def add_product(request):
  if not request.user.is_superuser:
    return redirect('index')

  if request.method == 'POST':
    form = ProductForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('index')
  else:
    form = ProductForm()

  return render(request, 'admin.html', {'form': form})


def ad_lists(request):
  if not request.user.is_superuser:
    return redirect('index')
  featured_products = FeaturedProduct.objects.all()
  top_products = TopProduct.objects.all()
  return render(request, 'ad_list.html', {'featured_products': featured_products, 'top_products': top_products})
