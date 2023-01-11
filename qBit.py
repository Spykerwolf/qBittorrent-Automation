# nssm install “qBit” “C:\Python39\Python.exe” “C:\Users\wills\Desktop\Coding\qBittorrent-Automation\qBit.py”
# nssm set qBit AppStderr "C:\Users\wills\Desktop\Coding\python-web-scraper\logs\out.log"
# nssm set qBit AppStdout "C:\Users\wills\Desktop\Coding\python-web-scraper\logs\error.log"
# nssm start qBit

    
import time
from qbittorrent import Client

currentEpochTime = int(time.time())
currentTime = time.ctime()
anHourAgo = currentEpochTime - 3600

try:
    qb = Client('http://localhost:8080')
    qb.login()
except:
    print("qBittorrent is not running")
    exit()

    
def qBitRemove():

    hashes = []
    completedNoCategory = qb.torrents(filter='completed', category='')
    completedRARBG = qb.torrents(filter='completed', category='RARBG')
    completedJackett = qb.torrents(filter='completed', category='Jackett')
    completedVR = qb.torrents(filter='completed', category='VR')
    completedOld = qb.torrents(filter="completed", category= 'Old')
    stalledRARBG = qb.torrents(filter="stalled", category='RARBG')
    stalledJackett = qb.torrents(filter="stalled", category='Jackett')
    stalledOld = qb.torrents(filter="stalled", category= 'Old')
    stalledVR = qb.torrents(filter="stalled", category= 'VR')

    
    if stalledRARBG or stalledJackett or stalledOld or stalledVR:
        for torrent in stalledRARBG or stalledJackett or stalledOld or stalledVR:
            lastActivity = torrent['last_activity']
            lastActivityTime = time.ctime(lastActivity) 
            if torrent['num_seeds'] == 0 and lastActivity < anHourAgo:
                hashes.append(torrent['hash'])
                print(f"Deleted: {torrent['name'][0:70]} - {torrent['num_seeds']} seeds - stalled for more than an hour - last active on {lastActivityTime}")
        qb.delete(hashes)
    

    if completedNoCategory or completedVR or completedRARBG or completedJackett or completedOld:
        for torrent in completedNoCategory or completedVR or completedRARBG or completedJackett or completedOld:
                hashes.append(torrent['hash'])
                print(f"Deleted: {torrent['name'][0:70]} - finished downloading")
        qb.delete(hashes)

while True:
    qBitRemove()
    time.sleep(30)