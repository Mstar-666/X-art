from django.conf.urls import url, include
from django.shortcuts import render

import xadmin as admin
from video.models import Category


def to_Index(request):
    cates = Category.objects.filter(parent__isnull=True)
    return render(request, 'index.html',locals())

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    url(r'^', to_Index),

]
