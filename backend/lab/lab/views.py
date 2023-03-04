from django.views import View
from django.shortcuts import render
from django.http import HttpResponse

PER_PAGE = 10

def paginate(objects_list: list, page: int, per_page=PER_PAGE):
    return objects_list[page*per_page::per_page]

class index(View):
    def get(self, request):
        questions = [{
            'title': 'title ' + str(i),
            'id': i,
            'text': 'text' + str(i)
        } for i in range(30)]
        try:
            page = int(request.query_params['page'])
            questions = paginate(questions, page)
        except KeyError:
            questions = questions[:10]
        config = {
            
        }
        return render(request, 'index.html', {'questions': questions})

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