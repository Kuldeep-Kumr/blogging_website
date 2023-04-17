from django.urls import path
from .views import CommentView,ReplyView
urlpatterns = [
    path('<int:id>', CommentView.as_view()),
    path('reply/<int:id>',ReplyView.as_view())
]