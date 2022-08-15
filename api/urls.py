from django.urls import path
from . import views
urlpatterns = [
    # with user system: /user/stacks
    path('stacks/', views.StackList.as_view()),
    # display entire stack info /user/id/stacks, returns cardlist too
    path('stacks/<int:pk>', views.StackDetail.as_view()),
    
    # probably useless
    path('stacks/<int:pk>/cards/', views.CardList.as_view()),
    path('stacks/<stack_id>/cards/<int:pk>', views.CardDetail.as_view())
]