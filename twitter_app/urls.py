from django.conf.urls.defaults import *

from twitter_app.views import *

urlpatterns = patterns('twitter_app.views',
    url(r'^$',
        view=main,
        name='twitter_oauth_main'),
    
    url(r'^auth/$',
        view=auth,
        name='twitter_oauth_auth'),

    url(r'^return/$',
        view=return_,
        name='twitter_oauth_return'),
  
    url(r'^list/$',
        view=friend_list,
        name='twitter_oauth_friend_list'),
    
    url(r'^clear/$',
        view=unauth,
        name='twitter_oauth_unauth'),
)
