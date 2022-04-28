from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from accounts.forms import SignUpForm
from accounts.models import User


class MyProfile(LoginRequiredMixin, UpdateView):
    # model = User
    queryset = User.objects.all()
    template_name = 'my_profile.html'
    success_url = reverse_lazy('index')
    fields = (
        'first_name',
        'last_name',
        'email',
        'avatar',
    )

    def get_object(self, queryset=None):
        return self.request.user

    # def get_queryset(self):
    #     queryset = User.objects.all()
    #     queryset = super().get_queryset()
    #     queryset = queryset.filter(id=self.request.user.id)
    #     return queryset


class SignUp(CreateView):
    queryset = User.objects.all()
    template_name = 'signup.html'
    success_url = reverse_lazy('index')
    form_class = SignUpForm


class ActivateUser(RedirectView):
    url = reverse_lazy('login')

    def get_redirect_url(self, username):
        user = get_object_or_404(User, username=username)

        if user.is_active:
            messages.error(self.request, 'Account is already activated!')
        else:
            user.is_active = True
            user.save(update_fields=['is_active'])
            messages.success(self.request, 'Account is activated!')

        return super().get_redirect_url()
