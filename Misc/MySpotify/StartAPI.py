import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
cid ='06d8346a7c354743a34c54259bf2d395'
secret = 'c49d8176157d4d08b158f2923f71fe75'
username = "JamesGor2018"
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
scope = 'user-library-read playlist-read-private'
token = util.prompt_for_user_token(username, scope)
if token:
    sp = spotipy.Spotify(auth=token)
else:
    print("Can't get token for", username)

    '''
export SPOTIPY_CLIENT_ID='06d8346a7c354743a34c54259bf2d395'
export SPOTIPY_CLIENT_SECRET='c49d8176157d4d08b158f2923f71fe75'
export SPOTIPY_REDIRECT_URI='localhost:8888'
    '''