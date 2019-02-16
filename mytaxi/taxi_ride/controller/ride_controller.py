from taxi_auth.models import Role, User
from taxi_ride.models import Request
from django.db.models import Q, F
import datetime



def create_request(data,user):
    if data.get('requested_by') is None:
        raise Exception('Requestor not found')
    requestor_id=data['requested_by']
    user=User.objects.get(id=requestor_id)
    if user is None:
        raise Exception('Requestor not registered')
    data_dict={
        'status':'pending',
        'accepted_by':None,
        'requested_by':data['requested_by']
    }
    request=Request.objects.create(**data_dict)
    request.save()
    return request

def accept_request(data,request_id,user):
    if data.get('acceptor') is None:
        raise Exception('Acceptor not found')
    acceptor_id = data['acceptor']
    user = User.objects.get(id=acceptor_id)
    if user is None:
        raise Exception('Requestor not registered')
    if request_id is None:
        raise Exception('Request Id not found')
    ongoing_request_qs = Request.objects.filter(status='ongoing', accepted_by=acceptor_id).values()
    if len(ongoing_request_qs) > 0:
        raise Exception('Requestor can have only one ongoing request')
    request=Request.objects.get(request_id=request_id)
    if request is None:
        raise Exception('Invalid request id')
    if request.status !='pending':
        raise Exception('Request already assigned. Please refresh'+request.status)
    request.status='ongoing'
    request.accepted_by=acceptor_id
    now = datetime.datetime.now()
    request.picked_up_at=now
    request.save()
    return request

def finish_request(data,request_id,user):
    if request_id is None:
        raise Exception('Request Id not found')
    request = Request.objects.get(request_id=request_id)
    if request is None:
        raise Exception('Invalid request id')
    if request.status != 'ongoing':
        raise Exception('Only ongoing requests can be cancelled')
    request.status = 'finished'
    now = datetime.datetime.now()
    request.completed_at = now
    request.save()
    return request

def get_available_requests(data,acceptor_id,user):
    if data.get('status') is None:
        raise Exception('Status not specified')
    status=data['status']
    if status == "pending":
          request_qs=Request.objects.filter(status='pending').values()
    else:
        request_qs = Request.objects.filter(status=status,accepted_by=acceptor_id).values()
    return request_qs

def get_all_requests(user):
    request_qs = Request.objects.filter().values()
    return request_qs

