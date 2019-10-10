"""NotesProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.HomePage.as_view(),name='home'),
    url(r'login/$',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    url(r'logout/$',auth_views.LogoutView.as_view(),name='logout'),
    url(r'^test/$',views.TestPage.as_view(),name='test'),
    url(r'^thanks/$',views.ThanksPage.as_view(),name='thanks'),
    url(r'^signup/$',views.SignUp.as_view(),name='signup'),
    #
    url(r'^allNotes$',views.NoteList.as_view(),name='all'),
    url(r'new/$',views.CreateNote.as_view(),name='create'),
    url(r'by(?P<username>[-\w]+)',views.UserNotes.as_view(),name='for_user'),
    url(r'by(?P<username>[-\w]+)/(?P<pk>\d+)/$',views.NoteDetail.as_view(),name='single'),
    url(r'delete/(?P<pk>\d+)/$',views.DeleteNote.as_view(),name='delete'),
]
