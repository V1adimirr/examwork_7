from django.urls import path

from Interview.views.poll_views import IndexPollView, DetailPollView

urlpatterns = [
    path('', IndexPollView.as_view(), name='polls_view'),
    path('polls/<int:pk>/detail/', DetailPollView.as_view(), name='detail_polls_view'),
]
