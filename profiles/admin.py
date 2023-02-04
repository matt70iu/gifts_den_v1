from django.contrib import admin
from .models import ContactUsForm


class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'subject',
        'message'
    )


admin.site.register(ContactUsForm, ContactAdmin)
