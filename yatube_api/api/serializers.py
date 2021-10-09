from posts.models import Comment, Group, Post, User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.StringRelatedField(many=True,
                                           read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'posts')
        ref_name = 'ReadOnlyUsers'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug')


class PostSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(source="author.username",
                                                read_only=True,
                                                default=serializers
                                                .CurrentUserDefault())

    class Meta:
        model = Post
        fields = ('id', 'text', 'pub_date', 'author', 'group')
        read_only_fields = ('author',)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(source="author.username",
                                                read_only=True,
                                                default=serializers
                                                .CurrentUserDefault())
    post = serializers.PrimaryKeyRelatedField(read_only=True,
                                              source="post.id")

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('author',)
