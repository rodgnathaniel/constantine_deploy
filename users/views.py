from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .forms import UserRegisterForm


def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}!')
            return redirect(reverse('login'))
    else:
        form = UserRegisterForm()
    return render(request, 'users/registration.html', {'form': form})

# messages.debug
# messages.info
# messages.success
# messages.warning
# messages.error