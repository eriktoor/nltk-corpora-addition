import bs4 
import requests

def getInfoFromID(id):
    res = requests.get("https://www.springfieldspringfield.co.uk/episode_scripts.php?tv-show=" + id)

    soup = bs4.BeautifulSoup(res.text, features="html.parser")

    res = []

    count_season, count_episode = 0, 0

    for season in soup.find_all('div',{'class':'season-episodes'}):
        count_season +=1
        for episode in season.find_all('a', {'class':'season-episode-title'}):
            count_episode += 1 
            season = soup.find_all('h3')[count_season-1].get('id').split("season")[1]
        res.append((int(season), count_episode))
        count_episode = 0

    return res 


# id = "60-minutes-1968"
# print(getInfoFromID(id))
