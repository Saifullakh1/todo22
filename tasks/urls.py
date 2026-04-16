from django.urls import path
from .views import list, detail, update, delete, create

urlpatterns = [
    path('', list, name='list'),
    path('create', create, name='create'),
    path('<int:id>', detail, name='detail'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete')
]