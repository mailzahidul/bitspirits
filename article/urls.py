from django.urls import path
from . import views
urlpatterns = [
    path('news/', views.news, name='news'),
    path('news/<int:id>', views.news_view, name='news_view'),
    path('event/', views.event, name='event'),
    path('event/<int:id>', views.event_view, name='event_view'),
    path('gallery/', views.gallery, name='gallery'),
    path('event_search/', views.event_search, name='event_search'),
    path('news_search/', views.news_search, name='news_search'),
]