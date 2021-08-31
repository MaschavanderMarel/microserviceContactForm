from graphene import ObjectType, String, Schema
from fastapi import FastAPI
from starlette.graphql import GraphQLApp
from mail import email

class Query(ObjectType):

    sendMessage = String(emailAddress=String(), message=String())

    def resolve_sendMessage (root, info, emailAddress, message):
        email(emailAddress, message)
        return 'Your message was sent to CollAction'

app = FastAPI()
app.add_route("/", GraphQLApp(schema=Schema(query=Query)))
