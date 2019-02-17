from taxi_auth.models import Role, User
from taxi_ride.models import Request
from django.db.models import Q, F
from taxi_auth.controller.user_controller import create_user
import datetime
import time

def create_request(data,user):
    if data.get('requested_by') is None:
        raise Exception('Requestor not found')
    requestor_id=data['requested_by']
    try:
         user=User.objects.get(id=requestor_id)
    except:
        user=create_user(requestor_id)
        requestor_id=user.id
    if user is None:
        raise Exception('Requestor not registered')
    data_dict={
        'status':'pending',
        'accepted_by':None,
        'requested_by':requestor_id
    }
    request=Request.objects.create(**data_dict)
    request.save()
    return requestor_id

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
          response_qs =request_qs
          for request in request_qs:
              now = datetime.datetime.now()
              created_at = request['created_at']
              request['created_at']=get_time_difference(now,created_at)-330 # time diff between mysql and django is 5.5hrs

    else:
        request_qs = Request.objects.filter(status=status,accepted_by=acceptor_id).values()
        response_qs=[]
        for request in request_qs:
            now = datetime.datetime.now()
            created_at = request['created_at']
            minutes = get_time_difference(now, created_at) - 330  # time diff between mysql and django is 5.5hrs
            request['created_at'] = minutes
            start_time = request['picked_up_at']
            time_elapsed = get_time_difference(now,start_time)
            request['picked_up_at'] = time_elapsed
            if request['status']=='ongoing':
                if time_elapsed>=5:
                     finish_request(request,request['request_id'],user)
                else:
                    response_qs.append(request)
            else:
                end_time = request['completed_at']
                time_elapsed = get_time_difference(now,end_time)
                request['completed_at']=time_elapsed
                response_qs.append(request)
    return response_qs

def get_all_requests(user):
    request_qs = Request.objects.filter().values()
    for request in request_qs:
        now = datetime.datetime.now()
        created_at = request['created_at']
        picked_up_at=request['picked_up_at']
        completed_at=request['completed_at']
        if picked_up_at is not None:
            request['picked_up_at']=get_time_difference(now,picked_up_at)
        if completed_at is not None:
            request['completed_at']=get_time_difference(now,completed_at)
        request['created_at'] =  get_time_difference(now, created_at) - 330
    return request_qs

def get_time_difference(t1,t2):
    t1=datetime.datetime.strftime(t1,"%Y-%m-%d %H:%M:%S")
    t2=datetime.datetime.strftime(t2,"%Y-%m-%d %H:%M:%S")
    dt1=datetime.datetime.strptime(t1,"%Y-%m-%d %H:%M:%S")
    dt2=datetime.datetime.strptime(t2,"%Y-%m-%d %H:%M:%S")
    duration = dt1 - dt2
    duration_in_s = duration.total_seconds()
    minutes = divmod(duration_in_s, 60)[0]
    return minutes
