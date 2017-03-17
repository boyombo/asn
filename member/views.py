from django.shortcuts import redirect, render
from django.contrib import messages

from member.forms import MemberForm


def home(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for registering')
            return redirect('home')
    else:
        form = MemberForm()
    return render(request, 'home.html', {'form': form})
