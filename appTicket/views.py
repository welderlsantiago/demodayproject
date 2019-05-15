from django.shortcuts import render

# Create your views here.

# função pra chamar o arquivo html 
def main(request):
    return render(request, 'main.html')
