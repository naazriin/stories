from rest_framework import serializers

from recipes.models import Category, Tags, Reciepes



class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name', 'created_at', 'updated_at']



class TagsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tags
        fields = ['id', 'name', 'created_at', 'updated_at']


class CategoryRecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']



class RecipesSerializer(serializers.ModelSerializer):
    
    # category = serializers.CharField(source = 'category.name')
    category = CategoryRecipeSerializer()
    tags = TagsSerializer(many=True)
    # author = serializers.CharField(source='authors.username')

    class Meta:
        model = Reciepes
        fields = ['id', 'title', 'description', 'image', 'category', 'tags', 'author_fullname']
                  

class RecipeCreatSerializer(serializers.ModelSerializer):
    author = serializers.CharField(read_only=True)
    class Meta:
        model = Reciepes
        fields = ['id', 'title', 'description', 'image', 'category', 'tags', 'author']
                  
    def validate(self, attrs):
        context = self.context['request']
        attrs['authors'] = context.user
        return attrs