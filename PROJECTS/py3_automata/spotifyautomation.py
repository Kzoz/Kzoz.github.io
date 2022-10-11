import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json

f = open('/Users/p.m.d/Documents/credentials.json')
dt = json.load(f)

client_id = dt['client_id']
client_secret = dt['client_secret']
device_id = dt['device_id']
playlist_id = dt['playlist_id']


sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id,
                                                           client_secret=client_secret))
results = sp.playlist_tracks(playlist_id='https://open.spotify.com/playlist/75jaHyVgpJXlciQ9y7hmsr?si=cf30167cd8544de4',limit=20)
for i in range(len(results['items'])):
    print(results['items'][i]['track']['artists'][0]['name'],'--',results['items'][i]['track']['name'],'--',
    results['items'][i]['track']['popularity'])

