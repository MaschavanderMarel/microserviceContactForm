from os import error
from graphene import ObjectType, String, Schema, Field
from fastapi import FastAPI
from starlette.graphql import GraphQLApp
from mail import send_email
import bleach

class Query(ObjectType):
    class Result(ObjectType):
            status = String()
            message = String()

    sendMessage = Field(Result, emailAddress=String(), message=String())

    def resolve_sendMessage (root, info, emailAddress, message):
        message = bleach.clean(message)
        emailAddress = bleach.clean(emailAddress)

        try:
            send_email(emailAddress, message)
            return Query.Result(status='success', message='Your message was sent to CollAction')
        except:
            return Query.Result(status='error', message='Could not send message')

app = FastAPI()
app.add_route("/", GraphQLApp(schema=Schema(query=Query)))
