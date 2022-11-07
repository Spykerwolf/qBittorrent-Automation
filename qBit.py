from qbittorrent import Client
qb = Client('http://localhost:8080')
qb.login()
import time

while True:

    hashes = []
    completedTorrents = qb.torrents(filter='completed', category='RARBG')

    if completedTorrents:
        for torrent in completedTorrents:
            hashes.append(torrent['hash'])
        print("Deleting the following torrents: \n" + torrent['name'])
        qb.delete(hashes)
    else:
        print("Nothing more to delete, waiting...")
    
    time.sleep(300)