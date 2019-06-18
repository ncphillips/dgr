import graphene
from graphene_django.types import DjangoObjectType
from cocktails.models import Cocktail


class CocktailType(DjangoObjectType):
    class Meta:
        model = Cocktail


class Query(object):
    all_cocktails = graphene.List(CocktailType)

    def resolve_all_cocktails(self, info, **kwargs):
        return Cocktail.objects.all()
