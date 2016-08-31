from rest_framework import generics
from ..models import Mark
from .serializers import MarkSerializer

class MarksListView(generics.ListAPIView):
	queryset = Mark.objects.all()
	serializer_class = MarkSerializer