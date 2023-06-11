from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Cafes
from .serializers import Serialize
import os
from dotenv import load_dotenv

load_dotenv()


@api_view(['GET'])
def all_cafes(request):
    return Response(Serialize(Cafes.objects.all(), many = True).data)


@api_view(['GET'])
def random_cafe(request):
    return Response(Serialize(Cafes.objects.order_by('?').first()).data)


@api_view(['GET'])
def cafe_by_location(request):
    return Response(Serialize(Cafes.objects.filter(location = request.GET.get('location')), many = True).data)


@api_view(['DELETE', 'GET'])
def delete_cafe(request):
    try:
        if request.GET.get('api_key') == os.getenv('API_KEY'):
            Cafes.objects.get(id = request.GET.get('cafe_id')).delete()
            return Response({'Success': 'The cafe was deleted successfully'})
        return Response({'Error': 'Enter a valid api key'})
    except:
        return Response({'Error': 'There is no cafe with that id in our database'})
    
    
@api_view(['PATCH', 'GET'])
def update_price(request):
    try:
        cafe = Cafes.objects.get(id = request.GET.get('cafe_id'))
        cafe.coffee_price = f"£{request.GET.get('new_price')}"
        cafe.save()
        return Response({'Success': 'The coffee price was updated successfully'})
    except:
        return Response({'Error': 'There is no cafe with that id in our database'})
    
    
@api_view(['GET', 'POST'])
def add_cafe(request):
    if request.method == 'POST':
        try:
            Cafes.objects.get(name = request.POST.get('name'), location = request.POST.get('location'))
            return Response({'Error': 'The cafe already exists in our database'})
        except:
            Cafes.objects.create(
                name = request.POST['name'],
                map_url = request.POST.get('map_url'),
                img_url = request.POST.get('img_url'),
                location = request.POST.get('location'),
                has_sockets = request.POST.get('has_sockets'),
                has_toilet = request.POST.get('has_toilet'),
                has_wifi = request.POST.get('has_wifi'),
                can_take_calls = request.POST.get('can_take_calls'),
                seats = request.POST.get('seats'),
                coffee_price = request.POST.get('coffee_price'),
            )
            return Response({'Success': 'The cafe was added successfully'})
        
