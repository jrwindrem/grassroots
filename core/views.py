from django.shortcuts import render
def home(request):
    ctx = {
    }
    return render(request, 'grassroots/home.html', ctx)