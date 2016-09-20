# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# from rest_framework.decorators import api_view
# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

from ..models import Mark
from .serializers import MarkSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

class MarkList(generics.ListCreateAPIView):
	queryset = Mark.objects.all()
	serializer_class = MarkSerializer
	permission_classes = (IsAuthenticated,)

class MarkDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Mark.objects.all()
	serializer_class = MarkSerializer
	permission_classes = (IsAuthenticated,)


# class MarkList(APIView):
# 	"""
# 	List all marks, or create  a new mark.
# 	"""
# 	def get (self, request, format=None):
# 		marks = Mark.objects.all()
# 		serializer = MarkSerializer(marks, many=True)
# 		return Response(serializer.data)

# 	def post(self, request, fromat=None):
# 		serializer = MarkSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class MarkDetail(APIView):
# 	"""
# 	Retrieve, update or delete a mark instance.
# 	"""
# 	def get_object(self, pk):
# 		try:
# 			return Mark.objects.get(pk=pk)
# 		except Mark.DoesNotExist:
# 			raise Http404

# 	def get(self, request, pk, format=None):
# 		mark = self.get_object(pk)
# 		serializer = MarkSerializer(mark)
# 		return Response(serializer.data)

# 	def put(self, request, pk, format=None):
# 		mark = self.get_object(pk)
# 		serializer = MarkSerializer(mark, data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			return Response(serializer.data)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 	def delete(self, request, pk, format=None):
# 		mark = self.get_object(pk)
# 		mark.delete()
# 		return Response(status=status.HTTP_204_NO_CONTENT)





# class JSONResponse(HttpResponse):
# 	"""
# 	An HttpResponse that renders  its content into JSON.
# 	"""
# 	def __init__(self, data, **kwargs):
# 		content = JSONRenderer().render(data)
# 		kwargs['content_type'] = 'application/json'
# 		super(JSONResponse, self).__init__(content, **kwargs)

# # @csrf_exempt
# @api_view(['GET','POST'])
# def mark_list(request, format=None):
# 	"""
# 	List all names marks, or create a new Mark.
# 	"""
# 	if request.method == 'GET':
# 		marks = Mark.objects.all()
# 		serializer = MarkSerializer(marks, many=True)
# 		return Response(serializer.data)
# 		# return JSONResponse(serializer.data)

# 	elif request.method == 'POST':
# 		# data = JSONParser().parse(request)
# 		# serializer = MarkSerializer(data=data)
# 		serializer = MarkSerializer(data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			# return JSONResponse(serializer.data, status=201)
# 			return Response(serializer.data, status=status.HTTP_201_CREATED)
# 		# return JSONResponse(serializer.errors, status=400)
# 		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # @csrf_exempt
# @api_view(['GET', 'PUT', 'DELETE'])
# def mark_detail(request, pk, format=None):
# 	"""
# 	Retrieve, update or delete a name mark
# 	"""
# 	try:
# 		mark = Mark.objects.get(pk=pk)
# 	except Mark.DoesNotExist:
# 		# return HttpResponse(status=404)
# 		return Response(status=status.HTTP_404_NOT_FOUND)

# 	if request.method == 'GET':
# 		serializer =  MarkSerializer(mark)
# 		# return JSONResponse(serializer.data)
# 		return Response(serializer.data)

# 	elif request.method == 'PUT':
# 		# data = JSONParser().parse(request)
# 		# serializer = MarkSerializer(mark, data=data)
# 		serializer = MarkSerializer(mark, data=request.data)
# 		if serializer.is_valid():
# 			serializer.save()
# 			# return JSONResponse(serializer.data)
# 			return Response(serializer.data)
# 		# return JSONResponse(serializer.erros, status=404)
# 		return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)

# 	elif request.method == 'DELETE':
# 		mark.delete()
# 		# return HttpResponse(status=204)
# 		return Response(status=status.HTTP_204_NO_CONTENT)


# class MarksListView(generics.ListCreateAPIView):
# 	queryset = Mark.objects.all()
# 	serializer_class = MarkSerializer

