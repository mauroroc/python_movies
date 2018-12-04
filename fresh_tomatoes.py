import webbrowser
import os
import re


# Todos os Estilos
# Scripts para janela modal do trailer
# Inicio do body tambem esta aqui
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Coming Soon in December - Mauro - Udacity</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet"
          href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet"
          href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script
        src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js">
    </script>
    <style type="text/css" media="screen">
        body {
  background: #333;
  padding: 70px 0;
  font: 15px/20px Arial, sans-serif;
}

.container {
  margin: 0 auto;
  width: 250px;
  height: 200px;
  position: relative;
  perspective: 1000px;
}

.carousel {
  height: 100%;
  width: 100%;
  position: absolute;
  transform-style: preserve-3d;
  transition: transform 1s;
}

.item {
  display: block;
  position: absolute;
  background: #000;
  width: 250px;
  height: 200px;
  line-height: 200px;
  font-size: 5em;
  text-align: center;
  color: #FFF;
  opacity: 0.95;
  border-radius: 10px;
}

.a {
  transform: rotateY(0deg) translateZ(250px);
  background: #ed1c24;
}
.b {
  transform: rotateY(60deg) translateZ(250px);
  background: #0072bc;
}
.c {
  transform: rotateY(120deg) translateZ(250px);
  background: #39b54a;
}
.d {
  transform: rotateY(180deg) translateZ(250px);
  background: #f26522;
}
.e {
  transform: rotateY(240deg) translateZ(250px);
  background: #630460;
}
.f {
  transform: rotateY(300deg) translateZ(250px);
  background: #8c6239;
}

.next, .prev {
  color: #444;
  position: absolute;
  top: 100px;
  padding: 1em 2em;
  cursor: pointer;
  background: #CCC;
  border-radius: 5px;
  border-top: 1px solid #FFF;
  box-shadow: 0 5px 0 #999;
  transition: box-shadow 0.1s, top 0.1s;
}
.next:hover, .prev:hover { color: #000; }
.next:active, .prev:active {
  top: 104px;
  box-shadow: 0 1px 0 #999;
}
.next { right: 5em; }
.prev { left: 5em; }

#trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed,
            //as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + 
                            trailerYouTubeId +
                            '?autoplay=1&html5=1';
            $("#trailer-video-container")
            .empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
<body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal"
          aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

'''


# Parte central que carrega o carrousel com os filmes dinamicamente
main_page_content = '''
    <div class="container">
  <div class="carousel" >
      {movie_tiles}
  </div>
</div>
<div class="next">Next</div>
<div class="prev">Prev</div>
    </div>
'''

# Scripts que fazem o carrousel funcionar
# Se colocados dentro da tag Head, nao funciona
scripts = '''
    <script src='https://static.codepen.io/assets/common/stopExecutionOnTimeout-b2a7b3fe212eaa732349046d8416e00a9dec26eb7fd347590fbced3ab38af52e.js'></script>
    <script src='https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'></script>
    <script type="text/javascript" charset="utf-8">
      var carousel = $(".carousel"),
  currdeg  = 0;

$(".next").on("click", { d: "n" }, rotate);
$(".prev").on("click", { d: "p" }, rotate);

function rotate(e){
if(e.data.d=="n"){
  currdeg = currdeg - 60;
}
if(e.data.d=="p"){
  currdeg = currdeg + 60;
}
carousel.css({
  "-webkit-transform": "rotateY("+currdeg+"deg)",
  "-moz-transform": "rotateY("+currdeg+"deg)",
  "-o-transform": "rotateY("+currdeg+"deg)",
  "transform": "rotateY("+currdeg+"deg)"
});
}
  </script>
  </body>
</html>
'''


# Codigo que monta a chamada para preencher o carrousel e
# ativar a janela modal do trailer
movie_tile_content = '''
<div class="item {x} movie-tile" data-trailer-youtube-id="{trailer_youtube_id}"
     data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" alt="{movie_title}" width="220" height="342">
    <h2>{movie_title}</h2>
</div>
'''


def create_movie_tiles_content(movies):
    # Codigo que faz a substituicao dinamica do conteudo de cada filme
    content = ''
    # lista com as letras referentes a posicao de cada filme
    x = 0
    letter = ['a', 'b', 'c', 'd', 'e', 'f']
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            movie_storyline=movie.storyline,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            x=letter[x]
        )
        x = x + 1
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content + scripts)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)