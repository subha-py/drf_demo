from django.conf.urls import url

from posts.views import PostCreateAPIView,PostDetailAPIView,PostListAPIView,PostDestroyAPIView,PostUpdateAPIView

urlpatterns = [
    url(r'^$',PostListAPIView.as_view(),name='list'),
    url(r'create/$',PostCreateAPIView.as_view(),name='create'),
    url(r'(?P<pk>\d+)/$',PostDetailAPIView.as_view(),name='read'),
    url(r'(?P<pk>\d+)/update/$', PostUpdateAPIView.as_view(), name='update'),
    url(r'(?P<pk>\d+)/delete/$', PostDestroyAPIView.as_view(), name='delete'),
]