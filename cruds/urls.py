from django.contrib import admin
from task import views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('create',views.create_form,name="create_f"),
    path('update/<int:id>',views.update_form,name="update_f"),
]
