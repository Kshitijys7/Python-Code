from django.shortcuts import render
from django.http import HttpResponse
from .models import AllCourses
from django.template import loader
from django.http import Http404

def first(request):
    ac=AllCourses.objects.all()
    template=loader.get_template('firstapp/first.html')
    context={
        'ac':ac,
    }
    return HttpResponse(template.render(context,request))

def detail(request,courseid):
    try:
        course=AllCourses.objects.get(pk=courseid)
    except AllCourses.DoesNotExist:
        raise Http404('Course not found.....')
    return render(request,'firstapp/detail.html',{'course':course})
