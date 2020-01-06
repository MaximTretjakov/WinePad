from django.views.generic.base import View
from django.shortcuts import render

from depend_form.forms import DependForm as DepForm


class DependForm(View):

    def get(self, request):
        context = {}

        country = request.GET.get('country')
        region = request.GET.get('region')
        administrative_area = request.GET.get('administrative_area')
        quality_mark = request.GET.get('quality_mark')

        context['form'] = DepForm(country, region, administrative_area, quality_mark)

        return render(request, 'depend_form.html', context)
