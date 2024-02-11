from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CustomUser

def set_name(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        request.user.name = name
        request.user.save()
        return redirect('name_page', name=name)
    return render(request, 'first_login.html')

def all(request):
    c = CustomUser.objects.all()
    return render(request, 'all.html', {'H':c})


@login_required
def name_page(request, name):
    users = CustomUser.objects.all()
    return render(request, 'user_data_change.html', {'users': users})

@login_required
def change_data(request, user_id):
    user = CustomUser.objects.get(pk=user_id)
    if request.method == 'POST':
        user.name = request.POST.get('name')
        user.save()
        return redirect('all')
    return render(request, 'user_data_change.html', {'user': user})

def createuser(request):
    if(request.method == 'POST'):
        data = request.POST
        name = data['name']
        CustomUser.objects.create(name=name)
        return redirect('all')
    return render(request, 'add.html')


def deleteUser(request, user_id):
    user = CustomUser.objects.get(pk=user_id)
    user.delete()
    return redirect('all')