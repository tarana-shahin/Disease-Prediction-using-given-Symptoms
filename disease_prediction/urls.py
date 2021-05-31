from django.urls import path, include
from . import views
# from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('knowyourdisease',views.knowyourdisease,name='knowyourdisease'),
    path('feedback',views.feedback,name='feedback'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('predict',views.predict,name='predict'),
    path('doctornearby',views.doctornearby,name='doctornearby'),
    path('feedbacksubmit',views.feedbacksubmit,name='feed'),
]