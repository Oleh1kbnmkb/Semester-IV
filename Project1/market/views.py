from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, 'index.html')


def about(request):
  return render(request, 'about.html')


def contact(request):
  return render(request, 'contact.html')


def about_me(request):
  return render(request, 'about_me.html')



def sign_up(request):
  return render(request, 'sign_up.html')