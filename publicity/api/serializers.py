from rest_framework import serializers
from ..models import Mark

class MarkSerializer(serializers.ModelSerializer):
	class Meta:
		model = Mark
		fields = ('id','name','description','image','visits','slug')

# class MarkSerializer(serializers.Serializer):
# 	pk  = serializers.IntegerField(read_only=True)
# 	name = serializers.CharField(max_length=50)
# 	#description = serializers.TextField()
# 	#image= serializers.ImageField(upload_to='imageMarks')
# 	visits = serializers.IntegerField(required=False)
# 	slug = serializers.SlugField(max_length=140)

# 	def create(self, validate_data):
# 		return Mark.objects.create(**validated_dat)

# 	def update(self, instance, validate_data):
# 		instance.name = validate_data.get('name', instance.name)
# 		#instance.description = validate_data.get('description', instance.description)
# 		#instance.image = validate_data.get('image',instance.image)
# 		instance.visits = validate_data.get('visits',instance.visits)
# 		instance.save()
# 		return instance
		
		



