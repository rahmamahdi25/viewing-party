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

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

