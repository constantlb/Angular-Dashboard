import requests
import time

def get_weather_light(widget):
    city = widget['params'][0]

    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&APPID=993904f621fbe867c5f374bec5dfda3a')
    json = r.json()

    if 'main' not in json or 'weather' not in json:
        temperature = 'unknown city'
        description = 'unknown city'
    else:
        temperature = int(round(json['main']['temp']))
        description = json['weather'][0]['main']

    return {
            'city': city,
            'temperature': temperature,
            'description': description
        }

def get_weather_big(widget):
    city = widget['params'][0]

    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&APPID=993904f621fbe867c5f374bec5dfda3a')
    json = r.json()

    if 'main' not in json or 'wind' not in json:
        temperature = 'unknown city'
        temperature_min = 'unknown city'
        temperature_max = 'unknown city'
        pressure = 'unknown city'
        humidity = 'unknown city'
        wind = 'unknown city'
    else:
        temperature = int(round(json['main']['temp']))
        temperature_min = int(round(json['main']['temp_min']))
        temperature_max = int(round(json['main']['temp_max']))
        pressure = int(round(json['main']['pressure']))
        humidity = int(round(json['main']['humidity']))
        wind = json['wind']['speed']

    return {
            'city': city,
            'temperature': temperature,
            'temperature_min': temperature_min,
            'temperature_max': temperature_max,
            'pressure': pressure,
            'humidity': humidity,
            'wind': wind
        }

def get_weather_day(widget):
    city = widget['params'][0]

    r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&APPID=993904f621fbe867c5f374bec5dfda3a')
    json = r.json()

    if 'sys' not in json or 'timezone' not in json:
        sunrise = 'unknown city'
        sunset = 'unknown city'
    else:
        sunrise = time.strftime('%Hh%M', time.localtime(json['sys']['sunrise'] + json['timezone']))
        sunset = time.strftime('%Hh%M', time.localtime(json['sys']['sunset'] + json['timezone']))

    return {
            'city': city,
            'sunrise': sunrise,
            'sunset': sunset
        }

def util_soundcloud_get_user(search):
    r = requests.get('https://api-v2.soundcloud.com/search/users?q=' + search + '&client_id=fnTBOUiqL776591kQ48BZ73aElSQU5Tb&limit=1&offset=0')
    json = r.json()

    if 'collection' not in json:
        return None

    users = list(json['collection'])

    if len(users) == 0:
        return None

    return users[0]

def get_soundcloud_profile(widget):
    username = widget['params'][0]

    user = util_soundcloud_get_user(username)
    if user is None:
        return {
                'user': username,
                'avatar': 'user not found',
                'link': 'https://soundcloud.com',
                'followers_count': 'user not found',
                'followings_count': 'user not found',
                'plays_count': 'user not found'
            }

    r = requests.get('https://api-v2.soundcloud.com/users/' + str(user['id']) + '/tracks?client_id=fnTBOUiqL776591kQ48BZ73aElSQU5Tb&limit=50&offset=0')
    json = r.json()

    plays_count = 0
    if 'collection' in json:
        for track in json['collection']:
            plays_count += track['playback_count']

    return {
            'user': user['username'],
            'avatar': user['avatar_url'],
            'link': user['permalink_url'],
            'followers_count': user['followers_count'],
            'followings_count': user['followings_count'],
            'plays_count': plays_count
        }

def get_soundcloud_discover(widget):
    country = widget['params'][0]
    music_genre = widget['params'][1]

    url = 'https://api-v2.soundcloud.com/charts?kind=top&high_tier_only=false&client_id=fnTBOUiqL776591kQ48BZ73aElSQU5Tb&limit=15'

    if country == 'Australia':
        url += '&region=soundcloud:regions:AU'
    if country == 'Canada':
        url += '&region=soundcloud:regions:CA'
    if country == 'France':
        url += '&region=soundcloud:regions:FR'
    if country == 'Germany':
        url += '&region=soundcloud:regions:DE'
    if country == 'Ireland':
        url += '&region=soundcloud:regions:IE'
    if country == 'Netherlands':
        url += '&region=soundcloud:regions:NL'
    if country == 'New Zealand':
        url += '&region=soundcloud:regions:NZ'
    if country == 'United Kingdom':
        url += '&region=soundcloud:regions:GB'
    if country == 'USA':
        url += '&region=soundcloud:regions:US'

    if music_genre == 'All music genres':
        url += '&genre=soundcloud:genres:all-music'
    if music_genre == 'Alternative Rock':
        url += '&genre=soundcloud:genres:alternativerock'
    if music_genre == 'Ambient':
        url += '&genre=soundcloud:genres:ambient'
    if music_genre == 'Classical':
        url += '&genre=soundcloud:genres:classical'
    if music_genre == 'Country':
        url += '&genre=soundcloud:genres:country'
    if music_genre == 'Dance & EDM':
        url += '&genre=soundcloud:genres:danceedm'
    if music_genre == 'Dancehall':
        url += '&genre=soundcloud:genres:dancehall'
    if music_genre == 'Deep House':
        url += '&genre=soundcloud:genres:deephouse'
    if music_genre == 'Disco':
        url += '&genre=soundcloud:genres:disco'
    if music_genre == 'Drum & Bass':
        url += '&genre=soundcloud:genres:drumbass'
    if music_genre == 'Dubstep':
        url += '&genre=soundcloud:genres:dubstep'
    if music_genre == 'Electronic':
        url += '&genre=soundcloud:genres:electronic'
    if music_genre == 'Folk & Singer-Songwriter':
        url += '&genre=soundcloud:genres:folksingersongwriter'
    if music_genre == 'Hip-hop & Rap':
        url += '&genre=soundcloud:genres:hiphoprap'
    if music_genre == 'House':
        url += '&genre=soundcloud:genres:house'
    if music_genre == 'Indie':
        url += '&genre=soundcloud:genres:indie'
    if music_genre == 'Jazz & Blues':
        url += '&genre=soundcloud:genres:jazzblues'
    if music_genre == 'Latin':
        url += '&genre=soundcloud:genres:latin'
    if music_genre == 'Metal':
        url += '&genre=soundcloud:genres:metal'
    if music_genre == 'Piano':
        url += '&genre=soundcloud:genres:piano'
    if music_genre == 'Pop':
        url += '&genre=soundcloud:genres:pop'
    if music_genre == 'R&B & Soul':
        url += '&genre=soundcloud:genres:rbsoul'
    if music_genre == 'Reggae':
        url += '&genre=soundcloud:genres:reggae'
    if music_genre == 'Reggaeton':
        url += '&genre=soundcloud:genres:reggaeton'
    if music_genre == 'Rock':
        url += '&genre=soundcloud:genres:rock'
    if music_genre == 'Soundtrack':
        url += '&genre=soundcloud:genres:soundtrack'
    if music_genre == 'Techno':
        url += '&genre=soundcloud:genres:techno'
    if music_genre == 'Trance':
        url += '&genre=soundcloud:genres:trance'
    if music_genre == 'Trap':
        url += '&genre=soundcloud:genres:trap'
    if music_genre == 'Trihop':
        url += '&genre=soundcloud:genres:triphop'
    if music_genre == 'World':
        url += '&genre=soundcloud:genres:world'

    r = requests.get(url)
    json = r.json()

    if 'collection' not in json:
        return {
                'country': country,
                'music_genre': music_genre,
                'tracks': [{
                    'title': 'invalid country or music genre',
                    'artwork': 'https://i1.sndcdn.com/avatars-000125177592-9vuquh-t500x500.jpg',
                    'link': 'https://soundcloud.com',
                    'week_plays_count': 'invalid country or music genre',
                    'author': 'invalid country or music genre'
                }]
            }

    tracks = []
    for track in json['collection']:
        tracks.append({
            'title': track['track']['title'],
            'artwork': track['track']['artwork_url'],
            'link': track['track']['permalink_url'],
            'week_plays_count': track['score'],
            'author': track['track']['user']['username']
        })

    return {
            'country': country,
            'music_genre': music_genre,
            'tracks': tracks
        }

def get_soundcloud_top(widget):
    username = widget['params'][0]

    user = util_soundcloud_get_user(username)
    if user is None:
        return {
                'user': username,
                'tracks': [{
                    'title': 'user not found',
                    'link': 'https://soundcloud.com'
                }]
            }

    r = requests.get('https://api-v2.soundcloud.com/users/' + str(user['id']) + '/toptracks?client_id=fnTBOUiqL776591kQ48BZ73aElSQU5Tb')
    json = r.json()

    if 'collection' not in json:
        return {
                'user': username,
                'tracks': [{
                    'title': 'user not found',
                    'link': 'https://soundcloud.com'
                }]
            }

    tracks = []
    for track in json['collection']:
        tracks.append({
            'title': track['title'],
            'link': track['permalink_url']
        })

    return {
            'user': user['username'],
            'tracks': tracks
        }

def get_news_subject(widget):
    search = widget['params'][0]
    date = time.strftime('%Y-%m-%d', time.localtime())

    r = requests.get('https://newsapi.org/v2/everything?q=' + search + '&from=' + date + '&language=en&sortBy=relevancy&apiKey=ff3465630b86437bbae04d5e6853566f')
    json = r.json()

    if 'status' not in json or 'articles' not in json:
        return {
                'search': search,
                'date': date,
                'articles': []
            }

    articles = []
    for article in json['articles']:
        if article['description'] is None:
            desciption = 'No description'
        else:
            description = article['description']

        if article['author'] is None:
            author = 'unknown author'
        else:
            author = article['author']

        if article['source']['name'] is None:
            source = 'unknown source'
        else:
            source = article['source']['name']

        if article['urlToImage'] is None:
            image = 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.QE_3I_EOdGQlg4rgV4ZkVQAAAA%26pid%3DApi&f=1'
        else:
            image = article['urlToImage']

        articles.append({
            'title': article['title'],
            'description': description,
            'author': author,
            'source': source,
            'date': article['publishedAt'],
            'url': article['url'],
            'image': image
        })

    return {
            'search': search,
            'date': date,
            'articles': articles
        }

def get_news_region(widget):
    country = widget['params'][0]
    category = widget['params'][1]

    url = 'https://newsapi.org/v2/top-headlines?language=en&sortBy=relevancy&apiKey=ff3465630b86437bbae04d5e6853566f'

    if country == 'United Arab Emirates':
        url += '&country=ae'
    if country == 'Argentina':
        url += '&country=ar'
    if country == 'Austria':
        url += '&country=at'
    if country == 'Australia':
        url += '&country=au'
    if country == 'Belgium':
        url += '&country=be'
    if country == 'Bulgaria':
        url += '&country=bg'
    if country == 'Brazil':
        url += '&country=br'
    if country == 'Canada':
        url += '&country=ca'
    if country == 'Switzerland':
        url += '&country=ch'
    if country == 'China':
        url += '&country=cn'
    if country == 'Colombia':
        url += '&country=co'
    if country == 'Cuba':
        url += '&country=cu'
    if country == 'Czechia':
        url += '&country=cz'
    if country == 'Germany':
        url += '&country=de'
    if country == 'Egypt':
        url += '&country=eg'
    if country == 'France':
        url += '&country=fr'
    if country == 'United Kingdom':
        url += '&country=gb'
    if country == 'Greece':
        url += '&country=gr'
    if country == 'Hong Kong':
        url += '&country=hk'
    if country == 'Hungary':
        url += '&country=hu'
    if country == 'Indonesia':
        url += '&country=id'
    if country == 'Ireland':
        url += '&country=ie'
    if country == 'Israel':
        url += '&country=il'
    if country == 'India':
        url += '&country=in'
    if country == 'Italy':
        url += '&country=it'
    if country == 'Japan':
        url += '&country=jp'
    if country == 'Korea':
        url += '&country=kr'
    if country == 'Lithuania':
        url += '&country=lt'
    if country == 'Latvia':
        url += '&country=lv'
    if country == 'Morocco':
        url += '&country=ma'
    if country == 'Mexico':
        url += '&country=mx'
    if country == 'Malaysia':
        url += '&country=my'
    if country == 'Nigeria':
        url += '&country=ng'
    if country == 'Netherlands':
        url += '&country=nl'
    if country == 'Norway':
        url += '&country=no'
    if country == 'New Zealand':
        url += '&country=nz'
    if country == 'Philippines':
        url += '&country=ph'
    if country == 'Poland':
        url += '&country=pl'
    if country == 'Portugal':
        url += '&country=pt'
    if country == 'Romania':
        url += '&country=ro'
    if country == 'Serbia':
        url += '&country=rs'
    if country == 'Russia':
        url += '&country=ru'
    if country == 'Saudi Arabia':
        url += '&country=sa'
    if country == 'Sweden':
        url += '&country=se'
    if country == 'Slovenia':
        url += '&country=si'
    if country == 'Slovakia':
        url += '&country=sk'
    if country == 'Thailand':
        url += '&country=th'
    if country == 'Turkey':
        url += '&country=tr'
    if country == 'Taiwan':
        url += '&country=tw'
    if country == 'Ukraine':
        url += '&country=ua'
    if country == 'United States':
        url += '&country=us'
    if country == 'Venezuela':
        url += '&country=ve'
    if country == 'South Africa':
        url += '&country=za'

    if category == 'Business':
        url += '&category=business'
    if category == 'Entertainment':
        url += '&category=entertainment'
    if category == 'General':
        url += '&category=general'
    if category == 'Health':
        url += '&category=health'
    if category == 'Science':
        url += '&category=science'
    if category == 'Sports':
        url += '&category=sports'
    if category == 'Technology':
        url += '&category=technology'

    r = requests.get(url)
    json = r.json()

    if 'articles' not in json:
        return {
                'country': country,
                'category': category,
                'articles': []
            }

    articles = []
    for article in json['articles']:
        if article['description'] is None:
            description = 'No description'
        else:
            description = article['description']

        if article['author'] is None:
            author = 'unknown author'
        else:
            author = article['author']

        if article['source']['name'] is None:
            source = 'unknown source'
        else:
            source = article['source']['name']

        if article['urlToImage'] is None:
            image = 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.QE_3I_EOdGQlg4rgV4ZkVQAAAA%26pid%3DApi&f=1'
        else:
            image = article['urlToImage']

        articles.append({
            'title': article['title'],
            'description': description,
            'author': author,
            'source': source,
            'date': article['publishedAt'],
            'url': article['url'],
            'image': image
        })

    return {
            'country': country,
            'category': category,
            'articles': articles
        }

def get_news_media(widget):
    source = widget['params'][0]

    url = 'https://newsapi.org/v2/top-headlines?apiKey=ff3465630b86437bbae04d5e6853566f'

    if source == 'ABC News':
        url += '&sources=abc-news'
    if source == 'Al Jazeera English':
        url += '&sources=al-jazeera-english'
    if source == 'BBC News':
        url += '&sources=bbc-news'
    if source == 'BBC Sport':
        url += '&sources=bbc-sport'
    if source == 'Bloomberg':
        url += '&sources=bloomberg'
    if source == 'Business Insider':
        url += '&sources=business-insider'
    if source == 'Buzzfeed':
        url += '&sources=buzzfeed'
    if source == 'CBS News':
        url += '&sources=cbs-news'
    if source == 'CNN':
        url += '&sources=cnn'
    if source == 'Engadget':
        url += '&sources=engadget'
    if source == 'Entertainment Weekly':
        url += '&sources=entertainment-weekly'
    if source == 'ESPN':
        url += '&sources=espn'
    if source == 'Fox News':
        url += '&sources=fox-news'
    if source == 'Hacker News':
        url += '&sources=hacker-news'
    if source == 'IGN':
        url += '&sources=ign'
    if source == 'Mashable':
        url += '&sources=mashable'
    if source == 'National Geographic':
        url += '&sources=national-geographic'
    if source == 'Reddit':
        url += '&sources=reddit-r-all'
    if source == 'TechCrunch':
        url += '&sources=techcrunch'
    if source == 'The Huffington Post':
        url += '&sources=the-huffington-post'
    if source == 'The New York Times':
        url += '&sources=the-new-york-times'
    if source == 'The Verge':
        url += '&sources=the-verge'
    if source == 'The Wall Street Journal':
        url += '&sources=the-wall-street-journal'
    if source == 'Wired':
        url += '&sources=wired'

    r = requests.get(url)
    json = r.json()

    if 'articles' not in json:
        return {
                'source': source,
                'articles': []
            }

    articles = []
    for article in json['articles']:
        if article['description'] is None:
            desciption = 'No description'
        else:
            description = article['description']

        if article['author'] is None:
            author = 'unknown author'
        else:
            author = article['author']

        if article['urlToImage'] is None:
            image = 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.QE_3I_EOdGQlg4rgV4ZkVQAAAA%26pid%3DApi&f=1'
        else:
            image = article['urlToImage']

        articles.append({
            'title': article['title'],
            'description': description,
            'author': author,
            'date': article['publishedAt'],
            'url': article['url'],
            'image': image
        })

    return {
            'source': source,
            'articles': articles
        }

def get_data(widget):
    if 'type' not in widget:
        return None

    if widget['type'] == 'widget-weather-light':
        return get_weather_light(widget)
    if widget['type'] == 'widget-weather-big':
        return get_weather_big(widget)
    if widget['type'] == 'widget-weather-day':
        return get_weather_day(widget)
    if widget['type'] == 'widget-soundcloud-profile':
        return get_soundcloud_profile(widget)
    if widget['type'] == 'widget-soundcloud-discover':
        return get_soundcloud_discover(widget)
    if widget['type'] == 'widget-soundcloud-top':
        return get_soundcloud_top(widget)
    if widget['type'] == 'widget-news-subject':
        return get_news_subject(widget)
    if widget['type'] == 'widget-news-region':
        return get_news_region(widget)
    if widget['type'] == 'widget-news-media':
        return get_news_media(widget)

    return None
