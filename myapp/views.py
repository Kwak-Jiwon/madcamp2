# views.py

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from myproject.db_connect import db
from bson import ObjectId


def add_data(request):
    collection = db['test_collection']
    data = {'name': 'Jae-hyun', 'age': 17}
    collection.insert_one(data)
    return HttpResponse("Data inserted into MongoDB!")

def get_data(request):
    collection = db['test_collection']
    data = list(collection.find({}, {"_id": 0}))  # 모든 데이터를 가져와서 리스트로 변환
    return JsonResponse(data, safe=False)


def delete_data(request, data_id):
    collection = db['test_collection']
    result = collection.delete_one({'_id': ObjectId(data_id)})
    if result.deleted_count == 1:
        return HttpResponse("Data deleted successfully!")
    else:
        return HttpResponse("Data not found.", status=404)

def update_data(request, data_id):
    collection = db['test_collection']
    new_data = {'name': 'Jane Doe', 'age': 25}  # 업데이트할 데이터 예시
    result = collection.update_one({'_id': ObjectId(data_id)}, {'$set': new_data})
    if result.matched_count == 1:
        return HttpResponse("Data updated successfully!")
    else:
        return HttpResponse("Data not found.", status=404)