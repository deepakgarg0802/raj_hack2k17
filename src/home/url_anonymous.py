from django.conf.urls import url, include

from .views import anonymous_tip, anonymous_user_login, anonymous_dashboard, get_interact_anonymous

urlpatterns = [

    url(r'^$', anonymous_user_login, name='anonymous_user_login'),
    url(r'^tip$', anonymous_tip, name='anonymous_tip'),
    url(r'^dashboard$', anonymous_dashboard, name="anonymous_dashboard"),
    url(r'^anonymous/get_interact/', get_interact_anonymous, name = "get_interact_anonymous")
]
