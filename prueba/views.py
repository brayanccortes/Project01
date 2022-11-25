from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from prueba.controller import AdminPersonasController

# Create your views here.

class AdminPersonaView(APIView):
    def get(self, request):
        try:
            persona = AdminPersonasController.get_all()
            return Response(persona)

        except Exception as e:
            Response({'mensaje': f'Ha ocurrido un error! {e}'}, status= status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, format = None):
        try:
            persona = AdminPersonasController.save_persona(request.data)
            if hasattr(persona,"errors") and persona.errors:
                return Response(persona.errors,status= status.HTTP_400_BAD_REQUEST)
            return Response(persona.data, status= status.HTTP_201_CREATED)

        except Exception as e:
            Response({'mensaje': f'Ha ocurrido un error! {e}'}, status= status.HTTP_500_INTERNAL_SERVER_ERROR)

class AdminPersonaViewDetail(APIView):

    def get(self, resquest, pk):
        try:
            persona = AdminPersonasController.get_all()
            return Response(persona)

        except Exception as e:
            return Response({'mensaje': f'Ha ocurrido un error! {e}'}, status= status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            persona = AdminPersonasController.update_persona(request.data, pk)
            if hasattr(persona,"errors") and persona.errors:
                return Response(persona.errors,status= status.HTTP_400_BAD_REQUEST)
            return Response(data={'mensaje': 'La persona ha sido actualizada!'}, status= status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'mensaje': f'Ha ocurrido un error! {e}'}, status= status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, resquest, pk):
        try:
            persona = AdminPersonasController.delete_persona(pk)
            return Response(data={'mensaje': 'La persona ha sido eliminada'}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'mensaje': f'Ha ocurrido un error! {e}'}, status= status.HTTP_500_INTERNAL_SERVER_ERROR)