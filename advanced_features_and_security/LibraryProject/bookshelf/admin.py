from django.contrib import admin
from .models import Book, CustomUser
from django.contrib.auth.admin import UserAdmin

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('author', 'publication_year')
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username','email','first_name','last_name','is_staff','date_of_birth']
    fieldsets=(
        (None,{'fields':('username','password')}),
        ('Personal info',{'fields':('first_name','last_name','email','date_of_birth','profile_photo')}),
        ('Permissions',{'fields':('is_active','is_staff','is_superuser','groups','user_permissions')}),
        ('Important dates',{'fields':('last_login','date_joined')}),
    )
    add_fieldsets = (
        (None,{
            'classes':('wide',),
            'fields':('username','email','first_name','last_name','date_of_birth','profile_photo','password1','password2','is_staff','is_active')}
            ),
    )
    search_fields = ('email','username')
    ordering =('email',)
admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Book,BookAdmin)

# Register your models here.



