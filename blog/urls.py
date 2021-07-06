from django.urls import path
from blog        import views

app_name = 'blog'
urlpatterns = [
    path('', views.ArticlesView.as_view(), name='index'),
    path('articles/<int:pk>', views.view_article_details, name='single_article'),
]
