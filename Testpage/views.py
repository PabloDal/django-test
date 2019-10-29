from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import UserProfile
from django.http import HttpResponse


def index(request):
    return render(request, 'Testpage/index.html')


def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_reg = UserProfile()
            new_reg.Name = request.POST.get("Name")
            new_reg.Mail = request.POST.get("Mail")
            new_reg.save()
            return redirect('Testpage:index')
        else:
            return HttpResponse('errors')
    else:
        form = RegisterForm()

    return render(request, 'Testpage/form.html', {'form': form})


def show_users(request):
    users = UserProfile.objects.all()[:10]

    return render(request, 'Testpage/show.html', {'users': users})