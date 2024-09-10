from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Darren Marcello Sidabutar',
        'class': 'PBP KKI',
        'name_app': 'E-Commerce',
    }

    return render(request, "main.html", context)