from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ..models import Company, Vacancy
import json
from ..serializers import CompanySerializer

@csrf_exempt
def companies(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer(companies,many=True)
        # companies_json = [company.to_json() for company in companies]
        # return JsonResponse(companies_json, safe=False)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data=json.loads(request.body)
        # company=Company.objects.create(name=data.get('name'), description=data.get('description'),city=data.get('city'),address=data.get('address'))
        # return JsonResponse(company.to_json())
        serializer=CompanySerializer(data=data)
        if serializer.is_valid():
            serializer.save() #insert into table
            return JsonResponse(serializer.data, status=201)
        return JsonReesponse(serializer.errors, status=400)

@csrf_exempt
def company_detail(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist:
        return JsonResponse({'error': f'Company with id {id} does not exist'}, status=404)

    if request.method == 'GET':
        # return JsonResponse(company.to_json())
        serializer = CompanySerializer(company)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        # company.name = data.get('name', company.name)
        # company.description = data.get('description', company.description)
        # company.city = data.get('city', company.city)
        # company.address = data.get('address', company.address)
        # company.save()
        # return JsonResponse(company.to_json())
        serializer = CompanySerializer(
            instance = company,
            data = data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save() #update table
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
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
        data=json.loads(request.body)
        vacancy=Vacancy.objects.create(name=data.get('name'), description=data.get('description'),salary=data.get('salary'),company=data.get('company'))
        return JsonResponse(vacancy.to_json())

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
        vacancy.description = data.get('description', vacancy.description)
        vacancy.salary = data.get('salary', vacancy.salary)
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
        vacancy.description = data.get('description', vacancy.description)
        vacancy.salary = data.get('salary', vacancy.salary)
        new_company_name = data.get('company')
        if new_company_name is not None:
            try:
                new_company = Company.objects.get(name=new_company_name)
                vacancy.company = new_company
            except Company.DoesNotExist:
                    return JsonResponse({'error': f'Company with name {new_company_name} does not exist'}, status=400)
        vacancy.save()
        return JsonResponse(vacancy.to_json())


    elif request.method == 'DELETE':
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