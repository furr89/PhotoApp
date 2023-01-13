
from django.urls import path
from .views import HomePageView, PostDetailView, PostFormView

app_name = 'feed' # This is a namespace for... good naming

# Sets the url to the homepage which is then accessible in mysite/urls
# The below will set a path bound to a class in views.py 
urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('details/<int:pk>/', PostDetailView.as_view(), name='detail'), 
    path('post/', PostFormView.as_view(), name='post')
]