# views.py

from django.shortcuts import render
from django.http import HttpResponse
from myproject.db_connect import db


from django.http import JsonResponse
from myproject.db_connect import db



def add_data(request):
    collection = db['test_collection']
    data = {'name': 'Jiwon', 'age': 23}
    collection.insert_one(data)
    return HttpResponse("Data inserted into MongoDB!")


def get_data(request):
    collection = db['test_collection']
    data = list(collection.find({}, {"_id": 0}))  # 모든 데이터를 가져와서 리스트로 변환
    return JsonResponse(data, safe=False)