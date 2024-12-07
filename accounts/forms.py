from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    """
    ユーザー登録用フォーム
    """
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'bio')  # 必要なフィールドを指定

class CustomUserChangeForm(UserChangeForm):
    """
    ユーザー情報編集用フォーム
    """
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'bio')  # 必要なフィールドを指定
