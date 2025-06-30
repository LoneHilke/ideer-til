from django.shortcuts import render, redirect
from django.views import View

class Forside(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pversigt/forside.html')
    
class Info(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pversigt/info.html')