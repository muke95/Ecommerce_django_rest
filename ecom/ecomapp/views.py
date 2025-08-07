from django.shortcuts import render
from django.http import HttpResponse ,JsonResponse
from . import models
from rest_framework.decorators import api_view , permission_classes,authentication_classes
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import products , Cart
from .serializers import productsSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializers import UserSignupSerializer , CartSerializer
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication ,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny



def paginate(items, page_size, page_number):
    start_index = (page_number - 1) * page_size
    end_index = start_index + page_size
    return items[start_index:end_index]

# # Example usage
# # Example: a list of numbers from 1 to 100
# all_items = list(range(1, 101))  

# page_size = 10  # Number of items per page
# page_number = 1  # Page number to retrieve

# current_page = paginate(all_items, page_size, page_number)
# print(f"Page {page_number}: {current_page}")

def response(request):
    return render(request, 'my_template.html') 

@api_view(['GET'])
# @permission_classes([IsAuthenticated])  # Remove this line if you want public access
def get_product(request):
    try:
        limit = int(request.GET.get('limit', 1000))
        page = int(request.GET.get('page', 1))

        if limit <= 0 or page <= 0:
            return JsonResponse({"error": "Limit and page must be greater than 0"}, status=400)

        offset = (page - 1) * limit

        product_queryset = models.products.objects.all()[offset:offset + limit]
        total_products = models.products.objects.count()

        product_list = list(product_queryset.values())

        return JsonResponse({
            "data": product_list,
            "total": total_products,
            "page_number": page,
            "page_size": limit
        }, safe=False)

    except ValueError:
        return JsonResponse({"error": "Limit and page must be integers"}, status=400)



# @api_view(['GET'])
# # @permission_classes([IsAuthenticated])
# def get_product(request):
#     paginator = PageNumberPagination()
#     paginator.page_size = request.GET.get('limit', 1000)  # default 1000
#     queryset = products.objects.all()
    
#     result_page = paginator.paginate_queryset(queryset, request)
#     serializer = productsSerializer(result_page, many=True)
    
#     return paginator.get_paginated_response(serializer.data)


# Signup API
@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    serializer = UserSignupSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=201)
    return Response(serializer.errors, status=400)

# Login API
@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    return Response({'error': 'Invalid credentials'}, status=401)

# Logout API
@api_view(['POST'])
def logout(request):
    request.user.auth_token.delete()
    return Response({'message': 'Logged out successfully'}, status=200)




@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication,TokenAuthentication])
@permission_classes([IsAuthenticated])  # Allow unauthenticated GET, restrict POST
def cart_view(request):
    user = request.user if request.user.is_authenticated else None
    
    # Ensure session exists
    session_id = request.session.session_key
    if not session_id:
        request.session.save()
        session_id = request.session.session_key

    if request.method == 'GET':
        cart_items = Cart.objects.filter(user=user) if user else Cart.objects.filter(session_id=session_id)
        serializer = CartSerializer(cart_items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        if not user:
            return Response({'error': 'Authentication required to add items to cart.'},
                            status=status.HTTP_401_UNAUTHORIZED)

        product_id = request.data.get('product')
        quantity = request.data.get('quantity')

        if not product_id or not quantity:
            return Response({'error': 'Both product and quantity are required.'},
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            product = products.objects.get(id=product_id)
        except products.DoesNotExist:
            return Response({'error': 'Product not found.'},
                            status=status.HTTP_404_NOT_FOUND)

        cart_item, created = Cart.objects.get_or_create(
            user=user,
            product=product,
            defaults={'quantity': quantity}
        )

        if not created:
            cart_item.quantity += int(quantity)
            cart_item.save()

        serializer = CartSerializer(cart_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        