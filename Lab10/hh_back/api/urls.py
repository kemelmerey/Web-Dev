from django.urls import path

# from .views import companies, company_detail, vacancies, vacancy_detail, company_vacancy, top10_vacancies
from .views import *

urlpatterns = [
    # path('companies/', CompanyListCreateAPIView.as_view()),
    # path('companies/<int:id>/', CompanyDetailAPIView.as_view()),
    path('companies/', companies),
    path('companies/<int:id>/', company_detail),
    path('vacancies/', vacancies),
    # path('vacancies/', VacancyListCreateAPIView.as_view()),
    path('vacancies/<int:id>/', vacancy_detail),
    # path('vacancies/<int:id>/', VacancyDetailAPIView.as_view()),
    path('companies/<int:id>/vacancies/', company_vacancy),
    path('vacancies/top_ten/', top10_vacancies)
]