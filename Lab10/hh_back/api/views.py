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

@csrf_exempt
def company_detail(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist:
        return JsonResponse({'error': f'Company with id {id} does not exist'}, status=404)

    if request.method == 'GET':
        return JsonResponse(company.to_json())
    if request.method == 'DELETE':
        company.delete()
        return JsonResponse({'message': 'Company deleted successfully'}, status=204)

@csrf_exempt
def vacancies(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        vacancies_json = [vacancy.to_json() for vacancy in vacancies]
        return JsonResponse(vacancies_json, safe=False)
@csrf_exempt
def vacancy_detail(request, id):
    try:
        vacancy = Vacancy.objects.get(id=id)
    except Vacancy.DoesNotExist:
        return JsonResponse({'error': f'Vacancy with id {id} does not exist'}, status=404)

    if request.method == 'GET':
        return JsonResponse(vacancy.to_json())
    if request.method == 'DELETE':
        vacancy.delete()
        return JsonResponse({'message': 'Vacancy deleted successfully'}, status=204)

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