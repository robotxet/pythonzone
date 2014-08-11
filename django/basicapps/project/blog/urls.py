from django.conf.urls import patterns, include, url

from views import PostListView, CategoryListView

urlpatterns = patterns('',
                       url(r'^$',
                           PostListView.as_view(),
                           name='blog_index'
                           ),
                       url(r'^categories/$',
                           CategoryListView.as_view(),
                           name='blog_category_list'
                           )
)
