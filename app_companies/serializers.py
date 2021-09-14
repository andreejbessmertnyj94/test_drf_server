from rest_framework import serializers

from .models import Company, Office


class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = [
            "id",
            "street",
            "postal_code",
            "city",
            "monthly_rent",
            "headquarter_of",
        ]


class OfficeCreateSerializer(OfficeSerializer):
    class Meta(OfficeSerializer.Meta):
        fields = [
            "street",
            "postal_code",
            "city",
            "company",
        ]


class HeadquarterSerializer(OfficeSerializer):
    class Meta(OfficeSerializer.Meta):
        fields = [
            "street",
            "postal_code",
            "city",
        ]


class CompanyViewSerializer(serializers.ModelSerializer):
    headquarter = HeadquarterSerializer(read_only=True)

    class Meta:
        model = Company
        fields = ["id", "name", "headquarter"]


class HeadquarterField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        company_id = self.context.get("request").parser_context.get("kwargs").get("pk")
        return Office.objects.all().filter(company_id=company_id)


class CompanyHeadquarterUpdateSerializer(CompanyViewSerializer):
    headquarter = HeadquarterField()

    class Meta(CompanyViewSerializer.Meta):
        fields = ["headquarter"]


class CompanyListSerializer(CompanyViewSerializer):
    headquarter = None

    class Meta(CompanyViewSerializer.Meta):
        fields = ["id", "name"]


class CompanyCreateSerializer(CompanyViewSerializer):
    offices = HeadquarterSerializer(many=True)
    headquarter = HeadquarterSerializer()

    class Meta(CompanyViewSerializer.Meta):
        fields = ["id", "name", "offices", "headquarter"]

    def create(self, validated_data):
        offices_data = validated_data.pop("offices")
        headquarter_data = validated_data.pop("headquarter")
        company = Company.objects.create(**validated_data)
        headquarter = Office.objects.create(company=company, **headquarter_data)
        company.headquarter = headquarter
        company.save()
        for office_data in offices_data:
            Office.objects.create(company=company, **office_data)
        return company
