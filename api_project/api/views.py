from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Book
from .serializers import BookSerializer
# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    """
    Authentication and permission behavior:
    - Uses global TokenAuthentication from settings.py.
    - Read actions (list/retrieve) require any authenticated user.
    - Write actions (create/update/partial_update/destroy) require admin user.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        # Action-based permissions keep read access broader than write access.
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
