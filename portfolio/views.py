from django.shortcuts import render


def home(requst):
    return render(requst, 'portfolio/home.html')
