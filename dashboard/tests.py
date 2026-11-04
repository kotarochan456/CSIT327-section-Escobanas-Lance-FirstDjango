from django.test import TestCase
from django.urls import reverse

from accounts.models import CustomUser


class HomePageTests(TestCase):
    def test_home_page_renders(self):
        user = CustomUser.objects.create_user(
            username="campusstudent",
            password="CampusConnect!2468",
        )
        self.client.force_login(user)

        response = self.client.get(reverse("dashboard"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome, campusstudent")


class AdminPanelTests(TestCase):
    def test_admin_panel_routes_render_for_admin(self):
        admin_user = CustomUser.objects.create_user(
            username="campusadmin",
            password="CampusConnect!2468",
            role=CustomUser.Role.ADMIN,
        )
        self.client.force_login(admin_user)

        for url in (reverse("admin_panel"), reverse("dashboard_admin_panel")):
            with self.subTest(url=url):
                response = self.client.get(url)

                self.assertEqual(response.status_code, 200)
                self.assertContains(response, "Admin panel")
                self.assertContains(response, "Registered members")


class ProfilePageTests(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username="campusstudent",
            password="CampusConnect!2468",
            first_name="Campus",
            last_name="Student",
            email="student@example.com",
            course="Computer Science",
        )

    def test_profile_requires_login(self):
        response = self.client.get(reverse("profile"))

        self.assertRedirects(
            response,
            f"{reverse('login')}?next={reverse('profile')}",
        )

    def test_user_can_view_and_update_own_profile(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("profile"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Your profile")
        self.assertContains(response, "Computer Science")

        response = self.client.post(
            reverse("profile"),
            {
                "first_name": "Updated",
                "last_name": "Student",
                "email": "updated@example.com",
                "course": "Information Technology",
            },
            follow=True,
        )

        self.user.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.user.first_name, "Updated")
        self.assertEqual(self.user.email, "updated@example.com")
        self.assertEqual(self.user.course, "Information Technology")
        self.assertContains(response, "Your profile has been updated.")
