import graphene
import json
from datetime import datetime
import uuid


class User(graphene.ObjectType):
    id = graphene.ID(default_value=str(uuid.uuid4()))
    username = graphene.String()
    created_at = graphene.DateTime(default_value=datetime.now()) # can set default values


# this is how you create a model of the data you want to insert etc (making a table)
class Query(graphene.ObjectType):
    users = graphene.List(User, limit=graphene.Int())  # makes a list from the User 'template'
    hello = graphene.String()
    is_Admin = graphene.Boolean()

    def resolve_hello(self, info):  # have to prepend func name with resolve
        return "world"  # here you can return the values that will be in 'hello'

    def resolve_is_Admin(self, info):
        return True

    def resolve_users(self, info, limit=None):
        return [
                   User(id="1", username="Greg", created_at=datetime.now()),
                   User(id="2", username="Jack", created_at=datetime.now())
               ][:limit]  # how to add a limit to the results


class CreateUser(graphene.Mutation):
    user = graphene.Field(User)

    class Arguments:
        username = graphene.String()  # arguments to pass in when creating a user

    # def mutate(self, info, username):
    #     newUser = User(id="3", username=username, created_at=datetime.now())
    #     return CreateUser(user=newUser)

    def mutate(self, info, username):
        user = User(username=username)
        return CreateUser(user=user)  # since default values, don't have to specify id and cc


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()


schema = graphene.Schema(query=Query, mutation=Mutation, auto_camelcase=False)  # create the schema, set auto to false
# otherwise you have to execute the queries in camelCase even if it is written in snake case :
# so if True... is_admin should be written as isAdmin in execution of query

# result = schema.execute(
#     """
#     {
#         users {
#             id
#             username
#             created_at
#         } 
#     }
#     """
# ) # here you run the query

# result = schema.execute(
#     """
#    mutation {
#        create_user(username : "Jeff") {
#            user {
#                id
#                username
#                created_at
#            }
#        }
#    }
#     """
# )  # make sure to use double quotes inside double quotes here... also can anly call the user you just created

# passing in variable names :
result = schema.execute(
    """
   mutation($username : String) {
       create_user(username : $username) {
           user {
               id
               username
               created_at
           }
       }
   }
    """,
    variable_values = {"username" : "Kelvin"}
)  # HAVE TO SAY 'variable_values' !!!!

# print(result.data.items())  # -- returns results in unformatted way

items = dict(result.data.items())
# # print(dictResult)
print(json.dumps(items, indent=2))
# # json dumps also return item in the form of a dictionary/ object


# when passing in variables into a normal query , you can't just do it the normal shorthand way :
# have to do the following :
# result = schema.execute(
#     """
#     query($limit : Int) {
#         users(limit : $limit) {
#             id
#             username
#             created_at
#         }
#     }
#     """,
#     variable_values = {"limit" : 1}
# )  -- you can give your query/mutation a name --> query/mutation someName {...}

# you know what the self argument refers to, but yiu can use the info arg to access the context of a 
# query for example :

# result = schema.execute(
#     """
#     {
#         users {
#             ...
#         }
#     }
#     """,
#     context = {"is_anon" : True}
# )
# then in the resolver --> 
# def resolver_users(self, info):
#     if info.context.get("is_anon"):  # is true ?
#         raise Exception("Not authorized to write post")
#     return ...