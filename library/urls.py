from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from library.books import views


router = routers.DefaultRouter()
router.register(r"authors", views.AuthorViewSet)
router.register(r"books", views.BookViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
