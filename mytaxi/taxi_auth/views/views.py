# Create your views here.
import requests
from oauth2_provider.decorators import protected_resource
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

"""
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)
"""


##Generate Your CLient id and Client Secret From Django admin add aplication or from
CLIENT_ID = 'OzuBESDIJVB1pKJUYup6YOKTZ7XhjWi7jVrUJq3D'
CLIENT_SECRET = 'ku24kxVCnCftN8mD0jO8dskzjh546Qv0wckF3wehjzqD4zMlBUzM0HZ0fogKRBfk95AkhEVA7lubjoscoC1BwMePGvaozgmAspeOqXIVoTAjCUgA5EfLbExAIpdmSLqM'


@api_view(['POST'])
@permission_classes([AllowAny])
def token(request):
    '''
    Gets tokens with username and password. Input should be in the format:
    {"username": "username", "password": "1234abcd"}
    '''
    #print(request.data['username'],request.data['password'])

    r = requests.post(
    'http://localhost:8000/o/token/',
        data={
            'grant_type': 'password',
            'username': request.data['username'],
            'password': request.data['password'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    # Return if its Oauth return bad request
    if r.status_code == 400:
        return Response({'message': 'invalid Username or Password'}, status=403)
    # Return if Username password is ok
    return Response(r.json(), r.status_code)


@api_view(['POST'])
@permission_classes([AllowAny])
def revoke_token(request):
    '''
    Method to revoke tokens.
    {"token": "<token>"}
    '''
    r = requests.post(
        'http://localhost:8000/o/revoke_token/',
        data={
            'token': request.data['token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    # If it goes well return sucess message (would be empty otherwise)
    if r.status_code == requests.codes.ok:
        return Response({'message': 'token revoked'}, r.status_code)
    # Return the error if it goes badly
    return Response(r.json(), r.status_code)





