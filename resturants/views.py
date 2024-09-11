from django.shortcuts import render

# Create your views here.
def display_res(req):
    return render(req,"d_res.html")