from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q

from .models import Organization, Program, Student, OrgMember


class HomePageView(ListView):
    model = Organization
    template_name = "studentorg/home.html"
    context_object_name = "home"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_students"] = Student.objects.count()
        context["total_organizations"] = Organization.objects.count()
        context["total_programs"] = Program.objects.count()
        return context


class OrganizationListView(ListView):
    model = Organization
    template_name = "studentorg/org_list.html"
    context_object_name = "organizations"
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get("q")

        if query:
            qs = qs.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query)
            )
        return qs


class ProgramListView(ListView):
    model = Program
    template_name = "studentorg/program_list.html"
    context_object_name = "program"
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        query = self.request.GET.get("q")

        if query:
            qs = qs.filter(
                Q(prog_name__icontains=query) |
                Q(college__college_name__icontains=query)
            )
        return qs


class StudentListView(ListView):
    model = Student
    template_name = "studentorg/student_list.html"
    context_object_name = "students"
    paginate_by = 5


class OrgMemberListView(ListView):
    model = OrgMember
    template_name = "studentorg/orgmember_list.html"
    context_object_name = "members"
    paginate_by = 5


class OrganizationCreateView(CreateView):
    model = Organization
    fields = "__all__"
    template_name = "studentorg/form.html"
    success_url = reverse_lazy("organization-list")


class OrganizationUpdateView(UpdateView):
    model = Organization
    fields = "__all__"
    template_name = "studentorg/form.html"
    success_url = reverse_lazy("organization-list")


class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = "studentorg/confirm_delete.html"
    success_url = reverse_lazy("organization-list")



class ProgramCreateView(CreateView):
    model = Program
    fields = "__all__"
    template_name = "studentorg/form.html"
    success_url = reverse_lazy("program-list")


class ProgramUpdateView(UpdateView):
    model = Program
    fields = "__all__"
    template_name = "studentorg/form.html"
    success_url = reverse_lazy("program-list")


class ProgramDeleteView(DeleteView):
    model = Program
    template_name = "studentorg/confirm_delete.html"
    success_url = reverse_lazy("program-list")


class StudentCreateView(CreateView):
    model = Student
    fields = "__all__"
    template_name = "studentorg/form.html"
    success_url = reverse_lazy("student-list")


class StudentUpdateView(UpdateView):
    model = Student
    fields = "__all__"
    template_name = "studentorg/form.html"
    success_url = reverse_lazy("student-list")


class StudentDeleteView(DeleteView):
    model = Student
    template_name = "studentorg/confirm_delete.html"
    success_url = reverse_lazy("student-list")



class OrgMemberCreateView(CreateView):
    model = OrgMember
    fields = "__all__"
    template_name = "studentorg/form.html"
    success_url = reverse_lazy("orgmember-list")


class OrgMemberUpdateView(UpdateView):
    model = OrgMember
    fields = "__all__"
    template_name = "studentorg/form.html"
    success_url = reverse_lazy("orgmember-list")


class OrgMemberDeleteView(DeleteView):
    model = OrgMember
    template_name = "studentorg/confirm_delete.html"
    success_url = reverse_lazy("orgmember-list")