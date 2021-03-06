import requests
from auth0.v3.authentication import GetToken
from auth0.v3.management import Auth0
from django.conf import settings
from django_rq import job


def get_auth0_token():
    get_token = GetToken(settings.AUTH0_DOMAIN)
    token = get_token.client_credentials(
        settings.AUTH0_CLIENT_ID,
        settings.AUTH0_CLIENT_SECRET,
        f'https://{settings.AUTH0_DOMAIN}/api/v2/',
    )
    return token


def get_auth0_client():
    token = get_auth0_token()
    client = Auth0(
        settings.AUTH0_DOMAIN,
        token['access_token'],
    )
    return client

def put_auth0_payload(endpoint, payload):
    token = get_auth0_token()
    access_token = token['access_token']
    headers = {
        'Authorization': f'Bearer {access_token}',
    }
    response = requests.put(
        f'https://{settings.AUTH0_DOMAIN}/api/v2/{endpoint}',
        headers=headers,
        json=payload,
    )
    return response

def get_user_data(user_id):
    client = get_auth0_client()
    data = client.users.get(user_id)
    return data

@job
def update_user(user):
    data = get_user_data(user.username)
    user.data = data
    user.name = data.get('name', '')
    user.email = data.get('email', None)
    user.save()
    return user


@job
def delete_user(user_id):
    client = get_auth0_client()
    response = client.users.delete(user_id)
    return response
