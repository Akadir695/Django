from django.shortcuts import render
from django.http import HttpResponse

def home_page_view(request): 
    return HttpResponse("Hello, world!")  # ✅ Correct response



def about_page_view(request):
    context = {"name": "Mohamed", "age": 20}
    return render(request, 'pages/about.html', context)  # This matches the directory inside templates