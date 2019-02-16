from django.contrib import admin, messages
from django.utils.text import slugify
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Group, Permission

from taxi_auth.models import Role

class PBRoleAdmin(GroupAdmin):

    def get_exclude(self, request, obj):
        if obj is not None: # Edit form
            exclude = ('soft_delete', 'created_by', 'updated_by')
        else: # Add form
            exclude = ('soft_delete', 'created_by', 'updated_by')
        return exclude

    def save_model(self, request, obj, form, change):
        obj.name = obj.role_name
        if change: # Edit form
            obj.updated_by = request.user
        else: # Add form
            obj.created_by = request.user
            obj.updated_by = request.user

        super(PBRoleAdmin, self).save_model(request, obj, form, change)

    def get_queryset(self, request):
        qs = super(PBRoleAdmin, self).get_queryset(request)
        return qs


    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     from oems_examination.models import Client
    #     if not request.user.is_superuser:  # Not PB superuser
    #         if db_field.name == 'client':
    #             client = request.user.client
    #             kwargs['queryset'] = Client.objects.filter(client_id=client.client_id)
    #     return super(PBRoleAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    list_display = ('role_name','role_name')
    fields = ('role_name', 'permissions')

admin.site.unregister(Group)
admin.site.register(Role, PBRoleAdmin)

