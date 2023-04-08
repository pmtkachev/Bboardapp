from django.urls import path
from .views import MainPage, BbByRubView, BbCreateView, BbDetailView, BbEditView, BbDelete

urlpatterns = [
    path('<int:rubric_id>/', BbByRubView.as_view(), name='by_rubric'),
    path('', MainPage.as_view(), name='index'),
    path('add/', BbCreateView.as_view(), name='add'),
    path('detail/<int:pk>/', BbDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', BbEditView.as_view(), name='update'),
    path('delete/<int:pk>/', BbDelete.as_view(), name='delete'),
]
