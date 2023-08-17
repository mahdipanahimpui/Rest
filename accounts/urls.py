from django.urls import path
from . import views
from rest_framework.authtoken import views as auth_token
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



app_name = 'accounts'
urlpatterns = [
    path('register', views.UserRegisterView.as_view(), name='user_register'),
    
]




# for token auth, add 'rest_framework.authtoken' in installed apps in settings.
# make migration
# set the ALL views authentication type in setting by:
        #REST_FRAMEWORK = {
        #     'DEFAULT_AUTHENTICATION_CLASSES': [
        #         'rest_framework.authentication.BasicAuthentication',
        #         'rest_framework.authentication.SessionAuthentication',
        #     ]
        # }

# from rest_framework.authtoken import views as auth_token or jwt
urlpatterns += [
    # path('api-token-auth/', auth_token.obtain_auth_token)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]




router = routers.SimpleRouter()
router.register('user', views.UserViewSet) # url, view name
urlpatterns += router.urls 