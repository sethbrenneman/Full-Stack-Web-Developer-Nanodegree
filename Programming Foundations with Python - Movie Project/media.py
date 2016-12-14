import webbrowser


class Movie():
    """ This class provides a way to store movie related information:
        Movie Title
        A brief storyline summary
        A poster image, stored as a URL link
        A youtube trailer, stored as a URL link
    """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    # Constructor
    def __init__(self, movie_title, movie_storyline,
                 movie_poster_image_url, movie_trailer_youtube_url):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_image_url
        self.trailer_youtube_url = movie_trailer_youtube_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
