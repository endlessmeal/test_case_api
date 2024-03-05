from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee, PointOfSale, Visit
from .serializers import PointOfSaleSerializer, VisitSerializer
from django.utils import timezone


@api_view(['GET'])
def get_points_of_sale(request):
    """
    Retrieve a list of Point of Sale objects associated with the provided phone number of an employee.

    Parameters:
    - phone_number (string): The phone number of the employee.

    Returns:
    - 200 OK: Returns a list of Point of Sale objects with their IDs and names.
    - 400 BAD REQUEST: If the phone_number parameter is not provided.
    - 404 NOT FOUND: If no employee is found with the provided phone number.
    """
    if request.method == 'GET':
        phone_number = request.GET.get('phone_number')
        if phone_number:
            phone_number = f"+{phone_number}"
            try:
                employee = Employee.objects.get(phone_number=phone_number)
                print(employee)
                points_of_sale = PointOfSale.objects.filter(employee=employee)
                serializer = PointOfSaleSerializer(points_of_sale, many=True)
                return Response(serializer.data)
            except Employee.DoesNotExist:
                return Response({'error': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'Phone number not provided'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def perform_visit(request):
    """
    Create a new visit to a Point of Sale with the provided information.

    Parameters:
    - phone_number (string): The phone number of the employee.
    - point_of_sale_pk (integer): The primary key of the Point of Sale.
    - latitude (float): The latitude of the visit location.
    - longitude (float): The longitude of the visit location.

    Returns:
    - 201 CREATED: Returns the primary key and datetime of the created visit.
    - 400 BAD REQUEST: If any required parameter is not provided or if data is invalid.
    - 403 FORBIDDEN: If the employee does not belong to the specified Point of Sale.
    - 404 NOT FOUND: If employee or Point of Sale is not found.
    """
    if request.method == 'POST':
        phone_number = request.data.get('phone_number')
        serializer = VisitSerializer(data=request.data)
        if serializer.is_valid():
            point_of_sale = serializer.validated_data.get('point_of_sale')
            latitude = serializer.validated_data.get('latitude')
            longitude = serializer.validated_data.get('longitude')
            try:
                employee = Employee.objects.get(phone_number=phone_number)
                point_of_sale = PointOfSale.objects.get(pk=point_of_sale.id)
                if point_of_sale.employee == employee:
                    visit = Visit.objects.create(
                        datetime=timezone.now(),
                        point_of_sale=point_of_sale,
                        latitude=latitude,
                        longitude=longitude
                    )
                    response_data = {'pk': visit.pk, 'datetime': visit.datetime}
                    return Response(response_data, status=status.HTTP_201_CREATED)
                else:
                    return Response({'error': 'Employee does not belong to this point of sale'}, status=status.HTTP_403_FORBIDDEN)
            except Employee.DoesNotExist:
                return Response({'error': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)
            except PointOfSale.DoesNotExist:
                return Response({'error': 'Point of sale not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
