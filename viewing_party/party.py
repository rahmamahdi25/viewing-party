# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie_dic = {}
    if title and genre and rating:
        movie_dic["title"] = title
        movie_dic["genre"] = genre
        movie_dic["rating"] = rating
        return movie_dic
    else:
        return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for i in range(len(user_data["watchlist"])):
        if isinstance(user_data, dict):
            if title == user_data["watchlist"][i]["title"]:
                user_data["watched"].append(user_data["watchlist"].pop(i))
                return user_data               

    return user_data

# ------------- WAVE 2 --------------------

def get_watched_avg_rating(user_data):
    total_ratings = 0.0

    watched = user_data.get("watched", [])
    if not watched:
        return total_ratings

    for movie in watched:
        rating = movie["rating"]
        total_ratings += rating

    avg_rating = total_ratings / len(watched)

    return avg_rating

def get_most_watched_genre(user_data):

    if not user_data["watched"]:
        return None
    
    genre_count = {}
    max_count = -1
    get_most_watched_genre = None

    for movie in user_data["watched"]:
        genre = movie["genre"]
        genre_count[genre] = genre_count.get(genre, 0) + 1

        if genre_count[genre] > max_count:
            max_count = genre_count[genre]
            get_most_watched_genre = genre

    return get_most_watched_genre

# ------------- WAVE 3 --------------------
def get_movie_titles(movies):
    titles = set()

    for movie in movies:
        titles.add(movie["title"])

    return titles

def get_unique_watched(user_data):
    user_watched = user_data.get("watched", [])
    friends = user_data.get("friends", [])

    friend_movie_titles = set()

    for friend in friends:
        friend_titles = get_movie_titles(friend["watched"])
        friend_movie_titles.update(friend_titles)

    unique_movies = []

    for movie in user_watched:
        if movie["title"] not in friend_movie_titles:
            unique_movies.append(movie)

    return unique_movies

def get_friends_unique_watched(user_data):
    user_watched = user_data.get("watched", [])
    friends = user_data.get("friends", [])

    user_movie_titles = get_movie_titles(user_watched)

    unique_movies = []
    added_titles = set()

    for friend in friends:
        friend_movies = friend["watched"]
        friend_titles = get_movie_titles(friend_movies)

        for title in friend_titles:
            if title not in user_movie_titles and title not in added_titles:
                added_titles.add(title)

                for movie in friend_movies:
                    if movie["title"] == title:
                        unique_movies.append(movie)
                        break
    return unique_movies
        
# ------------- WAVE 4 --------------------

def get_available_recs(user_data):
    recs_list = []
    for i in range(len(user_data["friends"])):
        for f in range(len(user_data["friends"][i]["watched"])):
            #print(len(user_data["friends"][i]["watched"]))
            name = user_data["friends"][i]["watched"][f]["title"]
            host = user_data["friends"][i]["watched"][f]["host"]
        
            found = False
            for j in range(len(user_data["watched"])):
                if name == user_data["watched"][j]["title"]:
                    found = True
            if not found:
                if host in user_data["subscriptions"]:
                    if user_data["friends"][i]["watched"][f] not in recs_list:
                        recs_list.append(user_data["friends"][i]["watched"][f])    
    return recs_list

# ------------- WAVE 5 --------------------
def get_all_friend_movies(user_data):
    friend_movies = []

    for friend in user_data["friends"]:
        friend_movies.extend(friend["watched"])

    return friend_movies

def get_new_rec_by_genre(user_data):
    genre = get_most_watched_genre(user_data)
    friend_movies = get_all_friend_movies(user_data)

    recommendations = []

    for movie in friend_movies:
        if movie not in user_data["watched"] and movie["genre"] == genre:
            if movie not in recommendations:
                recommendations.append(movie)

    return recommendations

def get_rec_from_favorites(user_data):
    friend_movies = get_all_friend_movies(user_data)

    recommendations = []

    for movie in user_data["favorites"]:
        if movie not in friend_movies:
            recommendations.append(movie)

    return recommendations
