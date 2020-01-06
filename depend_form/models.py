from django.db import models


# 1
class Country(models.Model):
    country = models.CharField('country', max_length=100)

    def __str__(self):
        return self.country

    class Meta:
        ordering = ('country',)
        verbose_name = 'country'
        verbose_name_plural = 'countries'


# 2
class Region(models.Model):
    region = models.CharField('region', max_length=100)
    country = models.ForeignKey('Country', verbose_name='country', on_delete=models.CASCADE)

    def __str__(self):
        return self.region

    class Meta:
        ordering = ('region',)
        verbose_name = 'region'
        verbose_name_plural = 'regions'


# 3
class AdministrativeArea(models.Model):
    administrative_area = models.CharField('administrative_area', max_length=100)
    region = models.ForeignKey('Region', verbose_name='region', on_delete=models.CASCADE)

    def __str__(self):
        return self.administrative_area

    class Meta:
        ordering = ('administrative_area',)
        verbose_name = 'administrative area'
        verbose_name_plural = 'administrative area'


# 4
class QualityMark(models.Model):
    quality_mark = models.CharField('quality_mark', max_length=100)
    country = models.ForeignKey('Country', verbose_name='country', on_delete=models.CASCADE)
    region = models.ForeignKey('Region', verbose_name='region', on_delete=models.CASCADE)
    administrative_area = models.ForeignKey('AdministrativeArea',
                                            verbose_name='administrative_area',
                                            on_delete=models.CASCADE)

    def __str__(self):
        return self.quality_mark

    class Meta:
        ordering = ('quality_mark',)
        verbose_name = 'quality mark'
        verbose_name_plural = 'quality mark'


# 5
class Container(models.Model):
    vine = models.CharField('vine', max_length=100)
    quality_mark = models.ForeignKey('QualityMark', verbose_name='quality_mark', on_delete=models.CASCADE)

    def __str__(self):
        return self.container

    class Meta:
        verbose_name = 'container'
