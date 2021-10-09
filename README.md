# api_yatube
api_yatube

##This is DRF project consists of 2 app: posts and api.
###api app includes:
serializers.py (UserSerializer, GroupSerializer, PostSerializer, CommentSerializer which are inherited from ModelSerializer);
views.py (UserViewSet(ModelViewSet); GroupViewSet(ReadOnlyModelViewSet); PostViewSet(ModelViewSet); CommentViewSet(ModelViewSet));
###posts app 
with models such as Group, Post, Comment.