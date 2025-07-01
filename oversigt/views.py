from django.shortcuts import render, redirect
from django.views import View

class Forside(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pversigt/forside.html')
    
class Info(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pversigt/info.html')
    
class Fane(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pversigt/fane.html')
    
class Tab(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pversigt/tap.html')
    
class Rul(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pversigt/rul.html')
    
class Ikon(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pversigt/ikon.html')
    
class Tekst(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pversigt/tekst.html')
    
class Side(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pversigt/side.html')
    
class Knap(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'pversigt/knapper.html')