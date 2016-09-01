from rest_framework import generics
from ..models import Mark
from .serializers import MarkSerializer

class MarksListView(generics.ListCreateAPIView):
	queryset = Mark.objects.all()
	serializer_class = MarkSerializer

