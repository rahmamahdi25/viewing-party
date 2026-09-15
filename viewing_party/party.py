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
                #print(user_data)
        else:
            if title == user_data["watchlist"][i]:
                user_data["watchlist"].remove("title")
                user_data["watched"].append("title")
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

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

