from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm ' : '2306275651',
        'name ' : 'Athallah Nadhif Yuzak ganteng',
        'class ' : 'PBP B'
    }
    return render(request, 'main.html', context)