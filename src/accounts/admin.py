from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from accounts.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """ Какие поля отображаются на странице списка для изменения из интерфейса администратора """
    list_display = ('username', 'email', 'first_name', 'last_name', 'get_groups')
    """ Поиск по полям """
    search_fields = ('email', 'first_name', 'last_name', 'username',)
    """ Делает все поля доступными только для чтения """
    readonly_fields = ('last_login', 'date_joined')
    """ Автоматически добавит фильтр этого поля на стороне администратора """
    list_filter = ('is_staff', 'is_active', 'is_superuser',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permission', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Groups', {'fields': ('groups', 'user_permissions')}),
        ('Impotent dates', {'fields': ('last_login', 'date_joined')})
    )

    def get_groups(self, obj):
        return ", ".join([group.name for group in obj.groups.all()])

    get_groups.short_description = 'Groups'
