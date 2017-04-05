from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.get_tasks, name="get_tasks"),
    url(r'^add$', views.add_task, name="add_task"),
    url(r'^change-state', views.change_state_task, name="change_state"),
]