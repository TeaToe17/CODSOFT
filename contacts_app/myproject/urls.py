"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from myapp import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.create_display_contacts, name='display_contacts'),
    path('update/<int:id>/', views.update_contact, name='update_contact'),
    path('delete/<int:id>/', views.delete_contact, name='delete_contact'),
    path('search/', views.search_contacts, name='search_contacts'),
]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',create_display_update_delete_search_contacts,name="home"),
#     path('update/<id>',create_display_update_delete_search_contacts,name="update_contact"),
#     path('delete/<id>',create_display_update_delete_search_contacts, {"delete":True} ,name="delete_contact"),
#     path('search/',create_display_update_delete_search_contacts,name="contact_search"),
# ]
