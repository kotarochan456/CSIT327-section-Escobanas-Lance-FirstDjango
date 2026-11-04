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
        self.assertContains(response, "Welcome, campusstudent!")


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
                self.assertContains(response, "Admin Panel")
