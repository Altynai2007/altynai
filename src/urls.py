"""
URL configuration for src project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from announcement.api import (
    MentorView,
    AnnouncementRetrieveView,
    AnnouncementUpdateView,
    AnnouncementDeleteView,
    AnnouncementCreateView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('announcements/', MentorView.as_view()),
    path('announcements/<int:pk>/', AnnouncementRetrieveView.as_view()),
    path('announcements-update/<int:pk>/', AnnouncementUpdateView.as_view()),
    path('announcements-delete/<int:pk>/', AnnouncementDeleteView.as_view()),
    path('announcements-create/', AnnouncementCreateView.as_view()),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)