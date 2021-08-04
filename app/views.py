from django.shortcuts import render
from rest_framework import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category,Product
from .serializers import *

# Create your views here.

class CategoryView(APIView):

    def get(self,request):
        query_set = Category.objects.all()
        serializer = CategorySerializer(query_set,many=True)
        return Response(serializer.data)
        

    def post(self,request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self,request):# put means update
        id = request.POST.get('id')
        category = request.POST.get('category')
        try:
            query_set =Category.objects.get(id=id)
            if query_set:
                query_set.category = category
                query_set.save()
                res = {
                    'success' : 'true',
                    'message' : 'Category has been successfully updated'
                }
                return Response(res, status=status.HTTP_201_CREATED)
        except:
            res = {
                    'success' : 'false',
                    'message' : 'Something went wrong'

                }
            return Response(res,status=status.HTTP_304_NOT_MODIFIED)


    def delete(self,request):
        id = request.POST.get("id")
        try:
            query_set = Category.objects.get(id=id).delete()
            if query_set:
                res = {
                    'success' : 'true',
                    'message' : 'Category has been successfully deleted'

                }
                return Response(res, status=status.HTTP_200_OK)
        except:
            res = {
                    'success' : 'false',
                    'message' : 'Record does not exist'
            }
            return Response(res, status=status.HTTP_400_BAD_REQUEST)


    
class ProductView(APIView):
    #Retrieve Product    
    def get(self, request):
        qs = Product.objects.all()
        ser = ProductSerializer(qs, many=True)
        return Response(ser.data)

    #Create Product
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #Update Product
    def put(self, request):
        id = request.POST.get("id")       
        product_name = request.POST.get("product_name")
        product_model_name = request.POST.get("product_model_name")
        price = request.POST.get("price")    
        try: 
            qs = Product.objects.get(id=id)
            if qs:
                qs.product_name = product_name
                qs.product_model_name = product_model_name
                qs.price = price
                qs.save()
                resp = {
                    'success' : 'true',
                    'message' : "Product Has Been Successfully Updated",
                }
                return Response(resp, status=status.HTTP_201_CREATED)
        except:
            resp = {
                'success' : 'false',
                'message' : "Something went wrong try again",      
                }    
            return Response(resp, status=status.HTTP_304_NOT_MODIFIED) 

    #Delete Product
    def delete(self, request):
        id = request.POST.get("id")  
        try:           
            qs = Product.objects.get(id=id).delete()
            if qs:
                resp = {
                    'success' : 'true',
                    'message' : "Product Deleted",
                }
                return Response(resp, status=status.HTTP_200_OK)
        except:
            resp = {
                'success' : 'false',
                'message' : "Record does not exist",        }    
            return Response(resp, status=status.HTTP_400_BAD_REQUEST)
