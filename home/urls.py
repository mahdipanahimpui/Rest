from django.urls import path, include
from . import views
from rest_framework.schemas import get_schema_view



app_name = 'home'

question_urlpatterns = [
    path('list/', views.QuestionListView.as_view(), name='question_list'),
    path('create/', views.QuestionCreateView.as_view(), name='question_create'),
    path('update/<int:pk>', views.QuestionUpdateView.as_view(), name='question_udpate'),
    path('delete/<int:pk>', views.QuestionDeleteView.as_view(), name='question_delete'),
]

urlpatterns = [
    # path('', views.home, name='home')
    path('', views.Home.as_view(), name='home'), # endpoint,
    path('serializer/', views.Serializer.as_view(), name='serializer'),
    path('question/', include(question_urlpatterns)),
]


# shema_urlpatterns = [
#     # ...
#     # Use the `get_schema_view()` helper to add a `SchemaView` to project URLs.
#     #   * `title` and `description` parameters are passed to `SchemaGenerator`.
#     #   * Provide view name for use with `reverse()`.
#     path('schema', get_schema_view(
#         title="Your Project",
#         description="API for all things …",
#         version="1.0.0"
#     ), name='openapi-schema'),
#     # ...
# ]


# urlpatterns += shema_urlpatterns




