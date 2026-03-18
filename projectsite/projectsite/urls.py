from django.contrib import admin
from django.urls import path
from studentorg.views import (
    HomePageView,
    OrganizationListView,
    ProgramListView,
    StudentListView,
    OrgMemberListView,

    OrganizationCreateView,
    OrganizationUpdateView,
    OrganizationDeleteView,

    ProgramCreateView,
    ProgramUpdateView,
    ProgramDeleteView,

    StudentCreateView,
    StudentUpdateView,
    StudentDeleteView,

    OrgMemberCreateView,
    OrgMemberUpdateView,
    OrgMemberDeleteView,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', HomePageView.as_view(), name='home'),


    path('organization/', OrganizationListView.as_view(), name='organization-list'),
    path('organization/add/', OrganizationCreateView.as_view(), name='organization-add'),
    path('organization/<int:pk>/edit/', OrganizationUpdateView.as_view(), name='organization-update'),
    path('organization/<int:pk>/delete/', OrganizationDeleteView.as_view(), name='organization-delete'),

 
    path('program/', ProgramListView.as_view(), name='program-list'),
    path('program/add/', ProgramCreateView.as_view(), name='program-add'),
    path('program/<int:pk>/edit/', ProgramUpdateView.as_view(), name='program-update'),
    path('program/<int:pk>/delete/', ProgramDeleteView.as_view(), name='program-delete'),

    path('student/', StudentListView.as_view(), name='student-list'),
    path('student/add/', StudentCreateView.as_view(), name='student-add'),
    path('student/<int:pk>/edit/', StudentUpdateView.as_view(), name='student-update'),
    path('student/<int:pk>/delete/', StudentDeleteView.as_view(), name='student-delete'),


    path('orgmember/', OrgMemberListView.as_view(), name='orgmember-list'),
    path('orgmember/add/', OrgMemberCreateView.as_view(), name='orgmember-add'),
    path('orgmember/<int:pk>/edit/', OrgMemberUpdateView.as_view(), name='orgmember-update'),
    path('orgmember/<int:pk>/delete/', OrgMemberDeleteView.as_view(), name='orgmember-delete'),
]