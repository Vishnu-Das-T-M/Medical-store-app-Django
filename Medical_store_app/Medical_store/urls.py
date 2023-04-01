from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('medicine/list', views.MedicineList.as_view(), name='medicine_list'),
    path('medicine/create/', views.MedicineCreate.as_view(), name='medicine_create'),
    path('medicine/<int:pk>/update/', views.MedicineUpdate.as_view(), name='medicine_update'),
    path('medicine/<int:pk>/delete/', views.MedicineDelete.as_view(), name='medicine_delete'),
    path("register/", views.register_request, name="register"),
    path("search/", views.search_product, name="search"),
]