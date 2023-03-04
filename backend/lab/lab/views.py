from django.views import View
from django.shortcuts import render
from django.http import HttpResponse

PER_PAGE = 10

def paginate(objects_list: list, page: int, per_page=PER_PAGE):
    page -= 1
    start = page*per_page
    end = page*per_page + per_page
    return objects_list[start:end]

class index(View):
    def get(self, request):

        questions = [{
            'title': 'title ' + str(i),
            'id': i,
            'text': 'text' + str(i)
        } for i in range(30)]

        pages = len(questions) // PER_PAGE
        page = int(request.GET.get('page', 1))
        questions = paginate(questions, page)
        
        config = {
            'pages': range(1, pages + 1),
            'questions' : questions
        }
        return render(request, 'index.html', config)

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