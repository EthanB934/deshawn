from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from deshawnapi.views import WalkerView, CityView, DogView, AppointmentsView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'walkers', WalkerView, 'walk')
router.register(r'cities', CityView, 'city')
router.register(r'dogs', DogView, 'dog')
router.register(r'appointments', AppointmentsView, 'appointment')
# The first argument is the routing path
# The second argument is the view that will handle client requests
# The third argument is needed for the registration process of the URL

urlpatterns = [
    path('', include(router.urls)),
]
