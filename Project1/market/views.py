from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Stuff, NewArrivals, FeaturedProduct, TopProduct, Basket
from .forms import ProductForm
from django.core.paginator import Paginator
from .forms import RegisterUserForm, NewArrivalsForm
from django.contrib.auth import authenticate, login
from django.contrib import messages




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
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
      login(request, user)
      messages.success(request, f'Welcome {user.username}!')
      return redirect('index')
    else:
      messages.error(request, 'Invalid username or password.')

  return render(request, "registration/login.html")


def index(request):
  user = request.user
  products = Product.objects.all()
  stuff = Stuff.objects.all()
  featured_products = FeaturedProduct.objects.all()
  top_products = TopProduct.objects.all()
  newarrivals = list(NewArrivals.objects.all())
  paginator = Paginator(newarrivals, 3)
  page = request.GET.get('page')
  paginated_list = paginator.get_page(page)

  response = render(request, 'index.html', {
    'products': products,
    'stuff': stuff,
    'newarrivals': newarrivals,
    'paginated_list': paginated_list,
    'featured_products': featured_products,
    'top_products': top_products,
    'user': user,
  })
  request.session.flush()
  return response


def add_product(request):
  if request.method == 'POST':
    form = ProductForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('index')
  else:
    form = ProductForm()

  return render(request, 'admin.html', {'form': form})


def settings(request):
    return render(request, 'settings.html')


def edit(request):
  newarrivals = NewArrivals.objects.all()
  response = render(request, 'products_edit.html', {
    'newarrivals': newarrivals,
  })

  return response


def delete(request):
  newarrivals = NewArrivals.objects.all()
  response = render(request, 'products_delete.html', {
    'newarrivals': newarrivals,
  })

  return response


def update_prod(request, arrivals_id):
  arrivals = NewArrivals.objects.get(pk=arrivals_id)
  form = NewArrivalsForm(request.POST or None, instance=arrivals)
  if form.is_valid():
    form.save()
    return redirect('edit')
  return render(request, 'update_products.html',
                {
                  'arrivals': arrivals,
                  'form': form,
                })



def delete_prod(request, arrivals_id):
  arrivals = NewArrivals.objects.get(pk=arrivals_id)
  arrivals.delete()
  return redirect('delete')


def add_to_basket(request, product_id):
  if request.method == "POST":
    if 'basket' not in request.session:
      request.session['basket'] = {}
    basket = request.session['basket']
    if str(product_id) in basket:
      basket[str(product_id)] += 1
    else:
      basket[str(product_id)] = 1
    request.session.modified = True
    product = get_object_or_404(NewArrivals, id=product_id)
    session_key = request.session.session_key
    if not session_key:
      request.session.create()
      session_key = request.session.session_key
    basket_item, created = Basket.objects.get_or_create(session_key=session_key, product=product)
    if not created:
      basket_item.count += 1
    else:
      basket_item.count = 1
    basket_item.save()
    return redirect('view_basket')
  else:
    return redirect('index')


def view_basket(request):
  basket_items = Basket.objects.all()
  return render(request, 'basket.html', {'basket_items': basket_items})
