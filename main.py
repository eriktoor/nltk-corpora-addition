import ShowNames
import ScrapeShow
import ShowInfo

def main():

    f = "tv-shows.txt" #file name that ShowNames will write all of the show names to
    pages = 284

    count = 0 
    for line in open(f, 'r'): 
        count += 1 
        if count > 20: break 

    if count < 20: 
        print("running again")
        ShowNames.getShowNames(f, pages)

    showNames = open(f, 'r') 

    scrapedShows = set()
    scrapedShows.add("the-simpsons")

    for line in showNames:

        showID = line.strip() #each line will be a showID 

        if showID in scrapedShows: #if we have seen the show before then skip this iteration 
            print("skipping...")
            continue 

        scrapedShows.add(showID) #add to the seen set 

        info = ShowInfo.getInfoFromID(showID) #will return an array of tuples with (seasonNo, episodes) for each season
        ''' 
        Ex info arr  ShowInfo.getInfoFromID("shameless-us") --> [(1, 12), (2, 12), (3, 12), (4, 12), (5, 12), (6, 12), (7, 12), (8, 12), (9, 14), (10, 8)]
        '''

        for season, episodes in info: 
            try: 
                ScrapeShow.scrapeSeasonOfShow(showID, season, episodes) #scrapes show and appends to corpus file 
            finally: 
                print("Completed...")
            '''
            Example corpus file
            corpora/shameless-us_s01e01
            '''


if __name__ == "__main__":
    main()
