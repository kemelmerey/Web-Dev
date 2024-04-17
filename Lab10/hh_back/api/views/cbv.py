import json
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from ..models import Company, Vacancy
from ..serializers import CompanySerializer, VacancySerializer, CompanySerializer2


class CompanyListCreateAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CompanySerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyDetailAPIView(APIView):
    permission_classes = [AllowAny]
    def get_object(self, id):
        try:
            company = Company.objects.get(id=id)
            return company
        except Company.DoesNotExist as e:
            return Response({"error": str(e)})

    def get(self, request, id):
        company = self.get_object(id)
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    def put(self, request, id):
        company = self.get_object(id)
        serializer = CompanySerializer2(
            instance=company,
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        company = self.get_object(id)
        company.delete()
        return Response({"deleted": True})




class VacancyListCreateAPIView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        vacanciess = Vacancy.objects.all()
        serializer = VacancySerializer(vacanciess, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VacancySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#
# @api_view(["GET", "POST"])
# def vacancies(request):
#     if request.method == 'GET':
#         vacanciess = Vacancy.objects.all()
#         # vacancies_json = [vacancy.to_json() for vacancy in vacanciess]
#         # return JsonResponse(vacancies_json, safe=False)
#         serializer = VacancySerializer(vacanciess, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         # data = json.loads(request.body)
#         # vac = Vacancy.objects.create(name=data['name'], description=data['description'],
#         #                               salary=data['salary'], company_id=data['company'])
#         # return JsonResponse(vac.to_json())
#         serializer = VacancySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VacancyDetailAPIView(APIView):
    permission_classes = [AllowAny]
    def get_object(self, id):
        try:
            vacancy = Vacancy.objects.get(id=id)
            return vacancy
        except Vacancy.DoesNotExist as e:
            return Response({"error": str(e)})

    def get(self, request, id):
        vacancy = self.get_object(id)
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data)

    def put(self, request, id):
        vacancy = self.get_object(id)
        serializer = VacancySerializer(
            instance=vacancy,
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        vacancy = self.get_object(id)
        vacancy.delete()
        return Response({"deleted": True})




#
# @api_view(["GET", "PUT", "DELETE"])
# def vacancy_detail(request, id):
#     try:
#         vacancy = Vacancy.objects.get(id=id)
#     except Vacancy.DoesNotExist as e:
#         return JsonResponse({'error': str(e)}, status=400)
#     if request.method == 'GET':
#         # return JsonResponse(vacancy.to_json())
#         serializer = VacancySerializer(vacancy)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         # data = json.loads(request.body)
#         # name = data['name']
#         # description = data['description']
#         # salary = data['salary']
#         # vacancy.name = name
#         # vacancy.description = description
#         # vacancy.salary = salary
#         # vacancy.save()
#         # return JsonResponse(vacancy.to_json())
#         serializer = VacancySerializer(
#             instance=vacancy,
#             data=request.data
#         )
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         vacancy.delete()
#         # return JsonResponse({}, status=204)
#         return Response({"deleted": True})


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
