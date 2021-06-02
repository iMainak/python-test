from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status
import importlib
import json
from datetime import  datetime
from django.apps import apps

class SourcesController(ViewSet):
    instance =None
    def __new__(cls):
        """
            __new__
        
            Creates a singleton object.
            ------------------------------------------------------
            @param object cls
            @return singleton object of class
        """
        if cls.instance is not None:
            return cls.instance
        else:
            inst = cls.instance = super(SourcesController, cls).__new__(cls)
            return inst
    def retunSerializerName(self, name):
        return {
            'sources':'SourcesSerializer'
        }[name]

    def getSerializerObject(self, name):
        module = importlib.import_module('return_status.serializers') 
        serializer = getattr(module, name)
        return serializer

    def saving_data(self, request):
        jsondata = {}
        now = datetime.now().strftime("%Y%m%d")
        print(now)
        for k, v in request.data.items():
            jsondata["id"] = now
            jsondata[k] = v
        serializer_name = self.retunSerializerName("sources")
        serializer_object = self.getSerializerObject(serializer_name)
        serializer = serializer_object(data=jsondata)
        if serializer.is_valid():
            print("yes")
            serializer.save()

        response = "successfully created"
        return Response(response, status= status.HTTP_200_OK)


    def retrive_data(self,request):
        return_dict = {}
        model_obj = apps.get_model("return_status", "sources")
        serializer_name = self.retunSerializerName("sources")
        serializer_object = self.getSerializerObject(serializer_name)
        _filter = {
            "status":"true"
        }
        data = model_obj.objects.filter(**_filter).values()
        return_dict["data"] = data
        return Response(return_dict, status= status.HTTP_200_OK)

