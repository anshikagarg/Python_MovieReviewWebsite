class Movie():
    """This class helps define the Model for Movie.
       Movie class has 4 values which define the
       name of the movie(title), the description of
       the movie, it provides a image of the poster &
       a youtube link to the trailer."""

    def __init__(self, movie_title, movie_description,
                 movie_poster, movie_trailer):
                self.title = movie_title
                self.description = movie_description
                self.poster = movie_poster
                self.trailer = movie_trailer
