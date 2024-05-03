from django.contrib.auth import login, authenticate
from django.core.checks import messages
from django.shortcuts import render
from werkzeug.utils import redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
  return render(request, 'index.html')


def about(request):
  return render(request, 'about.html')


def contact(request):
  return render(request, 'contact.html')


def about_me(request):
  return render(request, 'about_me.html')

def admin_page(request):
  return render(request, 'admin.html')



def register(request):
  return render(request, 'register.html')


def login1(request):
  return render(request, 'login.html')



def register_user(request):
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data['username']
      password = form.cleaned_data['password1']
      user = authenticate(username=username, password=password)
      login(request, user)
      return redirect('home')
  else:
    form = UserCreationForm()
  return render(request, 'register_user.html', {
    'form': form,
  })