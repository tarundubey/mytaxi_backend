from taxi_auth.models import Role, User
from django.db.models import Q, F

def create_user(user_id):
    try:
        role = Role.objects.get(role_name='customer')
    except Role.DoesNotExist:
        raise Exception('Invalid Role Name')

    data_dict = {
        'username': 'customer'+str(user_id),
        'first_name': 'customer',
        'last_name':'customer last name',
        'email': 'test@test.com',
        'mobile': 1234
    }

    user = User.objects.create(**data_dict)
    user.groups.add(role)
    user.set_password('customer'+str(user_id)+'@')
    user.save()
    return user

