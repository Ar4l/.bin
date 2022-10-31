import spotipy 
from spotipy.oauth2 import SpotifyOAuth

scope = 'user-library-read user-top-read'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items'][:100]):
    track = item['track']
    print(idx, track['artists'][0]['name'], ' – ', track['name'])


ranges = ['short_term', 'medium_term', 'long_term']
for sp_range in ranges:
    print('range:', sp_range)
    results = sp.current_user_top_tracks(time_range=sp_range, limit=50)
    for i, item in enumerate(results['items']):
        print(i, item['name'], '//', item['artists'][0]['name'])
    print()
    import pdb; pdb.set_trace()