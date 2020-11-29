# # Django
# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UserAdminBase
# from django.urls import reverse
from django.utils.safestring import mark_safe

# Local
# # Local
from .forms import UserChangeForm
from .forms import UserCreationForm
from .models import User


@admin.register(User)
class UserAdmin(UserAdminBase):
    save_on_top = True
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    fieldsets = (
        (None, {
            'fields': [
                'name',
                'email',
                'username',
            ]
        }
        ),
        ('Permissions', {'fields': ('is_admin', 'is_active')}),
    )
    list_display = [
        'name',
        'created',
        'last_login'
    ]
    list_filter = [
        'is_active',
        'is_admin',
        'created',
        'last_login',
    ]
    search_fields = [
        'name',
        'email',
        'username',
    ]
    ordering = [
        '-created',
    ]
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': [
                'name',
                'email',
                'username',
                'is_admin',
                'is_active',
            ]
        }
        ),
    )
    filter_horizontal = ()
    inlines = [
    ]

    def email_link(self, obj):
        return mark_safe(
            '<a href="mailto:{0}">{0}</a>'.format(
                obj.email,
            )
        )
    email_link.short_description = 'email'
