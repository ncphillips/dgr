from graphene import ObjectType, Schema, String
import cocktails.schema


class Query(cocktails.schema.Query, ObjectType):
    hello = String()

    def resolve_hello(self, ctx):
        return "Wrold"


schema = Schema(query=Query)
