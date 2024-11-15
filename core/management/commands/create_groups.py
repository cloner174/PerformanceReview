
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

class Command(BaseCommand):
    
    help = 'Create user groups for roles'
    def handle(self, *args, **kwargs):
        roles = ['Senior Manager', 'Manager', 'Employee']
        for role in roles:
            Group.objects.get_or_create(name=role)
        self.stdout.write(self.style.SUCCESS('Successfully created groups'))
    

#cloner174