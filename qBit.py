import requests
import jq

#Errored torrents
urlErrored = 'http://192.168.1.224:8080/api/v2/torrents/info?filter=errored&category=test'
hashesErrored = (jq.compile(".[] | .hash").input(requests.get(urlErrored).json()).text()).replace('"', '').split()
namesErrored = (jq.compile(".[] | .name").input(requests.get(urlErrored).json()).text()).replace('"', '')

deleteErrored = ("http://192.168.1.224:8080/api/v2/torrents/delete?hashes=" + "|".join(hashesErrored) + "&deleteFiles=true")

if namesErrored != "":
    print("Deleted the following Errored torrents:")
    print(namesErrored)
    requests.get(deleteErrored)

#Completed torrents
urlCompleted = 'http://192.168.1.224:8080/api/v2/torrents/info?filter=completed'
hashesCompleted = (jq.compile(".[] | .hash").input(requests.get(urlCompleted).json()).text()).replace('"', '').split()
namesCompleted = (jq.compile(".[] | .name").input(requests.get(urlCompleted).json()).text()).replace('"', '')

deleteCompleted = ("http://192.168.1.224:8080/api/v2/torrents/delete?hashes=" + "|".join(hashesCompleted) + "&deleteFiles=false")

if namesCompleted != "":
    print("Deleted the following Completed torrents:")
    print(namesCompleted)
    requests.get(deleteCompleted)