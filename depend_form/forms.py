from django import forms
from .models import Country, Region, AdministrativeArea, QualityMark, Container


class DependForm(forms.Form):

    country = forms.CharField(max_length=100, required=False)

    region = forms.ModelChoiceField(
        queryset=Region.objects.none(),
        required=False
    )

    administrative_area = forms.ModelChoiceField(
        queryset=AdministrativeArea.objects.none(),
        required=False
    )

    quality_mark = forms.ModelChoiceField(
        queryset=QualityMark.objects.none(),
        required=False
    )

    class Meta:
        fields = ('country', 'region', 'administrative_area', 'quality_mark')

    def __init__(self, country=None, region=None, administrative_area=None, quality_mark=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if country:
            self.fields['country'].queryset = country
            self.fields['region'].queryset = Region.objects.filter(country__country__contains=country)
        if region:
            self.fields['administrative_area'].queryset = AdministrativeArea.objects.filter(region__pk=str(region))
        if administrative_area:
            self.fields['quality_mark'].queryset = QualityMark.objects.filter(administrative_area__pk=str(administrative_area))
