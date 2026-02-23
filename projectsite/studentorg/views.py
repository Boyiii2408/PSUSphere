from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from studentorg.models import Organization
from studentorg.forms import OrganizationForm
from django.urls import reverse_lazy
from .models import College, Program, Student, OrgMember, Organization

paginate_by = 5

class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = "org_confirm_delete.html"
    success_url = reverse_lazy('organization-list')

class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = "org_form.html"
    success_url = reverse_lazy('organization-list')




class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = "org_form.html"
    success_url = reverse_lazy('organization-list')

class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = "home.html"


class OrganizationListView(ListView):
    model = Organization
    context_object_name = 'organizations'
    template_name = "org_list.html"
    paginate_by = 5


class CollegeListView(ListView):
    model = College
    paginate_by = 5

class CollegeCreateView(CreateView):
    model = College
    fields = "__all__"
    success_url = reverse_lazy("college-list")

class CollegeUpdateView(UpdateView):
    model = College
    fields = "__all__"
    success_url = reverse_lazy("college-list")

class CollegeDeleteView(DeleteView):
    model = College
    success_url = reverse_lazy("college-list")


class ProgramListView(ListView):
    model = Program
    paginate_by = 5

class ProgramCreateView(CreateView):
    model = Program
    fields = "__all__"
    success_url = reverse_lazy("program-list")

class ProgramUpdateView(UpdateView):
    model = Program
    fields = "__all__"
    success_url = reverse_lazy("program-list")

class ProgramDeleteView(DeleteView):
    model = Program
    success_url = reverse_lazy("program-list")


class StudentListView(ListView):
    model = Student
    paginate_by = 5

class StudentCreateView(CreateView):
    model = Student
    fields = "__all__"
    success_url = reverse_lazy("student-list")

class StudentUpdateView(UpdateView):
    model = Student
    fields = "__all__"
    success_url = reverse_lazy("student-list")

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy("student-list")

class OrgMemberListView(ListView):
    model = OrgMember
    paginate_by = 5

class OrgMemberCreateView(CreateView):
    model = OrgMember
    fields = "__all__"
    success_url = reverse_lazy("orgmember-list")

class OrgMemberUpdateView(UpdateView):
    model = OrgMember
    fields = "__all__"
    success_url = reverse_lazy("orgmember-list")

class OrgMemberDeleteView(DeleteView):
    model = OrgMember
    success_url = reverse_lazy("orgmember-list")

