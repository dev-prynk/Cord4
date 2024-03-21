from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import eventview, eventcategoryview, eventorganiserview

router = routers.DefaultRouter()
router.register('event', eventview, basename="event")

router.register('eventcategory', eventcategoryview, basename="eventcategory")

router.register('eventorganiser', eventorganiserview, basename="eventorganiser")

urlpatterns = [
    path('', include(router.urls)),
]
