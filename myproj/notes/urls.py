from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.PostList.as_view(), name='list'),
    path('detail/<int:pk>/', views.PostDetail.as_view(), name='detail'),
    path('create/', views.CreateNote.as_view(), name='create'),
    path('delete/<int:pk>/', views.DeleteNote.as_view(), name='delete'),
    path('update/<int:pk>/', views.UpdateNote.as_view(), name='update'),
]
