"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from studentorg.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('organization_list', OrganizationListView.as_view(), name='organization-list'),
    path('organization_list/add', OrganizationCreateView.as_view(), name='organization-add'),
    path('organization_list/<pk>',OrganizationUpdateView.as_view(), name='organization-update'),
    path('organization_list/<pk>/delete', OrganizationDeleteView.as_view(), name='organization-delete'),
    # College
path("college/", CollegeListView.as_view(), name="college-list"),
path("college/add/", CollegeCreateView.as_view(), name="college-add"),
path("college/<int:pk>/edit/", CollegeUpdateView.as_view(), name="college-edit"),
path("college/<int:pk>/delete/", CollegeDeleteView.as_view(), name="college-delete"),

# Program
path("program/", ProgramListView.as_view(), name="program-list"),
path("program/add/", ProgramCreateView.as_view(), name="program-add"),
path("program/<int:pk>/edit/", ProgramUpdateView.as_view(), name="program-edit"),
path("program/<int:pk>/delete/", ProgramDeleteView.as_view(), name="program-delete"),

# Student
path("student/", StudentListView.as_view(), name="student-list"),
path("student/add/", StudentCreateView.as_view(), name="student-add"),
path("student/<int:pk>/edit/", StudentUpdateView.as_view(), name="student-edit"),
path("student/<int:pk>/delete/", StudentDeleteView.as_view(), name="student-delete"),

# OrgMember
path("orgmember/", OrgMemberListView.as_view(), name="orgmember-list"),
path("orgmember/add/", OrgMemberCreateView.as_view(), name="orgmember-add"),
path("orgmember/<int:pk>/edit/", OrgMemberUpdateView.as_view(), name="orgmember-edit"),
path("orgmember/<int:pk>/delete/", OrgMemberDeleteView.as_view(), name="orgmember-delete"),

]