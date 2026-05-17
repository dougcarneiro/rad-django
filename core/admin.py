from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    
    # O email já está no fieldsets padrão (formulário de edição).
    # Precisamos adicioná-lo apenas no add_fieldsets (formulário de criação).
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('email',)}),
    )

admin.site.register(User, CustomUserAdmin)
