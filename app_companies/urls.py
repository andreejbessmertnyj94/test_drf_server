from django.urls import path

from .views import (
    CompanyCreate,
    CompanyHeadquarterUpdate,
    CompanyList,
    CompanyOfficesList,
    CompanyRetrieve,
    OfficeDetail,
    OfficeList,
    company_rent_sum,
)

urlpatterns = [
    path("companies/", CompanyCreate.as_view()),
    path("companies/list/", CompanyList.as_view()),
    path("companies/<int:pk>/", CompanyRetrieve.as_view()),
    path("companies/<int:pk>/headquarter/", CompanyHeadquarterUpdate.as_view()),
    path("companies/<int:pk>/rent/", company_rent_sum),
    path("companies/<int:pk>/offices/", CompanyOfficesList.as_view()),
    path("offices/", OfficeList.as_view()),
    path("offices/<int:pk>/", OfficeDetail.as_view()),
]
