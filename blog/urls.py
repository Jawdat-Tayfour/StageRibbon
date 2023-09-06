from django.urls import path 


from .views import announcements, PostDetailView,SoonTemplateView,AboutTemplateView,GamesListView


urlpatterns = [
    path("",announcements,name="announcements"),
    path("<uuid:pk>", PostDetailView.as_view(),name="post_detail"),
    path("Soon",SoonTemplateView.as_view(),name="soon"),
    path("About",AboutTemplateView.as_view(),name="about"),
    path("Games",GamesListView.as_view(),name="games"),
    
]
