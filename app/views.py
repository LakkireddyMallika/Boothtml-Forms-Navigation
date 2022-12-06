from django.shortcuts import render

# Create your views here.
def boot_cdn(request):
    return render(request,'boot_cdn.html')


def forms(request):
    return render(request,'forms.html')

def jobapp(request):
    return render(request,'jobapp.html')