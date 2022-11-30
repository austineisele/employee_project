from django.urls import path
from . import views

urlpatterns = [
    #this will show us the add form - this is for the GET and INSERT operation
    path('', views.employee_form, name='employee_insert'),
    #this will be the update path. The first part is the parameter <int:id>
    path('<int:id>/', views.employee_form, name='employee_update'),
    path('delete/<int:id>/', views.employee_delete, name='employee_delete'),
    #add for the list function page view - this is GET request to retreive and display all records
    path('list/', views.employee_list, name='employee_list')
]
