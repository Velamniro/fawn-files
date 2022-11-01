from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import *
from .models import *


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    list_display = ['username', 'gender', 'email', 'birth_date']

    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (
            'Custom fields',
            {
                'fields': (
                    'gender',
                    'birth_date',
                )
            }
        )
    )
    fieldsets = (
        *UserAdmin.add_fieldsets,
        (
            'Custom fields',
            {
                'fields': (
                    'gender',
                    'birth_date',
                    'avatar',
                )
            }
        )
    )

#
# @admin.register(Profile)
# class ProfileAdmin(UserAdmin):
#     model = Profile
#     form = ProfileChangeForm
#
#     list_display = ['pk']
#     fieldsets = (
#         *UserAdmin.add_fieldsets,
#         (
#             'Custom fields',
#             {
#                 'fields': (
#                     'avatar',
#                 )
#             }
#         )
#     )


admin.site.register(Profile)
