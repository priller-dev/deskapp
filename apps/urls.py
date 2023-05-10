from django.urls import path

from apps.views import index_view, detail_view

urlpatterns = [
    path('', index_view, name='index_view'),
    path('detail/<uuid:uid>', detail_view, name='detail_view'),
]
