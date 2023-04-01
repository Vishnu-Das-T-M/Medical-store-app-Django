from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login_api'),
    path('register/',views.RegisterView.as_view(), name='auth_register'),
    path('medicines/', views.medicine_list),
    path('medicines/<int:pk>/', views.medicine_detail),
    path('meds/', views.MedicineListView.as_view()),

]