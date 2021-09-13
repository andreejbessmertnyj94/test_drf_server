from django.db import models


class Company(models.Model):
    name = models.CharField("Name", max_length=300)
    headquarter = models.OneToOneField(
        "Office", related_name="headquarter_of", on_delete=models.PROTECT, null=True
    )


class Office(models.Model):
    street = models.CharField("Street", max_length=256, blank=True, null=True)
    postal_code = models.CharField("Postal Code", max_length=32, blank=True, null=True)
    city = models.CharField("City", max_length=128, blank=True, null=True)
    monthly_rent = models.DecimalField(
        decimal_places=2, max_digits=10, blank=True, null=True
    )
    company = models.ForeignKey(
        Company, related_name="offices", on_delete=models.CASCADE
    )
