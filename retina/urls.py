"""retina URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from graduation_project import views

from rest_framework import routers

p = routers.DefaultRouter()
p.register('',views.patient_LIST)

d = routers.DefaultRouter()
d.register('',views.doctor_LIST)

log = routers.DefaultRouter()
log.register('',views.login_LIST)

s_d = routers.DefaultRouter()
s_d.register('',views.signup_doctor_LIST)

s_p = routers.DefaultRouter()
s_p.register('',views.signup_patient_LIST)

g = routers.DefaultRouter()
g.register('',views.gps)

img = routers.DefaultRouter()
img.register('',views.image)

ask = routers.DefaultRouter()
ask.register('ask',views.ask_LIST)

answer = routers.DefaultRouter()
answer.register('answer',views.answer_LIST)

center = routers.DefaultRouter()
center.register('center',views.center_LIST)

review= routers.DefaultRouter()
review.register('review',views.review_LIST)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('p/',include(p.urls)),
    path('d/',include(d.urls)),
    path('l/',include(log.urls)),
    path('sd/',include(s_d.urls)),
    path('sp/',include(s_p.urls)),
    path('g/',include(g.urls)),
    path('img/',include(img.urls)),
    path('ask/',include(ask.urls)),
    path('answer/',include(answer.urls)),
    path('center/',include(center.urls)),
    path('review/',include(review.urls)),
    path('api/stripe/', include('graduation_project.urls')),
]

