from django.urls import path
from core import views

urlpatterns = [
    path("", views.index, name="index"),
    path("tickets", views.ticket_list, name="ticket_list"),
    path("tickets/new", views.ticket_create, name="ticket_create"),
    path("tickets/<int:ticket_id>", views.ticket_detail, name="ticket_detail"),
]
