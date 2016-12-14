import media
import fresh_tomatoes

# Create six instances of Movie: Toy Story, Avatar, The Good the Bad and
#                                the Ugly, Apocalypse Now, The Sting,
#                                and No Country for Old Men

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys who come to life.",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # noqa
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet.",
                     "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",  # noqa
                     "http://www.youtube.com/watch?v=-9ceBgWV8io")

gbu = media.Movie("The Good, the Bad, and the Ugly",
                  "Classic western movie",
                  "http://image.tmdb.org/t/p/original/v6TUio0GgIsK9pbW7FfFArbyECb.jpg",  # noqa
                  "https://www.youtube.com/watch?v=WCN5JJY_wiA")

apocalypse_now = media.Movie("Apocalypse Now",
                             "A journey into the heart of darkness",
                             "http://cdn.traileraddict.com/content/united-artists/apocalypse_now.jpg",  # noqa
                             "https://www.youtube.com/watch?v=IkrhkUeDCdQ")

the_sting = media.Movie("The Sting",
                        "One last con job",
                        "https://s-media-cache-ak0.pinimg.com/originals/b9/42/9d/b9429df20e10920642b2abe866dd3172.jpg",  # noqa
                        "https://www.youtube.com/watch?v=_nAIb_J9T5M")

no_country = media.Movie("No Country for Old Men",
                         "Modern day western",
                         "https://images-na.ssl-images-amazon.com/images/M/MV5BMjA5Njk3MjM4OV5BMl5BanBnXkFtZTcwMTc5MTE1MQ@@._V1_UY1200_CR92,0,630,1200_AL_.jpg",  # noqa
                         "https://www.youtube.com/watch?v=38A__WT3-o0")


# Combine the movies into a list (which the open_movies_page() method requires
# as an argument) and use fresh_tomatoes.open_movies_page() to create the
# open the HTML file to display the movies

movies = [toy_story, avatar, gbu, apocalypse_now, the_sting, no_country]
fresh_tomatoes.open_movies_page(movies)
