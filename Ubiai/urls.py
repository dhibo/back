from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from UUbiaiApplication.views import DocumentAnnotationView , DocumentViewSet, LabelViewSet, AnnotationViewSet

router = DefaultRouter()
router.register(r'documents', DocumentViewSet)
router.register(r'labels', LabelViewSet)
router.register(r'annotations', AnnotationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('export/<int:id>/', DocumentAnnotationView.as_view(), name='document-annotation'),

]