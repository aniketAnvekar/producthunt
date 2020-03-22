from . import views
from django.urls import path, include

urlpatterns = [
    path('create',views.create,name='create'),
    path('<int:job_id>',views.detail,name='detail'),
    path('<int:product_id>/upvote', views.upvote, name='upvote'),
]    
