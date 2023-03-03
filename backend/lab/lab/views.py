from django.views import View
from django.shortcuts import render
from django.http import HttpResponse

class index(View):
    def get(self, request):
        return render(request, 'index.html')

class add_question(View):
    def get(self, request):
        return render(request, 'add-question.html', {'quest': True})
    
    def post(self, request):
        return HttpResponse(200)

class question(View):
    def get(self, request):
        return render(request, 'question.html')

class tag(View):
    def get(self, request):
        return render(request, 'tag.html')

class profile(View):
    def get(self, request):
        return render(request, 'profile.html')

class login(View):
    def get(self, request):
        return render(request, 'login.html')

class signup(View):
    def get(self, request):
        return render(request, 'signup.html')