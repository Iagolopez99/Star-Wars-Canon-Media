import pandas as pd

def scrape_data():

    url = "https://starwars.fandom.com/wiki/Timeline_of_canon_media"

    ctimeline = pd.read_html(url, parse_dates=True)
    ctimeline = ctimeline[2]
    ctimeline.rename(columns={'Unnamed: 1':'Media'}, inplace=True)
    #ctimeline = ctimeline.loc[(ctimeline.Media!="P") & (ctimeline.Media!="TV") & (ctimeline.Media!="SS") & (ctimeline.Media!="JR") & (ctimeline.Media!="YR") & (ctimeline.Media!="VG")]
    ctimeline = ctimeline.loc[(ctimeline.Media!="P") & (ctimeline.Media!="SS") & (ctimeline.Media!="YR")]
    ctimeline = ctimeline.reset_index(drop=True)
    ctimeline['Released'] = ctimeline['Released'].fillna('Uknown')
    ctimeline['Year'] = ctimeline['Year'].str.replace(r'\[.*?\]', '', regex=True)
    ctimeline['Year'] = ctimeline['Year'].str.replace(r'c\. ', '', regex=True)
    ctimeline['Title'] = ctimeline['Title'].str.replace(r'†', '', regex=True)
    #ctimeline['Consumed'] = False

    ctimeline.to_csv('data/all_media.csv')

    
if __name__ == "__main__":
    scrape_data()

#print(ctimeline)


