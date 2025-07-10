from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import AllCourses
from django.template import loader

def Courses(request):
    ac=AllCourses.objects.all()
    template=loader.get_template('TechnicalCourses/Courses.html')
    context={
        'ac':ac,
    }
    return HttpResponse(template.render(context,request))

def detail(request,course_id):
    course=get_object_or_404(AllCourses,pk=course_id)
    return render(request,'TechnicalCourses/detail.html',{'course':course})

def yourchoice(request,course_id):
    course=get_object_or_404(AllCourses,pk=course_id)
    try:
        selected_ct=course.detail_set.get(pk=request.POST['choice'])

    except(KeyError,AllCourses.DoesNotExist):
        return render(request,'TechnicalCourses/detail.html',{
            'course':course,
            'error_message':'Select valid option'
        })

    else:
        selected_ct.your_choice=True
        selected_ct.save()
        return render(request,'TechnicalCourses/detail.html',{'course':course})

