from django.urls import path,include
from .views import AllBlogView,BlogView

urlpatterns = [
    path('', AllBlogView.as_view()),
    path('<int:id>/', BlogView.as_view()),
    path('comments/', include('comments.urls')),
]