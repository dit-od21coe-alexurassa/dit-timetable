from django.test import TestCase

from .models import AcademicYear


class AcademicYearModelTests(TestCase):

    def setUp(self) -> None:
        self.acYear = AcademicYear.objects.create(name="2023/24")

    def testName(self):
        self.assertEqual(self.acYear.name, '2023/24', "Name is not correctly added")
