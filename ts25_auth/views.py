from django.shortcuts import render, get_object_or_404, redirect
from ts25_auth.models import User
from rest_framework.response import Response
from django.http import JsonResponse
from django.http import HttpResponse
import json
import datetime


"""
request.GET은 django에서 사용할 수 있다. 아까 방금 확인했지만 
request는 Http 리퀘스트가 보내졌을 때에 Django가 만든 객체이다. 
그리고 request.GET을 실행하는 것으로, request의 정보를 사전형의 데이터로 얻을 수 있게 된다.
"""
def find_user(request):
    user = get_object_or_404(User, pk=request.GET.get("userid"))
    result = {'user': user}
    print('result: ', result)

    result = json.dumps(result, default=lambda o: o.__dict__)
    return HttpResponse(result, content_type="application/json")


"""
request.get은 dictionary value값을 get하는 python method.
django에 function based view를 정의할 때의 인수로써 설정하는 'request'는 
사전형 데이터가 아닌 것을 주의하자.
"""
def login_check(request):
    user = get_object_or_404(User, pk=request.POST.get("userid"))
    result = {'user': user}
    print('result: ', result)

    result = json.dumps(result, default=lambda o: o.__dict__)
    return HttpResponse(result, content_type="application/json")

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

def viewArticle(request, articleId):
   text = "Displaying article Number : %s"%articleId
   return HttpResponse(text) ##HttpResponse(django) 리턴.

def hello(request):
    today = datetime.datetime.now().date()
    # return render(request, "hello.html", {"today":today}) ## render(): template를 return할 때.
    return redirect("https://www.djangoproject.com")