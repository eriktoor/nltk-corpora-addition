import bs4 
import requests


def getShowNames(fi, pages):
    for page in range(pages + 1):

        str_page = str(page)

        res = requests.get("https://www.springfieldspringfield.co.uk/tv_show_episode_scripts.php?page=" + str_page)

        soup = bs4.BeautifulSoup(res.text, features="html.parser")

        seen = set()

        for link in soup.find_all("a"):
            if "?tv-show=" in link['href'] and "episode_scripts" in link['href']:
                import io
                with io.open(fi, "a", encoding="utf-8") as f:
                    show = link['href'].split("?tv-show=")[1].strip()
                    if show in seen:
                        continue 
                    seen.add(show)
                    print(show)
                    # print(link)
                    f.write(show + "\n")



#print(getShowNames("tv-shows.txt", 1))
