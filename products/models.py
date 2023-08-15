from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres import fields as postgresFields


# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=256)
    icon_url = models.URLField(blank=True)
    description = models.TextField()
    parent_category = models.ForeignKey(
        # we are using self because we are referencing the same model
        "self",
        # blank and null are used to make the field optional
        blank=True,
        null=True,
        # related_name is used to access the child categories of a parent category
        related_name="child_categories",
        # if the parent category is deleted then delete all the child categories
        on_delete=models.CASCADE,
    )

    # we are telling django that use the name field as the representational field for this model
    def __str__(self):
        return self.name


class Maker(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    class Currency(models.TextChoices):
        SWEDISH_CROWNS = "SEK", _("Swedish Crown")
        AMERICAN_DOLLLAR = ("USD", _("US Dollars"))
        EUROS = ("EUR", _("Euro"))
        POUND_STERLING = ("GBP", _("Pound Sterling"))
        YEN = ("JPY", _("Yen"))
        INDIAN_RUPEE = ("INR", _("Indian Rupee"))
        AUSTRALIAN_DOLLAR = ("AUD", _("Australian Dollar"))

    title = models.CharField(max_length=256)
    subtitle = models.CharField(max_length=256, blank=True)
    maker = models.ForeignKey(
        Maker, on_delete=models.CASCADE, related_name="products", blank=True, null=True
    )

    image1_url = models.URLField(blank=True, null=True)
    image2_url = models.URLField(blank=True, null=True)
    image3_url = models.URLField(blank=True, null=True)
    image4_url = models.URLField(blank=True, null=True)

    price = models.DecimalField(max_digits=10, decimal_places=2)

    currency = models.CharField(
        max_length=3, choices=Currency.choices, default=Currency.AMERICAN_DOLLLAR
    )

    variation_product_ids= postgresFields.ArrayField(
        models.IntegerField(null=True,blank=True),
        null=True,
        blank=True
    )

    def __str__(self) -> str:
        return f"{self.title} - {self.subtitle} - {self.maker}"
