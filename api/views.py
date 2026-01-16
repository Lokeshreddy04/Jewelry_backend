from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


# --------------------------
# PRODUCTS API
# --------------------------

@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()

    search = request.GET.get('search')
    if search:
        products = products.filter(name__icontains=search) | products.filter(description__icontains=search)

@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()

    # Filters
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    base_metal = request.GET.get('metal')
    sort = request.GET.get('sort')

    # Filters
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    base_metal = request.GET.get('metal')
    sort = request.GET.get('sort')

    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)
    if base_metal:
        products = products.filter(base_metal__iexact=base_metal)

    # Sorting
    if sort == "price_low":
        products = products.order_by("price")
    elif sort == "price_high":
        products = products.order_by("-price")
    elif sort == "latest":
        products = products.order_by("-id")
    elif sort == "popularity":
        products = products.order_by("-rating")

    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_product(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=404)

    serializer = ProductSerializer(product)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_product(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=404)

    serializer = ProductSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_product(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=404)

    product.delete()
    return Response({"message": "Product deleted"})


# --------------------------
# CATEGORY API
# --------------------------

@api_view(['GET'])
def get_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_products_by_category(request, id):
    products = Product.objects.filter(category_id=id)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
