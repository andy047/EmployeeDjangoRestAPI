from django.conf.urls import url
from django.urls.conf import path

from Employee import views

urlpatterns = [
    #url(r'^department$',views.departmentApi),
    #url(r'^department/([0-9]+)'),
    path('department/<int:id>',views.departmentApi)

]
