from django.urls import path
from . import views


urlpatterns = [
    path('v1/items', views.manage_items, name="items"),
    path('v1/items/<slug:key>', views.manage_item, name="single_item")
]
