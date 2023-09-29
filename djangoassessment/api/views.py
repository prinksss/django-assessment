from django.shortcuts import render
from rest_framework import generics, status,permissions
from rest_framework.authtoken.models import Token
from .models import Invoice, InvoiceDetail
from rest_framework.response import Response
from .serializers import InvoiceSerializer, UserRegistrationSerializer
from rest_framework.permissions import IsAuthenticated
class UserRegistrationView(generics.CreateAPIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            # Create a token for the newly registered user
            user = serializer.instance
            token, created = Token.objects.get_or_create(user=user)

            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class InvoiceListView(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = (IsAuthenticated,)

class InvoiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InvoiceDetail.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = [permissions.IsAuthenticated,]

    
