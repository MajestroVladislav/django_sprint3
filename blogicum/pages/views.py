from django.shortcuts import render


# Create your views here.
def about(request):
    t = 'pages/about.html'
    return render(request, t)


def rules(request):
    t = 'pages/rules.html'
    return render(request, t)
