from django.contrib import admin
from portfolio_contact.models import ContactUS


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'subject', 'is_read']
    # list_filter = ['is_read']
    # list_editable = ['is_read']
    # search_fields = ['subject', 'text']

    class Meta:
        model = ContactUS


admin.site.register(ContactUS, ContactUsAdmin)
