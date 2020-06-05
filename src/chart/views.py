from django.shortcuts import render
from .models import Programing


def prog_stat(request):
	prog_stat = Programing.objects.all()
	context = {'prog_stat':prog_stat}
	return render(request,'chart/index.html',context)