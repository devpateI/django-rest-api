from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):


    # This code is for serializers
    # title = serializers.CharField(max_length=100)
    # author = serializers.CharField(max_length=100)
    # email = serializers.EmailField(max_length=100)
    # date = serializers.DateField()

    # def create(self,validate_data):
    #     return Article.objects.create(validate_data)

    # def update(self,instance,validate_data):
    #     instance.title = validate_data.get('title',instance.title)
    #     instance.author = validate_data.get('author',instance.author)
    #     instance.email = validate_data.get('email',instance.email)
    #     instance.date = validate_data.get('date',instance.date)
    #     instance.save()
    #     return instance
    
    class Meta:
        model = Article
        fields = ['id','title','author','discription']
