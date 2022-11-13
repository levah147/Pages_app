from django.urls import path
from .views import HomePagesView,AboutPagesView

urlpatterns =[
    path('', HomePagesView.as_view(), name='home'),
    path('about/', AboutPagesView.as_view(), name='about'),

]