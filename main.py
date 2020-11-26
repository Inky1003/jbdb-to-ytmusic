from argon2 import PasswordHasher
import requests
import json
import base64
import time
from ytmusicapi import YTMusic
ytmusic = YTMusic("request_h.json")


def sres (a, n):
    search_results = ytmusic.search(a + n)
    final_results = dict()
    iter = 0
    for result in search_results:
        if result["resultType"] == "song" or result["resultType"] == "video":
            r = requests.get(result["thumbnails"][len(result["thumbnails"])-1]["url"], stream=True)
            if r.status_code == 200:
                rawimg = r.content
                b64img = base64.b64encode(rawimg).decode('utf-8')
            else:
                b64img = "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"
            final_results.update({iter: {"thumb" : b64img, "url" : "https://www.youtube.com/watch?v=" + result["videoId"]}})
            iter += 1
    frsend = json.dumps(final_results).replace("'", '"')
    ph = PasswordHasher()
    shash = ph.hash("bancojbfm")


    requestsend = {
        "links": frsend.replace("\"", "\\\""),
        "nome":  a,
        "artista": n,
        "pash": shash
    }
    ureq = requests.post("http://jbfm.inky1003.com.br/drfdb.php", requestsend)
    print(ureq.text)




if __name__ == '__main__':
    while True:
        freq = requests.get("http://jbfm.inky1003.com.br/drfdb.php?contar=ok")
        if freq.text != "N/A":
            an = freq.text.split("|")
            sres(an[0], an[1])
            time.sleep(10)
        else:
            time.sleep(3600)
