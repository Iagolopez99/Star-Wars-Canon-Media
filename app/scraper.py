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
    ctimeline['Title'] = ctimeline['Title'].apply(lambda x: x.split('Flashback')[0].strip() if 'Flashback' in x else x)
    ctimeline['Title'] = ctimeline['Title'].apply(lambda x: x.split('flashback')[0].strip() if 'flashback' in x else x)
    ctimeline['Title'] = ctimeline['Title'].apply(lambda x: x.split('Prologue')[0].strip() if 'Prologue' in x else x)
    ctimeline['Title'] = ctimeline['Title'].apply(lambda x: x.split('Epilogue')[0].strip() if 'Epilogue' in x else x)
    ctimeline['Title'] = ctimeline['Title'].apply(lambda x: x.split('Occurs')[0].strip() if 'Occurs' in x else x)
    ctimeline['Title'] = ctimeline['Title'].apply(lambda x: x.split('Opening')[0].strip() if 'Opening' in x else x)
    ctimeline['Title'] = ctimeline['Title'].apply(lambda x: x.split('Prelude')[0].strip() if 'Prelude' in x else x)
    ctimeline['Title'] = ctimeline['Title'].apply(lambda x: x.split('Late game')[0].strip() if 'Late game' in x else x)
    ctimeline['Title'] = ctimeline['Title'].apply(lambda x: x.split('Frame story')[0].strip() if 'Frame story' in x else x)
    ctimeline['Title'] = ctimeline['Title'].apply(lambda x: x.split('First two')[0].strip() if 'First two' in x else x)
    ctimeline['Title'] = ctimeline['Title'].apply(lambda x: x.split('Graphic novelization')[0].strip() if 'Graphic novelization' in x else x)
    ctimeline['Title'] = ctimeline['Title'].apply(lambda x: x.split('Video game adaptation')[0].strip() if 'Video game adaptation' in x else x)
    ctimeline['Title'] = ctimeline['Title'].apply(lambda x: x.split('Video game partial adaptation')[0].strip() if 'Video game partial adaptation' in x else x)
    ctimeline['Title'] = ctimeline['Title'].apply(lambda x: x.split('Partial adaptation')[0].strip() if 'Partial adaptation' in x else x)
    ctimeline['Title'] = ctimeline['Title'].apply(lambda x: x.split('Comic adaptation')[0].strip() if 'Comic adaptation' in x else x)
    ctimeline['Title'] = ctimeline['Title'].apply(lambda x: x.split('Web series adaptation')[0].strip() if 'Web series adaptation' in x else x)
    ctimeline['Title'] = ctimeline['Title'].apply(lambda x: x.split('Webcomic adaptation')[0].strip() if 'Webcomic adaptation' in x else x)
    ctimeline['Title'] = ctimeline['Title'].apply(lambda x: x.split('Chapter book adaptation')[0].strip() if 'Chapter book adaptation' in x else x)
    ctimeline['Title'] = ctimeline['Title'].apply(lambda x: x.split('Young readers adaptation')[0].strip() if 'Young readers adaptation' in x else x)
    ctimeline['Title'] = ctimeline['Title'].apply(lambda x: x.split('Junior novel adaptation')[0].strip() if 'Junior novel adaptation' in x else x)
    ctimeline['Title'] = ctimeline['Title'].apply(lambda x: x.split('Manga adaptation')[0].strip() if 'Manga adaptation' in x else x)
    ctimeline['Title'] = ctimeline['Title'].apply(lambda x: x.split('Adaptation of')[0].strip() if 'Adaptation of' in x else x)
    ctimeline['Title'] = ctimeline['Title'].apply(lambda x: x.split('Partial comic adaptation')[0].strip() if 'Partial comic adaptation' in x else x)
    ctimeline['Title'] = ctimeline['Title'].apply(lambda x: x.split('Junior novelization')[0].strip() if 'Junior novelization' in x else x)
    ctimeline['Title'] = ctimeline['Title'].apply(lambda x: x.split('French')[0].strip() if 'French' in x else x)
    ctimeline['Title'] = ctimeline['Title'].apply(lambda x: x.split('Novelization')[0].strip() if 'Novelization' in x else x)
    ctimeline['Title'] = ctimeline['Title'].apply(lambda x: x.split('[')[0].strip() if '[' in x else x)
    ctimeline['Title'] = ctimeline['Title'].apply(lambda x: x.split('Alternating')[0].strip() if 'Alternating' in x else x)
    ctimeline['Title'] = ctimeline['Title'].apply(lambda x: x.split('Main')[0].strip() if 'Main' in x else x)
    ctimeline['Title'] = ctimeline['Title'].apply(lambda x: x.split('Concurrent')[0].strip() if 'Concurrent' in x else x)

    #ctimeline['Consumed'] = False

    ctimeline.to_csv('data/all_media.csv')

    
if __name__ == "__main__":
    scrape_data()

#print(ctimeline)


