from django.contrib import admin
from .models import Registration, ContactMessage



@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('name', 'email', 'message', 'created_at')

    def has_add_permission(self, request):
        # Disallow adding messages manually
        return False


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'agreed_to_terms')
    list_filter = ('agreed_to_terms',)
    search_fields = ('full_name', 'email', 'interests')
    readonly_fields = ('full_name', 'email', 'interests', 'agreed_to_terms')

    fieldsets = (
        ('User Info', {
            'fields': ('full_name', 'email')
        }),
        ('Details', {
            'fields': ('interests', 'agreed_to_terms')
        }),
    )
