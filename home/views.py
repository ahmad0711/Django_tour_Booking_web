from django.http import response
from django.shortcuts import render, HttpResponse
from rest_framework import serializers, viewsets
from .models import Form
from django.contrib import messages
from choclaty.serializers import FormSerializer
from rest_framework.renderers import JSONRenderer

# Create your views here.
def index(request):
    return render(request, 'index.html')    
    # return HttpResponse("This is Chocolaty page")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is About page")

def contact(request):
    return render(request, 'contact.html')
    # return HttpResponse("This is Contact page")

def services(request):
    return render(request, 'services.html')
    # return HttpResponse("This is Services page")

def form(request):
    if request.method == "POST":
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        city = request.POST.get('city')
        form = Form (name=name, mobile=mobile, email=email, city=city)
        form.save()
        messages.success(request, 'Your Form Has Been Submitted successfully')
    return render(request, 'booking_form.html')


class Formvieweset(viewsets.ModelViewSet):
    queryset = Form.objects.all()
    Serializer_class = FormSerializer 

    def list(self, request, *args, **kwargs):
        form = Form.objects.all()
        serializer = FormSerializer(form, many=True)
        return response(serializer.data)

# def form_details(request):
#     fr = Form.object.get(id = 1)
#     serializer = FormSerializer(fr)
#     json_data = JSONRenderer().render(serializer.data)
#     return HttpResponse(json_data, content_type='application/json')
