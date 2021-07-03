from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.http import JsonResponse
from django.http import HttpResponse
import json


def find_user(request):
    user = get_object_or_404(User, pk=request.GET.get("userId"))
    result = {'user': user}
    print('result: ', result)

    result = json.dumps(result, default=lambda o: o.__dict__)
    return HttpResponse(result, content_type="application/json")


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
