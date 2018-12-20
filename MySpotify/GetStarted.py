import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


cid ='06d8346a7c354743a34c54259bf2d395'
secret = 'c49d8176157d4d08b158f2923f71fe75'
username = "JamesGor2018"
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)

birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

results = spotify.artist_albums(birdy_uri, album_type='album')
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])