from django.http import JsonResponse
from recipes.models import Category, Tags, Reciepes
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from recipes.api.serializers import CategorySerializer, TagsSerializer, RecipesSerializer, RecipeCreatSerializer

def categories(request):
    category_list = Category.objects.all()

    # data = []
    # for category in category_list:
    #     data.append(
    #         {
    #         'id': category.id,
    #         'name': category.name,
    #         }
    #         )
    # return JsonResponse(data, safe=False)

    serializer = CategorySerializer(category_list, many=True)
    return JsonResponse(serializer.data, safe=False)


def tags(request):
    tags_list = Tags.objects.all()

    serializer = TagsSerializer(tags_list, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET','POST'])
def recipes(request):
    recipes_list = Reciepes.objects.all()
    if request.method == 'POST':
        serializer = RecipeCreatSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False, status=201)
        return JsonResponse(serializer.errors, safe=False, status=403)
   
    serializer = RecipesSerializer(recipes_list, many=True, context = {'request':request})
    return JsonResponse(serializer.data, safe=False, status=200)


class RecipeListCreateApiView(ListCreateAPIView):
    serializer_class = RecipesSerializer
    queryset = Reciepes.objects.all()
    allowed_methods = ['GET', 'POST']

    # def get_serializer_class(self):
    #     if self.request.method == 'POST':
    #         self.serializer_class = RecipeCreatSerializer

    #     return self.serializer_class

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return RecipeCreatSerializer
        return RecipesSerializer


@api_view(['PUT','PATCH'])
def recipes_update(request, pk):
    recipes = Reciepes.objects.get(id=pk)

    if request.method == 'PUT':
        serializer = RecipeCreatSerializer(data = request.data, instance=recipes)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False, status=201)
        return JsonResponse(serializer.errors, safe=False, status=403)
    
    elif request.method == 'PATCH':
        serializer = RecipeCreatSerializer(data = request.data, instance=recipes, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False, status=201)
        return JsonResponse(serializer.errors, safe=False, status=403)
   
    return JsonResponse(serializer.data, safe=False, status=200)

class RecipeRetrieveUpdateView(RetrieveUpdateDestroyAPIView):
    serializer_class = RecipeCreatSerializer
    queryset = Reciepes.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]