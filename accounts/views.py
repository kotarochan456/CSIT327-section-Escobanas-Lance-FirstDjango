from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, UpdateView
from .forms import CustomUserCreationForm, ProfileForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def form_valid(self, form):
        messages.success(
            self.request,
            "Your account has been created successfully. You can now log in.",
        )
        return super().form_valid(form)


class ProfileUpdateView(
    LoginRequiredMixin, SuccessMessageMixin, UpdateView
):
    form_class = ProfileForm
    template_name = "accounts/profile.html"
    success_url = reverse_lazy("profile")
    success_message = "Your profile has been updated."

    def get_object(self, queryset=None):
        return self.request.user