import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import os, time
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

f = open('/Users/p.m.d/Documents/credentials.json')
dt = json.load(f)
scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
client_id = dt['client_id']
client_secret = dt['client_secret']
mySpotifyPlaylist = []
# Disable OAuthlib's HTTPS verification when running locally.
# *DO NOT* leave this option enabled in production.
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
api_service_name = "youtube"
api_version = "v3"
client_secrets_file = "ytcredentials.json"
flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
credentials = flow.run_console()
youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

def createSongPlaylist():
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id,
                                                            client_secret=client_secret))
    results = sp.playlist_tracks(playlist_id='https://open.spotify.com/playlist/75jaHyVgpJXlciQ9y7hmsr?si=503c99c2e4d54cc2')
    for i in range(len(results['items'])):
        cx = results['items'][i]['track']['artists'][0]['name']+" - "+results['items'][i]['track']['name']
        mySpotifyPlaylist.append(cx)
    return mySpotifyPlaylist

def createYtPlaylist(title):
    request = youtube.playlists().insert(
        part="contentDetails,id,localizations,snippet,status",
        body={
          "snippet": {
            "title": title,
            "description": "Music",
            "defaultLanguage": "EN"
          },
          "status": {
            "privacyStatus": "private"
          }
        }
    )
    response = request.execute()
    return response['id']
def searchOnYT(item):
    request = youtube.search().list(type='video',q=item,part='snippet', maxResults=10, order='relevance', regionCode="US")
    response = request.execute()
    return response['items'][0]['id']['videoId']

def addOnPlaylist(videoId, playlistId):

    request = youtube.playlistItems().insert(
        part="contentDetails,id,snippet,status",
        body={
          "snippet": {
            "playlistId": playlistId,
            "resourceId": {
              "kind" : "youtube#video",
              "videoId": videoId
            }
          }
        }
    )
    response = request.execute()
    return None


def main():
    ytPlId = "PLikElNvqYFvAlI3V7h42z9tbTh6hGq7x4"
    ytPltitle = "Mr. Blue Sky"
    

    pl = createSongPlaylist()
    newYtPlaylist = createYtPlaylist(ytPltitle)
    for i in pl:
      x = searchOnYT(i)
      addOnPlaylist(x,newYtPlaylist)
      time.sleep(1)
      print(i)

if __name__ == "__main__":
    main()
print('------ DONE ------')
