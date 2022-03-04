from django.urls import path

from . import views

from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:blog_id>/', views.blogpost, name='blogpost'),
    path('<int:blog_id>/comment', views.comment, name='comment'),
    path('archive/', views.archive, name="archive"),
    path('plan/', views.plan, name='plan'),
    path('about/', views.about, name="about"),
    path('techtips+css/', views.ttpcss, name="techtips+css"),
    path('techtips-css/', views.ttmcss, name="techtips-css"),
]

