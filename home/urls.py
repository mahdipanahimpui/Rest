from django.urls import path, include
from . import views

app_name = 'home'

question_urlpatterns = [
    path('list/', views.QuestionListView.as_view(), name='question_list'),
    path('create', views.QuestionCreateView.as_view(), name='question_create'),
    path('update/<int:pk>', views.QuestionUpdateView.as_view(), name='question_udpate'),
    path('delete/<int:pk>', views.QuestionDeleteView.as_view(), name='question_delete'),
]

urlpatterns = [
    # path('', views.home, name='home')
    path('', views.Home.as_view(), name='home'), # endpoint,
    path('serializer/', views.Serializer.as_view(), name='serializer'),
    path('question/', include(question_urlpatterns))
]
