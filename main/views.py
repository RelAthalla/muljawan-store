from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306223925',
        'name': 'Farrel Athalla Muljawan',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)