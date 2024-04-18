from django.shortcuts import render
import json
from django.http.response import JsonResponse
from ..models import Company, Vacancy
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from ..serializers import CompanySerializer, VacancySerializer


@api_view(["GET", "POST"])
# @csrf_exempt
def companies(request):
    if request.method == 'GET':
        companiess = Company.objects.all()
        companies_json = [company.to_json() for company in companiess]
        return JsonResponse(companies_json, safe=False)
        # serializer = CompanySerializer(companiess, many=True)
        # return JsonResponse(serializer.data)
    elif request.method == 'POST':
        data = json.loads(request.body)
        comp = Company.objects.create(name=data['name'], description=data['description'],
                                      city=data['city'], address=data['address'])
        return JsonResponse(comp.to_json())
        # serializer = CompanySerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # else:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(["GET", "PUT", "DELETE"])
@csrf_exempt
def company_detail(request, id):
    try:
        company = Company.objects.get(id=id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)

    if request.method == 'GET':
        return JsonResponse(company.to_json())
        # serializer = CompanySerializer(company)
        # return Response(serializer.data)
    elif request.method == 'PUT':
        # data = json.loads(request.body)
        # name = data['name']
        # description = data['description']
        # city = data['city']
        # address = data['address']
        # company.name = name
        # company.description = description
        # company.city = city
        # company.address = address
        # company.save()
        # return JsonResponse(company.to_json())
        serializer = CompanySerializer(
            instance=company,
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        company.delete()
        return JsonResponse({}, status=204)
        # company.delete()
        # return Response({"deleted": True})


# @api_view(["GET", "POST"])
@csrf_exempt
def vacancies(request):
    if request.method == 'GET':
        vacanciess = Vacancy.objects.all()
        vacancies_json = [vacancy.to_json() for vacancy in vacanciess]
        return JsonResponse(vacancies_json, safe=False)
        # serializer = VacancySerializer(vacanciess, many=True)
        # return Response(serializer.data)
    elif request.method == 'POST':
        data = json.loads(request.body)
        vac = Vacancy.objects.create(name=data['name'], description=data['description'],
                                      salary=data['salary'], company_id=data['company'])
        return JsonResponse(vac.to_json())
        # serializer = VacancySerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # else:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(["GET", "PUT", "DELETE"])
@csrf_exempt
def vacancy_detail(request, id):
    try:
        vacancy = Vacancy.objects.get(id=id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)
    if request.method == 'GET':
        return JsonResponse(vacancy.to_json())
        # serializer = VacancySerializer(vacancy)
        # return Response(serializer.data)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        name = data['name']
        description = data['description']
        salary = data['salary']
        vacancy.name = name
        vacancy.description = description
        vacancy.salary = salary
        vacancy.save()
        return JsonResponse(vacancy.to_json())
        # serializer = VacancySerializer(
        #     instance=vacancy,
        #     data=request.data
        # )
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data)
        # else:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        vacancy.delete()
        return JsonResponse({}, status=204)
        # return Response({"deleted": True})


def company_vacancy(request, id):
    try:
        company = Company.objects.get(id=id)
        vacanciess = Vacancy.objects.filter(company=company)
        vacancies_json = [vacancy.to_json() for vacancy in vacanciess]
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse(vacancies_json, safe=False)


def top10_vacancies(request):
    vacanciess = Vacancy.objects.all().order_by('-salary')[:10]
    vacancies_json = [vacancy.to_json() for vacancy in vacanciess]
    return JsonResponse(vacancies_json, safe=False)
