from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from main.forms import ModelObjectForm
from main.models import ObjectEntry

# Create your views here.
def show_main(request):
    object_entries = ObjectEntry.objects.all()
    context = {
        'name': 'Darren Marcello Sidabutar',
        'class': 'PBP KKI',
        'name_app': 'E-Commerce',
        'object_entries': object_entries
    }
    print(object_entries)

    return render(request, "main.html", context)

def model_object(request):
    form = ModelObjectForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_model_object.html", context)

def show_xml(request):
    data = ObjectEntry.objects.all()

def show_xml(request):
    data = ObjectEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = ObjectEntry.objects.all()

def show_json(request):
    data = ObjectEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = ObjectEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = ObjectEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

