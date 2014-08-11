from django.conf.urls import patterns, include, url

from views import PostListView

urlpatterns = patterns('blog.views',
                       url(r'^$',
                           PostListView.as_view(),
                           name='blog_index'
                           )
)
