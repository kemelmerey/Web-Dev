from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Company, Vacancy
import json

@csrf_exempt
def companies(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        companies_json = [company.to_json() for company in companies]
        return JsonResponse(companies_json, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        company = Company.objects.create(name=data['name'], description=data['description'],city=data['city'],address=data['address'])
        return JsonResponse(company.to_json(), status=201)

@csrf_exempt
def company_detail(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist:
        return JsonResponse({'error': f'Company with id {id} does not exist'}, status=404)

    if request.method == 'GET':
        return JsonResponse(company.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        company.name = data.get('name', company.name)
        company.description = data.get('description', company.description)
        company.city=data.get('city',company.city)
        company.address=data.get('address',company.address)
        company.save()
        return JsonResponse(company.to_json())
    elif request.method == 'DELETE':
        company.delete()
        return JsonResponse({'message': 'Company deleted successfully'}, status=204)

@csrf_exempt
def vacancies(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        vacancies_json = [vacancy.to_json() for vacancy in vacancies]
        return JsonResponse(vacancies_json, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        vacancy = Vacancy.objects.create(name=data['name'], description=data['description'], salary=data['salary'], company=['company'])
        return JsonResponse(vacancy.to_json(), status=201)

@csrf_exempt
def vacancy_detail(request, id):
    try:
        vacancy = Vacancy.objects.get(id=id)
    except Vacancy.DoesNotExist:
        return JsonResponse({'error': f'Vacancy with id {id} does not exist'}, status=404)

    if request.method == 'GET':
        return JsonResponse(vacancy.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        vacancy.name = data.get('name', vacancy.name)
        vacancy.description=data.get('description',vacancy.description)
        vacancy.salary = data.get('salary', vacancy.salary)
        vacancy.company=data.get('company',company.name)
        vacancy.save()
        return JsonResponse(vacancy.to_json())
    elif request.method == 'DELETE':
        vacancy.delete()
        return JsonResponse({'message': 'Vacancy deleted successfully'}, status=204)

@csrf_exempt
def company_vacancy(request, id):
    try:
        company = Company.objects.get(id=id)
        vacancies = Vacancy.objects.filter(company=company)
        vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    except Company.DoesNotExist:
        return JsonResponse({'error': f'Company with id {id} does not exist'}, status=404)

    return JsonResponse(vacancies_json, safe=False)

def top10_vacancies(request):
    vacancies = Vacancy.objects.all().order_by('-salary')[:10]
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)

