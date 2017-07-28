'''
Movie Trailer Website
Udacity Nanodegree Project
Author: Sattamjh
'''


class Movie(object):
    '''This class provides a way to store movie related information '''

    def __init__(self, title, poster_image, trailer_youtube):
        self.title = title
        self.poster_image_url = poster_image    # image url
        self.trailer_youtube_url = trailer_youtube  # full URL from youtube
