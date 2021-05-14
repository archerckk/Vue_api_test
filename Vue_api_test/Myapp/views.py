import json

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse


# Create your views here.

def index(request):
    return render(request, 'index.html')


value_list = ['apple', 'pear', 'banana']


def search_key(request):
    method = request.method
    if method == 'POST':
        body = json.loads(request.body)
        if "key" not in body:
            return JsonResponse([], safe=False)

        key = body['key']
        ret=[]

        for i in value_list:
            if key in i:
                ret.append(i)

        return JsonResponse(ret, safe=False)

    else:
        return HttpResponse(status=404)
