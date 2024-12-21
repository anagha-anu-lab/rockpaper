from django.urls import path
from.import views

urlpatterns = [
    path('',views.display,name="display"),
    path('result/',views.result,name="result"),
    path('again/',views.again,name="again")
]
