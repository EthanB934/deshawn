from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from deshawnapi.models import Appointments, Walker

class AppointmentsView(ViewSet):
    def retrieve(self, request, pk=None):
        appointment = Appointments.objects.get(pk=pk)
        serialized = AppointmentsSerializer(appointment, many=False)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def list(self, request):
        appointments = Appointments.objects.all()
        serialized = AppointmentsSerializer(appointments, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def create(self, request):
    # Get the related walker from the database using the request body value
        client_walker_id = request.data["walkerId"]
        walker_instance = Walker.objects.get(pk=client_walker_id)

        # Create a new appointment instance
        appointment = Appointments()

        # Use walker instance as the value of the model property
        appointment.walker = walker_instance

        # Assign the appointment date using the request body value
        appointment.date = request.data["appointmentDate"]

        # Performs the INSERT statement into the deshawnapi_appointment table
        appointment.save()

        # Serialized the response to the client
        serialized = AppointmentsSerializer(appointment, many=False)

        # Respond with newly created appointment in JSON format with a 201 status code
        return Response(serialized.data, status=status.HTTP_201_CREATED)

# The serializer will be covered in the next chapter
class AppointmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointments
        fields = ("id", "walker", "date",)
