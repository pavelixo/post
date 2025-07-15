import pytest
from tests.factories.post_factory import PostFactory

@pytest.mark.django_db
def test_create_post():
    post = PostFactory()
    assert post.pk is not None