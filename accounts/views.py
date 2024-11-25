from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import FormView, UpdateView
from django.views.generic import ListView
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views

from accounts.forms import RegisterForm , LoginForm , UserUpdateForm , ProfileUpdateForm
from blogs.models import Post

class RegisterView(FormView):
    template_name = 'accounts/register.html'
    form_class = RegisterForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('pages:home')
    
    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)
            
        return super(RegisterView, self).form_valid(form)



class ChangePasswordView(auth_views.PasswordChangeView):
    template_name = 'accounts/change_password.html'
    success_url = reverse_lazy('accounts:profile')



class foolsoulsLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('pages:home') 
    
    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))


class ChangePasswordView(auth_views.PasswordChangeView):
    template_name = 'accounts/changepassword.html'
    success_url = reverse_lazy('accounts:profile')



@login_required
def Profile(request, pk=None):
    if pk:
        post_owner = get_object_or_404(User, pk=pk)
        user_post = Post.objects.filter(author=pk)
        
    else:
        post_owner = request.user
        user_post = Post.objects.filter(author=request.user)
    
    context = {
        'post_owner':post_owner,
        'user_post':user_post
    }
    return render(request, 'accounts/profile.html',context)



@login_required
def ProfileUpdate(request):
    
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return reverse_lazy('accounts:profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    
    return render(request, 'accounts/updateprofile.html', context)


@login_required(login_url='accounts:login')
def logout_view(request):
    logout(request)
    return render(request, 'pages/home.html')
