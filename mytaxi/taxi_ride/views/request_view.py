from rest_framework.views import APIView
from rest_framework import status
from django.db import transaction
from rest_framework.response import Response
from taxi_ride.controller.ride_controller import create_request,accept_request,finish_request
from taxi_auth.auth import IsAuth


class RequestView(APIView):
    permission_classes = (IsAuth,)

    def post(self,request):
        user = request.user
        with transaction.atomic():
            try:
                create_request(request.data, request.user)
                return Response({'message': 'Request created successfully!'})
            except Exception as e:
                print(e)
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class RequestRetrieveView(APIView):
    def put(self,request,request_id):
        user = request.user
        with transaction.atomic():
            try:
                accept_request(request.data,request_id,request.user)
                return Response({'message': 'Request accepted successfully!'})
            except Exception as e:
                print(e)
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class RequestCompleteView(APIView):
    def put(self, request, request_id):
        user = request.user
        with transaction.atomic():
            try:
                finish_request(request.data,request_id,request.user)
                return Response({'message': 'Request completed successfully!'})
            except Exception as e:
                print(e)
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)