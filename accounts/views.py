from django.shortcuts import render
from .forms import CustomUserCreationForm

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # ホームページにリダイレクト
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})  # フォームをテンプレートに渡す


def login_view(request):
    return render(request, 'accounts/login.html')
