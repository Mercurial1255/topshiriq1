from django.urls import path
from .views import set_name, name_page, change_data, all, createuser, deleteUser

urlpatterns = [
    path('set-name/', set_name, name='set_name'),
    path('name-page/<str:name>/', name_page, name='name_page'),
    path('change-data/<int:user_id>/', change_data, name='change_data'),
    path('delete-user/<int:user_id>/', deleteUser, name='delete_data'),
    path('add/', createuser, name='add'),
    path('', all, name='all')
]
