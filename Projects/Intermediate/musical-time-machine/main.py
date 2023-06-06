from entities.build_playlist import BuildPlaylist

app = BuildPlaylist()
app.scraping_billboard()
app.get_spotify_authentication()
app.searching_songs()
app.create_playlist()