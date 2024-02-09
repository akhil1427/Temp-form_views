from typing import Any
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView,FormView
from app.forms import *
# Create your views here.
class templatehtml(TemplateView):
    template_name='templatehtml.html'

    def get_context_data(self, **kwargs):
        ECDO=super().get_context_data(**kwargs)
        ECDO['name']='akhil'
        ECDO['age']=23
        return ECDO
    

class collagedata_TV(TemplateView):
    template_name='collagedata_TV.html'

    def get_context_data(self, **kwargs):
        ECDO=super().get_context_data(**kwargs)
        ECDO['CFO']=collageform
        return ECDO
    
    def post(self,request):
        CFDO=collageform(request.POST)
        if CFDO.is_valid():
            CFDO.save()
            return HttpResponse('Inserted data by TV is done')
        


class collagedata_FV(FormView):
    template_name='collagedata_FV.html'
    form_class=collageform
    def form_valid(self, form):
        form.save()
        return HttpResponse('Inserted data by FV is done ')


        