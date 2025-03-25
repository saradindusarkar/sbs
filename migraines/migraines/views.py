from django.shortcuts import render


def index_view(request):
    return render(request, 'index.html')
    #return redirect('/dlog/login')


def about_view(request):
    return render(request, 'about.html')
