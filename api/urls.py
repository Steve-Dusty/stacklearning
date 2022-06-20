from django.urls import path
from . import views
urlpatterns = [
    path('stacks/', views.StackList.as_view()),
    path('stack/<int:pk>', views.StackDetail.as_view()),
    path('cards/', views.CardList.as_view()),
    path('card/<int:pk>', views.CardDetail.as_view())

]