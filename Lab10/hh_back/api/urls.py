from django.urls import path

from .views import *

urlpatterns = [
    path('companies/', companies),
    path('companies/<int:id>/', company_detail),
    path('vacancies/', vacancies),
    path('vacancies/<int:id>/', vacancy_detail),
    path('companies/<int:id>/vacancies/', company_vacancy),
    path('vacancies/top_ten/', top10_vacancies)
]