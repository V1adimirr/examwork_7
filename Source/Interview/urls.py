from django.urls import path

from Interview.views.poll_views import IndexPollView, DetailPollView, CreatePollView, UpdatePollView, DeletePollView

urlpatterns = [
    path('', IndexPollView.as_view(), name='polls_view'),
    path('polls/<int:pk>/detail/', DetailPollView.as_view(), name='detail_polls_view'),
    path('polls/create/', CreatePollView.as_view(), name='create_poll'),
    path('polls/<int:pk>/update/', UpdatePollView.as_view(), name='update_poll'),
    path('polls/<int:pk>/delete/', DeletePollView.as_view(), name='delete_poll'),
]
