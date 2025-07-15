import factory
from contents.models import Post

class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post
    
    title = factory.Faker("sentence")
    body = factory.Faker("text")
