from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate, login

from account.models import Account



class RegisterView(View):
    def get(self, request):
        return render(request, 'account/register.html')

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('password2')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('account:register')

        try:
            account = Account.objects.create_user(username=username, email=email, password=password)
            account.save()
            messages.success(request, 'Registratsiya muvaffaqiyatli bajarildi!')
            return redirect(reverse('account:login'))
        except Exception as e:
            messages.error(request, f'XATOLIK: {str(e)}')
            return redirect('account:register')


class LoginView(View):
    def get(self, request):
        return render(request, "account/login.html")

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('chat:home')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('account:login')
class ProfileView(View):
    def get(self, request, username):
        account = Account.objects.get(username=username)
        context = {
            "account": account
        }
        return render(request, "account/profile.html", context=context)


class FollowView(LoginRequiredMixin, View):
    def get(self, request, username):
        account = request.user
        user = Account.objects.get(username=username)
        type = request.GET.get('type')
        if type == "follow":
            account.following.add(user)
            messages.success(request, "You are successfully followed")
        elif type == "unfollow":
            account.following.remove(user)
            messages.success(request, "You are successfully unfollowed")
        else:
            messages.error(request, "Bad credentials")

        return redirect("account:profile", username=username)
