import urllib.request

def scrapeSeasonOfShow(show, season, episodes):

    print("Scraping Season", season, "of", show) 

    for episode in range(1, episodes + 1):

        season_str = str(season)
        episode_str= str(episode)

        if season < 10: 
            season_str = "0" + str(season)
        if episode < 10: 
            episode_str = "0" + str(episode)

        filename = "s" + season_str + "e" + episode_str
        url = 'https://www.springfieldspringfield.co.uk/view_episode_scripts.php?tv-show=' + show + '&episode=' + filename

        try: 
            req = urllib.request.Request(url)
            resp = urllib.request.urlopen(req)
            respData = resp.read()
            from bs4 import BeautifulSoup #pip install beautifulsoup4
            soup = BeautifulSoup(respData, features="html.parser")
            res = soup.find('div',{'class':'scrolling-script-container'}).text
            
        except: 
            print("Error printing episode", episode)
            continue
        #print(respData)



        import io
        import os
        path = "corpora/" + show + "/" + show + "_" + filename + ".txt"  #os.path.dirname(filename)
        dirname = "corpora/" + show
        if not os.path.exists(dirname):
            os.makedirs(dirname)

        with io.open(path, "w", encoding="utf-8") as f:
            f.write(res.strip())


    return True




show = "13-reasons-why-2017"
season = 3 
episodes = 14



# print(scrapeSeasonOfShow(show, season, episodes))
