from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('indexht/', views.indexht, name='indexht'),
    path('indexhtml/', views.indexnew, name='indexhtml'),
    path('<str:question_id>/', views.detail, name='detail'),
    path('<str:question_id>/results/', views.results, name='results'),
    path('<str:question_id>/vote/', views.vote, name='vote'),
]