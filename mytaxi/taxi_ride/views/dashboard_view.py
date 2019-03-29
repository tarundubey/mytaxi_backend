from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from rest_framework.views import APIView
from rest_framework import status
from django.db import transaction
from rest_framework.response import Response
from taxi_ride.controller.ride_controller import create_request,accept_request,finish_request,get_available_requests,get_all_requests
from taxi_auth.auth import IsAuth
from oauth2_provider.views.generic import ProtectedResourceView
from django.contrib.auth.decorators import login_required



class DashboardView(APIView):
    permission_classes = (IsAuth,TokenHasReadWriteScope)
    def post(self,request,acceptor_id):
        user = request.user
        print(user)
        with transaction.atomic():

            try:
                response = get_available_requests(request.data, acceptor_id, request.user)
                return Response(response,user)
            except Exception as e:
                print(e)
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AdminDashboardView(APIView,ProtectedResourceView):
    permission_classes = (IsAuth,TokenHasReadWriteScope)
    def post(self,request):
        user = request.user
        with transaction.atomic():
            try:
                response=get_all_requests(request.user)
                return Response(response)
            except Exception as e:
                print(e)
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
