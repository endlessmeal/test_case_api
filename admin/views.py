from rest_framework import viewsets
from app.models import Employee, PointOfSale, Visit
from .serializers import EmployeeSerializer, PointOfSaleSerializer, VisitSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for CRUD operations on Employee objects.

    list:
    Retrieve a list of all Employee objects.

    create:
    Create a new Employee object.

    retrieve:
    Retrieve the details of a specific Employee object.

    update:
    Update an existing Employee object.

    destroy:
    Delete an existing Employee object.

    search:
    Search for Employee objects by name.

    Parameters:
    - name (string): The name of the employee to search for.

    Returns:
    - 200 OK: Returns a list of Employee objects matching the search query.
    - 404 NOT FOUND: If no Employee objects match the search query.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    search_fields = ['name']


class PointOfSaleViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for CRUD operations on Point of Sale objects.

    list:
    Retrieve a list of all Point of Sale objects.

    create:
    Create a new Point of Sale object.

    retrieve:
    Retrieve the details of a specific Point of Sale object.

    update:
    Update an existing Point of Sale object.

    destroy:
    Delete an existing Point of Sale object.

    search:
    Search for Point of Sale objects by name.

    Parameters:
    - name (string): The name of the point of sale to search for.

    Returns:
    - 200 OK: Returns a list of Point of Sale objects matching the search query.
    - 404 NOT FOUND: If no Point of Sale objects match the search query.
    """
    queryset = PointOfSale.objects.all()
    serializer_class = PointOfSaleSerializer
    search_fields = ['name']


class VisitViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for CRUD operations on Visit objects.

    list:
    Retrieve a list of all Visit objects.

    create:
    Create a new Visit object.

    retrieve:
    Retrieve the details of a specific Visit object.

    update:
    Update an existing Visit object.

    destroy:
    Delete an existing Visit object.

    search:
    Search for Visit objects by employee name or point of sale name.

    Parameters:
    - employee_name (string): The name of the employee to search for visits.
    - point_of_sale_name (string): The name of the point of sale to search for visits.

    Returns:
    - 200 OK: Returns a list of Visit objects matching the search query.
    - 404 NOT FOUND: If no Visit objects match the search query.
    """
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer
    search_fields = ['employee__name', 'point_of_sale__name']
