from pydoc import describe
import graphene
from graphene_django.types import DjangoObjectType
from .models import StoredImage, UploadedImage

class StoredImageType(DjangoObjectType):
    class Meta:
        model = StoredImage


class Query(object):
    all_images = graphene.List(StoredImageType)

    def resolve_all_images(self, info, **kwargs):
        return StoredImage.objects.all()


class SaveImage(graphene.Mutation):
    images = graphene.Field(StoredImageType)
    class Arguments:
        name = graphene.String()
        img_feature_path = graphene.String()
        image = graphene.String()
      
    def mutate(self, name, image, img_feature_path):
        images = StoredImage(name=name, image=image, img_feature_path=img_feature_path)
        images.save()
        return SaveImage(images=images)


class Mutation(graphene.ObjectType):
    save_image = SaveImage.Field()