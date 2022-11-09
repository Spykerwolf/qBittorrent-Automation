from qbittorrent import Client
qb = Client('http://localhost:8080')
qb.login()
import time

while True:
    hashes = []
    all = qb.torrents()
    completed = qb.torrents(filter='completed', category='RARBG')
    VR = qb.torrents(filter='completed', category='VR')
    stalled= qb.torrents(filter="stalled")
    
    if stalled:
        for torrent in stalled:
            if torrent['num_seeds'] == 0: 
                hashes.append(torrent['hash'])
                print("Deleted: " + torrent['name'] + " - 0 seeds")
        qb.delete(hashes)

    if completed or VR:
        for torrent in completed or VR:
                hashes.append(torrent['hash'])
                print("Deleted: " + torrent['name'] + " - finished downloading")
        qb.delete(hashes)
    else:
        time.sleep(300)