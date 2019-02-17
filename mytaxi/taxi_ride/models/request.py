from django.db import models
from django.conf import settings

class Request(models.Model):
    request_id=models.AutoField(primary_key=True)
    requested_by=models.IntegerField(null=True,blank=True,default=None)
    accepted_by=models.IntegerField(null=True,blank=True,default=None)
    # requested_by=models.ForeignKey(settings.AUTH_USER_MODEL.id,
    #                                db_column='requested_by',
    #                                related_name='ride_requested_by',
    #                                on_delete=models.SET_NULL, null=True, blank=True)
    # accepted_by=models.ForeignKey(settings.AUTH_USER_MODEL.id,
    #                               db_column='accepted_by',
    #                               related_name='ride_accepted_by',
    #                               on_delete=models.SET_NULL, null=True, blank=True
    #                               )
    status=models.CharField(max_length=255,default='pending')
    latitude=models.IntegerField()
    longitude=models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    picked_up_at=models.DateTimeField(null=True,blank=True,default=None)
    completed_at=models.DateTimeField(null=True,blank=True,default=None)

    def __str__(self):
        return self.request_id

    class Meta:
        db_table = 'request'
        verbose_name_plural = 'Requests'



