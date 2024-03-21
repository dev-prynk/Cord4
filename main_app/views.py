from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import Event_Serializer, EventOrganiser_Serializer, EventCategory_Serializer
from .models import event_table, EventCategory, EventOrganiser
from rest_framework.permissions import IsAuthenticated
from .custom_auth import Custom_Authentication
from .filters import eventfilterset
# Create your views here.

class eventview(viewsets.ViewSet):
    

    def get_authenticators(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [Custom_Authentication()]
        return super().get_authenticators()
    
    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated()]
        return super().get_permissions()
    
    def list(self, request):
        try:
            events = event_table.objects.all()
            event_filter = eventfilterset(request.GET, queryset=events)
            queryset = event_filter.qs
            serializer = Event_Serializer(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def create(self, request):
        try:
            serializer = Event_Serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
    def retrieve(self, request, pk=None):
        try:
            event = event_table.objects.get(id=pk)
            serializer = Event_Serializer(event)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response({"error": "Event does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def update(self, request, pk=None):
        try:
            event = event_table.objects.get(id=pk)
            serializer = Event_Serializer(event, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response({"error": "Event does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def partial_update(self, request, pk=None):  
        try:

            event = event_table.objects.get(id=pk)
            serializer = Event_Serializer(event, data=request.data, partial=True)  
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response({"error": "Event does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def destroy(self, request, pk=None):
        try:
            event = event_table.objects.get(id=pk)
            event.delete()
            return Response({"msg": "Deleted"})
        except ObjectDoesNotExist:
            return Response({"error": "Event does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class eventcategoryview(viewsets.ViewSet):

    def get_authenticators(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [Custom_Authentication()]
        return super().get_authenticators()
    
    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated()]
        return super().get_permissions()
    

    def list(self, request):

        try:
            categories = EventCategory.objects.all()
            serializer = EventCategory_Serializer(categories, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def create(self, request):
        try:
            serializer = EventCategory_Serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def retrieve(self, request, pk=None):
        try:
            category = EventCategory.objects.get(id=pk)
            serializer = EventCategory_Serializer(category)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response({"error": "Event does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def update(self, request, pk=None):
        try:
            category = EventCategory.objects.get(id=pk)
            serializer = EventCategory_Serializer(category, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response({"error": "Event does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def partial_update(self, request, pk=None):
        try:
            category = EventCategory.objects.get(id=pk)
            serializer = EventCategory_Serializer(category, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response({"error": "Event does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def destroy(self, request, pk=None):
        try:
            category = EventCategory.objects.get(id=pk)
            category.delete()
            return Response({"msg": "Deleted"})
        except ObjectDoesNotExist:
            return Response({"error": "Event does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
class eventorganiserview(viewsets.ViewSet):

    def get_authenticators(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [Custom_Authentication()]
        return super().get_authenticators()
    
    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated()]
        return super().get_permissions()
    
    def list(self, request):
        organisers = EventOrganiser.objects.all()
        serializer = EventOrganiser_Serializer(organisers, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = EventOrganiser_Serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        try:
            organiser = EventOrganiser.objects.get(id=pk)
            serializer = EventOrganiser_Serializer(organiser)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response({"error": "Event does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def update(self, request, pk=None):
        try:
            organiser = EventOrganiser.objects.get(id=pk)
            serializer = EventOrganiser_Serializer(organiser, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response({"error": "Event does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def partial_update(self, request, pk=None):
        try:
            organiser = EventOrganiser.objects.get(id=pk)
            serializer = EventOrganiser_Serializer(organiser, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response({"error": "Event does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    
    def destroy(self, request, pk=None):
        try:
            organiser = EventOrganiser.objects.get(id=pk)
            organiser.delete()
            return Response({"msg": "Deleted"})
        except ObjectDoesNotExist:
            return Response({"error": "Event does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
