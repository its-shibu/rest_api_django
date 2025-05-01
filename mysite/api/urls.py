from django.urls import path
from . import views


urlpatterns = [
    path('blogposts/', views.BlogPostListCreate.as_view(), name='blogpost-list-create'),
    path('formdata/', views.FormDataListCreate.as_view(), name='formdata-list-create'),
    path('blogposts/<int:pk>/', views.BlogPostRetrieveUpdateDestroy.as_view(), name='update'),
    path('formdata/<int:pk>/', views.FormDataRetrieveUpdateDestroy.as_view(), name='delete_update_formdata'),

]