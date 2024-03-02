from apps.post.models import Post


class PostService:
    def __init__(self, repository):
        self._repository = repository

    def get_all_posts(self, **kwargs) -> list:
        return self._repository.get_all_posts(**kwargs)

    def get_post(self, pk):
        return self._repository.get_post_by_id(post_id=pk)

    def create_post(self, data: dict) -> Post:
        pass
        # return Post(owner=data['owner'], description=data['description'], location=data['location'])

    def update_post(self, instance, validate_data) -> Post:
        pass
