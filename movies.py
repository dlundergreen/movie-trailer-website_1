#Classes used:
import fresh_tomatoes
import media

#This part initializes the movie objects
#See media.py for more details
gatsby = media.Movie(
    "The Great Gatsby",
    "Be careful of a significant other who will only marry you if you are rich.",
    "http://upload.wikimedia.org/wikipedia/en/2/26/TheGreatGatsby2012Poster.jpg",
    "https://www.youtube.com/watch?v=rARN6agiW7o"
    )

the_wolf_of_wall_st=media.Movie(
    "The Wolf of Wall Street",
    "Exaclty the wrong way and reason to be wealthy",
    "http://upload.wikimedia.org/wikipedia/en/thumb/1/1f/WallStreet2013poster.jpg/220px-WallStreet2013poster.jpg",
    "https://www.youtube.com/watch?v=iszwuX1AK6A"
    )

avatar = media.Movie(
    "Avatar",
    "To be honest, I have never seen this movie.",
    "http://www.dvdsreleasedates.com/covers/avatar-dvd-cover-67.jpg",
    "http://www.youtube.com/watch?v=cRdxXPV9GNQ"
    )

interstellar = media.Movie(
    "Interstellar",
    "A movie that will make you wish you became an astronaut like your five year old self dreamed.",
    "http://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
    "https://www.youtube.com/watch?v=0vxOhd4qlnA"
    )

home_tonight = media.Movie(
    "Take Me Home Tonight",
    "A movie about being lost after graduating from college.",
    "http://upload.wikimedia.org/wikipedia/en/c/cf/Take_Me_Home_Tonight_Poster.jpg",
    "https://www.youtube.com/watch?v=ZsSNCmGUK2I"
    )

orgy = media.Movie(
    "A Good Old Fashioned Orgy",
    "This movie is not what you are thinking it is.  Watch it, its awesome.",
    "http://goodfilmguide.co.uk/wp-content/uploads/2011/08/A-Good-Old-Fashioned-Orgy-Poster.jpg",
    "https://www.youtube.com/watch?v=89xzifrMTWE"
    )

#This creates an of the Movies for the fresh_tomatoes.open_movies_page() to open
#Put the Movie() objects you would like to display here.
movies = [
    gatsby, interstellar,
    orgy, the_wolf_of_wall_st,
    home_tonight, avatar]

#this is the function that will create the webpage
#see fresh_tomatoes.py for more information.
fresh_tomatoes.open_movies_page(movies)
