# Django
from django.contrib.auth.forms import UserChangeForm as UserChangeFormBase
from django.contrib.auth.forms import UserCreationForm as UserCreationFormBase
from django.forms import ModelForm

# Local
from .models import Brother
from .models import User


class BrotherForm(ModelForm):
    class Meta:
        model = Brother
        fields = [
            'name',
            'email',
            'phone',
        ]

    def clean_email(self):
        data = self.cleaned_data['email']
        return data.lower()

    def clean_name(self):
        data = self.cleaned_data['name']
        return data.title()


class UserCreationForm(UserCreationFormBase):
    """
    Custom user creation form for Auth0
    """

    # Bypass password requirement
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].required = False
        self.fields['password2'].required = False

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_unusable_password()
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = [
            'username',
        ]


class UserChangeForm(UserChangeFormBase):
    """
    Custom user change form for Auth0
    """

    class Meta:
        model = User
        fields = [
            'username',
        ]
