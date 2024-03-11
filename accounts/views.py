from django.shortcuts import render
from rest_framework.views import APIView

from accounts.serializer import AccountSerializer
from .models import *
from .serializer import *
from rest_framework.response import Response

# Create your views here.

class AccountView(APIView):
    def get(self, request):
        output = [{'id': output.id, 'username': output.username, 'email': output.email, 'password': output.password, 'created_at': output.created_at, 'updated_at': output.updated_at} for output in Account.objects.all()]
        return Response(output)

    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)