from plexapi.server import PlexServer

# 登录PlexServer至plex
baseurl='http://howard115.synology.me:32400'
token='yTVZiyvTcy9DMQG1FrxJ'
plex=PlexServer(baseurl, token)

# Example 8: Get audio/video/all playlists
for playlist in plex.playlists():
    print(playlist.title)
print(plex.playlists())

# Playlist.create(server=plex, title="wqe", items=Audio)
movies=plex.library.section('电影')
print(movies)
for video in movies.search():
    print(video.title)
pli = plex.createCollection(title="wqe", items=movies)