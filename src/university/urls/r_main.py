from django.urls import re_path, include


app_name: str = "university"


urlpatterns = [
    re_path(r"academic-years", include("university.urls.r_academic_year", namespace="academic_years")),
    re_path(r"intake-classes", include("university.urls.r_intake_class", namespace="intake_classes"))
]
