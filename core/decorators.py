#
from django.contrib.auth.decorators import user_passes_test


def group_required(group_name):
    """Requires user membership in at least one of the groups passed in."""
    def in_groups(u):
        if u.is_authenticated:
            if u.groups.filter(name=group_name).exists() or u.is_superuser:
                return True
        return False
    
    return user_passes_test(in_groups)

#cloner174