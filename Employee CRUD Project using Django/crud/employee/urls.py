from django.urls import path
# from .views import Home
from .views import create_employee, update_employee, employee_list, delete_employee

urlpatterns=[
    # path('',Home)
    path('', employee_list, name="list"),
    path('create/', create_employee, name="create"),
    path('update/<int:pk>/', update_employee, name="update"),
    path('delete/<int:pk>/', delete_employee, name="delete")
]