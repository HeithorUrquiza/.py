from bs4 import BeautifulSoup
import requests
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

URL = "https://www.billboard.com/charts/hot-100/"

class BuildPlaylist:
    
    def __init__(self) -> None:
        load_dotenv()
        self.date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
        self.songs_title = None
        self.sp = None
        self.songs_uri = []


    def scraping_billboard(self):
        # Scraping Billboard 100
        resp = requests.get(f"{URL}{self.date}/")
        soup = BeautifulSoup(resp.text, "html.parser")
        self.songs_title = [song.getText().strip() for song in soup.select("li ul li h3")]
        

    def get_spotify_authentication(self):
        #Spotify Authentication
        scope = "playlist-modify-private"
        self.sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=os.getenv("CLIENT_ID"), 
                client_secret=os.getenv("CLIENT_SECRET"), 
                redirect_uri="http://example.com", 
                scope=scope,
                show_dialog=True,
                cache_path="Projects/Intermediate/musical-time-machine/entities/token.txt"
                )
            )


    def searching_songs(self):
        #Searching Spotify for songs by title
        year = self.date.split("-")[0]
        for song in self.songs_title:
            # Pesquisa da música
            results = self.sp.search(q=f"track:{song} year:{year}", type="track")
            
            try:
                uri = results["tracks"]["items"][0]["uri"]
                self.songs_uri.append(uri)
            except:
                print(f"{song} doesn't exit on Spotify")
    
    
    def create_playlist(self):
        #Creating a new private playlist in Spotify
        playlist = self.sp.user_playlist_create(
            user=self.sp.me()["id"], 
            name=f"{self.date} Billboard 100", 
            public=False, 
            description="Top 100 songs of this date"
            )

        #Adding songs found into the new playlist
        self.sp.playlist_add_items(playlist_id=playlist["id"], items=self.songs_uri)