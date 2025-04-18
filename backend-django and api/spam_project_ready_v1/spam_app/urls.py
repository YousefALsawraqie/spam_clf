# urls.py file content will go here
from django.urls import include, path
from . import views, api_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('nodes',views.NoteViewset,basename='nodes')

urlpatterns = [
    path('', views.message_input, name='message_input'),
    path('result/', views.classification_result, name='classification_result'),
    path('api/classify/', api_views.classify_api, name='classify_api'), 
    path('api/',include(router.urls)) # إضافة API
]

