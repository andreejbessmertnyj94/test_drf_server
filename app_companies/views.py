from django.db.models import Sum
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Company, Office
from .serializers import (
    CompanyCreateSerializer,
    CompanyHeadquarterUpdateSerializer,
    CompanyListSerializer,
    CompanyViewSerializer,
    OfficeCreateSerializer,
    OfficeSerializer,
)


class CompanyCreate(generics.CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyCreateSerializer


class CompanyList(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanyListSerializer


class CompanyRetrieve(generics.RetrieveAPIView):
    serializer_class = CompanyViewSerializer

    def get_queryset(self):
        return Company.objects.filter(pk=self.kwargs["pk"])


class CompanyHeadquarterUpdate(generics.UpdateAPIView):
    serializer_class = CompanyHeadquarterUpdateSerializer

    def get_queryset(self):
        return Company.objects.filter(pk=self.kwargs["pk"])


class CompanyOfficesList(generics.ListAPIView):
    serializer_class = OfficeSerializer

    def get_queryset(self):
        return Office.objects.filter(company_id=self.kwargs["pk"])


@api_view(["GET"])
def company_rent_sum(request, pk):
    """
    sum of rent for all offices of a Company
    """
    company_rent = Company.objects.filter(pk=pk).aggregate(Sum("offices__monthly_rent"))
    return Response(company_rent)


class OfficeList(generics.ListCreateAPIView):
    # TODO remove later
    queryset = Office.objects.all()
    serializer_class = OfficeCreateSerializer


class OfficeDetail(generics.RetrieveUpdateDestroyAPIView):
    # TODO remove later
    serializer_class = OfficeSerializer

    def get_queryset(self):
        return Office.objects.filter(pk=self.kwargs["pk"])
