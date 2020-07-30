import request
from bs4 import BeautifulSoup
import webbrowser


def youtube(video):
    try:
        yt_url = "https://www.youtube.com/"
        url = "https://www.youtube.com/results?search?_query"
        tmp = video.replace(' ','+')
        url = url+tmp
        source_code = request.get(url)
        plain_text = source_code.text 
        soup = BeautifulSoup(plain_text,'html.praser')
        url_list=[]
        for link in soup.findAll('a',{'dir':'ltr'}):
            herf = link.get('herf')
            if '/watch?' in herf:
                url_list.append(herf)
                ping = yt_url+url_list[0]

        
 webbrowser.open(ping)
 except:
     print ("ERROR...Internet connection lost") 

  