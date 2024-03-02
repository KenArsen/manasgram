from apps.post.models import Post


class PostRepository:
    @classmethod
    def get_all_posts(cls, **kwargs) -> list:
        return Post.objects.filter(**kwargs)

    @classmethod
    def get_post_by_id(cls, post_id: int) -> Post:
        return Post.objects.get(pk=post_id)

    @classmethod
    def get_post_by_owner_email(cls, owner_email: str) -> Post:
        return Post.objects.get(owner__email=owner_email)
