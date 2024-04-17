from django.urls import path

from .views import companies, company_detail, vacancies, vacancy_detail, company_vacancy, top10_vacancies

urlpatterns = [
    path('companies/', companies),
    path('companies/<int:id>/', company_detail),
    path('vacancies/', vacancies),
    path('vacancies/<int:id>/', vacancy_detail),
    path('companies/<int:id>/vacancies/', company_vacancy),
    path('vacancies/top_ten/', top10_vacancies)
]