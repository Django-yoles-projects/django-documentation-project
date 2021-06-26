from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

    path('f', views.index_f, name="index_f"),
    path('long/', views.index_long, name="index_long"),
    path('no-template/', views.index_no_template, name="index_no_template"),
    # ex: /polls/5/
    path('f/<int:question_id>/', views.detail_f, name="detail_f"),
    path('f/<int:question_id>/results', views.results_f, name="results_f"),
]
