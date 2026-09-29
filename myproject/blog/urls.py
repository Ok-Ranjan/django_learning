from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name="blog_home"),
    path('about/', views.about, name="blog_about"),
    path('user-profile/<str:username>/', views.user_profile, name="user_profile"),
    path('post/<int:post_id>/', views.post_details, name="post"),
    
    re_path(r'^article/(?P<year>[0-9]{4})/$', views.article_by_year, name="article_by_year"),
    re_path(r'^article/(?P<date>[0-9]{4}-[0-9]{2}-[0-9]{2})/$', views.article_by_date, name="article_by_date"),

    path('article/<int:year>/<int:month>/<int:date>', views.article_details, name="article_details")

]