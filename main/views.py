from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name' : 'Barbell',
        'price': 'Rp100.000',
        'description': 'For training purposes'
    }

    return render(request, "main.html", context)