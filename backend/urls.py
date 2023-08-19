from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("rest_framework.urls")),
    # including application_name.urls
    
    # In Django's URL configuration, the namespace parameter is used to provide a unique identifier for a set of URLs defined within an included URL configuration. It's especially useful when you have multiple applications with their own sets of URLs and you want to avoid naming conflicts between them.
    path("products/", include("products.urls", namespace="products")),
]
