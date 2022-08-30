from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello!")



def fist(request):
    projects = Project.objects.all()
    return HttpResponse(str(projects))