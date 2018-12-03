# Arquivo media.py

import webbrowser


class Movie():
    def __init__(self, _title, _storyline, _image, _url):
        self.title = _title
        self.storyline = _storyline
        self.poster_image_url = _image
        self.trailer_youtube_url = _url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
