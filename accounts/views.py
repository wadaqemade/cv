from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from accounts.forms import NewCv
from django.shortcuts import redirect
from .models import Cv


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def home(request):
    all_info = Cv.objects.all()
    if request.method == 'POST':
        all_info = Cv.objects.filter(full_name__icontains=request.POST['search'],city__icontains=request.POST['city'],specialization__icontains=request.POST['specialization'])
            
    context = {
        'info' : all_info
    }
    return render(request, 'home.html', context)

def mycv(request):
    all_info = Cv.objects.filter(user=request.user)
    context = {
        'info' : all_info
    }
    return render(request, 'mycv.html', context)

def info(request):
    if request.method == 'POST':
        info_cv = NewCv(request.POST)
        if info_cv.is_valid():
            info_cv1 = info_cv.save(commit=False)
            info_cv1.user = request.user
            info_cv1.save()
            return redirect('home')
    else:
        info_cv = NewCv
    context = {
        'form': info_cv
    }

    return render(request, 'cv.html', context)