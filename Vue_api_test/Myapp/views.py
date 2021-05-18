import json

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse


# Create your views here.

def index(request):
    return render(request, 'index.html')


value_list = ['apple', 'pear', 'banana']


def load_login(request):
    return render(request, 'login.html')


def search_key(request):
    method = request.method
    if method == 'POST':
        body = json.loads(request.body)
        if "key" not in body:
            return JsonResponse([], safe=False)

        key = body['key']
        ret = []

        for i in value_list:
            if key in i:
                ret.append(i)

        return JsonResponse(ret, safe=False)

    else:
        return HttpResponse(status=404)


fruites = ['apple', 'pear', 'banana', 'orange']


def get_fruits(request):
    return JsonResponse(fruites, safe=False)


def login(request):
    users = [
        {'user': 'user1', 'psw': 'user1'},
        {'user': 'user2', 'psw': 'user2'}
    ]

    method = request.method

    if method == 'POST':
        body = json.loads(request.body)

        if "name" not in body or "psw" not in body:
            return JsonResponse({'success': False}, safe=False)

        for user in users:
            if user['user'] == body['name'] and user['psw'] == body['psw']:
                return JsonResponse({'success': True}, safe=False)
        else:
            return JsonResponse({'success': False}, safe=False)

    else:
        return HttpResponse(status=404)


def style_demo(request):
    return render(request,'style_demo.html')


def component_info(request):
    return render(request,'component_info.html')