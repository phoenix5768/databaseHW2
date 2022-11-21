from django import forms
from django.forms import ModelForm
from .models import Doctor, Publicservant, Record, Specialize, Users, Country, Discover, Disease, Diseasetype

class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = "__all__"

class CountryForm(ModelForm):
    class Meta:
        model = Country
        fields = "__all__"

class DiseaseForm(ModelForm):
    class Meta:
        model = Disease
        fields = "__all__"

class DiseasetypeForm(ModelForm):
    class Meta:
        model = Diseasetype
        fields = "__all__"

class DiscoverForm(ModelForm):
    class Meta:
        model = Discover
        fields = "__all__"

class UserForm(ModelForm):
    class Meta:
        model = Users
        fields = "__all__"

class SpecializeForm(ModelForm):
    class Meta:
        model = Specialize
        fields = "__all__"

class ServantForm(ModelForm):
    class Meta:
        model = Publicservant        
        fields = "__all__"

class RecordForm(ModelForm):
    class Meta:
        model = Record        
        fields = "__all__"