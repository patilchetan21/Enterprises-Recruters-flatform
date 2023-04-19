from django.urls import path
from resumeClassifier import views

urlpatterns = [
    path('resumeClf/', views.resumeList.as_view()),
    path('hiredCanditate/', views.hiredCanditateList.as_view()),
]
