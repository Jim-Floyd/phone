from django.urls import path
from . import views

app_name = 'contact'
urlpatterns = [
    path('list/', views.contact_list_page, name='list'),
    path('get/<int:pk>', views.details, name='details'),
    path('create_page/', views.create_page, name='create_page'),
    path('create/', views.create, name='create'),
    path('delete_page/', views.delete_page, name='delete_page'),
    path('delete/', views.delete, name='delete')
]