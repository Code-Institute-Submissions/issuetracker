from django.db import models
from django.utils import timezone
        

class Ticket(models.Model):
    """
    A single Ticket
    """
    title = models.CharField(max_length=200)
    issue = models.CharField(max_length=1000)
    reported_by = models.CharField(max_length=50, blank=False)
    reported_on = models.DateTimeField(default=timezone.now, editable = True)
    choice_priority = (
        ('HIGH', 'HIGH'),
        ('MEDIUM', 'MEDIUM'),
        ('LOW', 'LOW'),
    )
    priority = models.CharField(max_length=10, choices=choice_priority, default='LOW')
    assigned_to = models.CharField(max_length=50, blank=True, null=True)
    choice_status = (
        ('TO_DO', 'TO_DO'),
        ('DOING', 'DOING'),
        ('DONE', 'DONE'),
    )
    status = models.CharField(max_length=10, choices=choice_status, default='TO_DO')
    resolution = models.CharField(max_length=400, blank =True, null = True)
    verified = models.BooleanField(default=False)
    notes = models.CharField(max_length=400, blank =True, null = True)
    views = models.IntegerField(default=0)
    profile_user=models.CharField(max_length=50, blank=True)
    
    def __unicode__(self):
        return "{0}-{1}-{2}".format(self.id, self.title, self.reported_by)
        
