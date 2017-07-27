'''
Purpose: Instantiate some movie objects using the Movie class,
then make a list of them to generate the movie website using "fresh_tomatoes"
'''

import media
import fresh_tomatoes

toy_story = media.Movie(
    "Toy Story",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc"
    )

avatar = media.Movie(
    "Avatar",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=d1_JBMrrYw8"
    )

the_terminal = media.Movie(
    "The Terminal",
    "https://upload.wikimedia.org/wikipedia/en/8/86/Movie_poster_the_terminal.jpg",
    "https://www.youtube.com/watch?v=GZjC9dAvWuU"
    )

school_of_rock = media.Movie(
    "School of Rock",
    "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
    "https://www.youtube.com/watch?v=3PsUJFEBC74"
    )

the_patriot = media.Movie(
    "The Patriot (2000)",
    "https://upload.wikimedia.org/wikipedia/en/6/68/Patriot_promo_poster.jpg",
    "https://www.youtube.com/watch?v=P5u1am7pmrw"
    )

the_intern = media.Movie(
    "The Intern",
    "https://upload.wikimedia.org/wikipedia/en/c/c9/The_Intern_Poster.jpg",
    "https://www.youtube.com/watch?v=R1z5q6SSH00"
    )

movies = [toy_story, the_terminal, the_patriot, the_intern, school_of_rock, avatar]

# gernerate HTML website for movie list, then open browser window
fresh_tomatoes.open_movies_page(movies)
