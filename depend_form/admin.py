from django.contrib import admin

from .models import Country, Region, AdministrativeArea, QualityMark, Container


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('country',)


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('region', 'country',)
    search_fields = ('region', )
    list_filter = ('region',)


@admin.register(AdministrativeArea)
class AdministrativeAreaAdmin(admin.ModelAdmin):
    list_display = ('administrative_area', 'region',)
    search_fields = ('administrative_area', )
    list_filter = ('administrative_area',)


@admin.register(QualityMark)
class QualityMarkAdmin(admin.ModelAdmin):
    list_display = ('quality_mark', 'country', 'region', 'administrative_area',)
    search_fields = ('quality_mark', )
    list_filter = ('country', 'region', 'administrative_area',)


@admin.register(Container)
class ContainerAdmin(admin.ModelAdmin):
    list_display = ('vine', 'quality_mark',)
    search_fields = ('vine', )
    list_filter = ('quality_mark',)
