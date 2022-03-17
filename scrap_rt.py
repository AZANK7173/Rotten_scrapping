from bs4 import BeautifulSoup
import requests
import pandas as pd

def get_main_page(link):

    source=requests.get(link).text 
    soup=BeautifulSoup(source,'html.parser')
    title = soup.find_all('h2',class_="panel-heading")[0].text

    return soup,title


def get_all_movies_table(soup):

    table = soup.find_all('table',class_='table')[0]

    return table.find_all('tr')[1:]


def get_basic_movie_data(movie):

    score = movie.find('span',class_='tMeterScore').text
    score = int(score.strip().strip('%'))
    title = movie.a.text.strip()
    href = movie.a['href']
    link = 'https://www.rottentomatoes.com' + href

    return title, score, link


def get_specific_movie_data(link):

    source = requests.get(link).text
    soup = BeautifulSoup(source,'html.parser')

    if len(soup.findAll("div", {"id": "movieSynopsis"})) > 0:
        sinop = soup.findAll("div", {"id": "movieSynopsis"})[0].text.strip()
    else:
        sinop = None

    if len(soup.find_all('time')) > 0:
        duration = soup.find_all('time')[-1].text.strip()
    else:
        duration = None

    return sinop, duration


def get_dataframe(link='https://www.rottentomatoes.com/top/bestofrt/?year=2019'):

    soup, title = get_main_page(link)
    movies = get_all_movies_table(soup)
    df = pd.DataFrame()

    for movie in movies:    

        title, score, link = get_basic_movie_data(movie)
        sinop, duration = get_specific_movie_data(link)

        data_dict = {'Title': title, 'Score': score, 
            'Synopses': sinop, 'Duration': duration, 'Link': link}

        df = df.append(data_dict, ignore_index=True)
        
    return df 


if __name__ == '__main__':

    df = get_dataframe('https://www.rottentomatoes.com/top/bestofrt/?year=1950')
        
    
    