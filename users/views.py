from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView

from .forms import UserRegisterForm

class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('catalog:product_list')


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('')