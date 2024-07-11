from django.urls import path
from blog import views


app_name = "blog"
urlpatterns = [
    path('posts/', views.show_all, name='show_all'),
    path('<slug:slug>/', views.show_detail, name='show_detail'),
    path('delete/<int:id>/', views.delete_post, name='delete_post'),
    path('delete/confirmed/<int:id>/', views.delete, name='delete'),
    path('change/<int:id>/', views.change_post, name='change_post'),
]