from django.urls import path
from . import views
app_name = 'polls'
urlpatterns = [

    path('', views.index, name="index"),
    #127.0.0.1/polls

    path('<int:question_id>/', views.detail, name="detail"),
    #127.0.0.1/polls/6
    path('<int:question_id>/result', views.result, name="result"),
    #127.0.0.1/polls/6/result
    path('<int:question_id>/vote', views.vote, name="vote"),
    #127.0.0.1/polls/6/vote

    path('fun/', views.fun, name="fun"),
    #127.0.0.1/polls/fun
]
