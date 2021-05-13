from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
# Create your views here.

def index(request):
    return render(request,'index.html')


value_list=['apple','pear','banana']
def search_key(request):
    method=request.method
    if method=='POST':
        key=request.body['key']

        for i in value_list:
            if key in value_list:
                return key
            else:
                return HttpResponse(status=404)
