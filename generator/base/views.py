from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from.forms import *
from django.contrib.auth import login
from django.views.generic.edit import FormView,CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/login')
def home(request):
    return render(request,'base/home.html')

class RegisterPage(FormView):
    template_name = 'registration/sign_up.html'
    form_class = RegisterForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')
    

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('/home')
        return super(RegisterPage, self).get(*args, **kwargs)

