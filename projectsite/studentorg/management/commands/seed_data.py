from django.core.management.base import BaseCommand
from faker import Faker
import random
from datetime import date

from studentorg.models import (
    College,
    Program,
    Organization,
    Student,
    OrgMember
)

fake = Faker()


class Command(BaseCommand):
    help = "Seed database with fake data"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING("Seeding database with fake data..."))


        OrgMember.objects.all().delete()
        Student.objects.all().delete()
        Organization.objects.all().delete()
        Program.objects.all().delete()
        College.objects.all().delete()

        colleges = []
        for _ in range(5):
            college = College.objects.create(
                college_name=fake.company()
            )
            colleges.append(college)


        programs = []
        for _ in range(10):
            program = Program.objects.create(
                prog_name=fake.job(),
                college=random.choice(colleges)
            )
            programs.append(program)


        organizations = []
        for _ in range(8):
            org = Organization.objects.create(
                name=fake.company(),
                college=random.choice(colleges),
                description=fake.sentence(nb_words=10)
            )
            organizations.append(org)

        students = []
        for _ in range(30):
            student = Student.objects.create(
                student_id=fake.unique.bothify(text="20##-#####"),
                lastname=fake.last_name(),
                firstname=fake.first_name(),
                middlename=fake.first_name() if random.choice([True, False]) else None,
                program=random.choice(programs)
            )
            students.append(student)


        for _ in range(40):
            OrgMember.objects.create(
                student=random.choice(students),
                organization=random.choice(organizations),
                date_joined=fake.date_between(start_date="-2y", end_date="today")
            )

        self.stdout.write(self.style.SUCCESS("✅ Fake data successfully added!"))