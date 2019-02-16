from django.urls import path
from taxi_ride.views import RequestView,RequestRetrieveView,RequestCompleteView,DashboardView,AdminDashboardView
urlpatterns = [
    path('request/', RequestView.as_view()),
    path('request/<int:request_id>/accept/',RequestRetrieveView.as_view()),
    path('request/<int:request_id>/complete/',RequestCompleteView.as_view()),
    path('dashboard/<int:acceptor_id>/',DashboardView.as_view()),
    path('dashboard/',AdminDashboardView.as_view())
]