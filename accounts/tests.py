from django.test import TestCase
from django.urls import reverse

from .models import CustomUser


class AccountPagesTests(TestCase):
    def test_signup_page_renders(self):
        response = self.client.get(reverse("signup"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "bootstrap@5.3.3")
        self.assertContains(response, "class=\"form-control\"")

    def test_short_signup_url_renders(self):
        response = self.client.get("/signup/")

        self.assertEqual(response.status_code, 200)

    def test_login_page_renders(self):
        response = self.client.get(reverse("login"))

        self.assertEqual(response.status_code, 200)

    def test_authenticated_user_is_redirected_from_login_page(self):
        user = CustomUser.objects.create_user(
            username="campusstudent",
            password="CampusConnect!2468",
        )
        self.client.force_login(user)

        response = self.client.get(reverse("login"))

        self.assertRedirects(response, reverse("dashboard"))

    def test_signup_creates_user_and_redirects_to_login(self):
        response = self.client.post(
            reverse("signup"),
            {
                "username": "campusstudent",
                "email": "student@example.com",
                "first_name": "Campus",
                "last_name": "Student",
                "role": CustomUser.Role.STUDENT,
                "course": "Computer Science",
                "password1": "CampusConnect!2468",
                "password2": "CampusConnect!2468",
            },
        )

        self.assertRedirects(response, reverse("login"))
        self.assertTrue(CustomUser.objects.filter(username="campusstudent").exists())

    def test_signup_shows_success_feedback_after_redirect(self):
        response = self.client.post(
            reverse("signup"),
            {
                "username": "newcampusstudent",
                "email": "newstudent@example.com",
                "role": CustomUser.Role.STUDENT,
                "password1": "CampusConnect!2468",
                "password2": "CampusConnect!2468",
            },
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Your account has been created successfully")

    def test_login_redirects_to_home(self):
        CustomUser.objects.create_user(
            username="campusstudent",
            password="CampusConnect!2468",
        )

        response = self.client.post(
            reverse("login"),
            {"username": "campusstudent", "password": "CampusConnect!2468"},
        )

        self.assertRedirects(response, reverse("dashboard"))
