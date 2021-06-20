from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('long/', views.index_long, name="index_long"),
    path('no-template/', views.index_no_template, name="index_no_template"),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name="detail"),
    path('<int:question_id>/results', views.results, name="results"),
    path('<int:question_id>/vote', views.vote, name="vote"),
]
