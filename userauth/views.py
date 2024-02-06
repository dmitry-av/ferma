from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from userauth.forms import ProfileEditForm
from userauth.models import User


@login_required
def profile(request):
    return render(request, "userauth/profile.html", {"page_group": "profile"})


@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, "userauth/userlist.html", {"page_group": "user_list", "users": users})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileEditForm(instance=request.user)
    return render(request, 'userauth/edit_profile.html', {'form': form})
