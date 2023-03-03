from django.views import View
from django.shortcuts import render
from django.http import HttpResponse

class index(View):
    def get(self, request):
        return render(request, 'index.html')