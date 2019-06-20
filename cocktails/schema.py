import graphene
from graphene_django.types import DjangoObjectType
from cocktails.models import Cocktail


class CocktailType(DjangoObjectType):
    class Meta:
        model = Cocktail


class Query(object):
    all_cocktails = graphene.List(CocktailType)
    cocktail = graphene.Field(
        CocktailType, 
        id=graphene.String()
    )

    def resolve_all_cocktails(self, info, **kwargs):
        return Cocktail.objects.all()

    def resolve_cocktail(self, info, id):
        return Cocktail.objects.get(pk=id)
