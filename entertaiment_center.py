# Arquivo entertaiment_center.py
import media
import fresh_tomatoes
import tmdbsimple as tmdb


# Chave para acesso a API do TMDBSimple
# Antiga - tmdb.API_KEY = 'ae221525f59fff4f079bf164de77fa34'
tmdb.API_KEY = 'f3da2aee3c21c6eb05f8e3fbaae64f01'

def getInfo(id_imdb):
    # Cria um objeto do tipo Movies da classe TMDB recebendo o id do filme no
    # IMDB
    movie = tmdb.Movies(id_imdb)
    response = movie.info()
    return movie


def getTrailer(id_imdb):
    # Retorna uma string com o codigo do trailer no Youtube recebendo o id do
    #  filme no IMDB
    kwargs = {'append_to_response': 'trailers'}
    movie = tmdb.Movies(id_imdb).info(**kwargs)
    return movie.get('trailers')['youtube'][0]['source']

# Carrega o codigo no IMDB de 6 filmes que vao estreiar em decembro
comingSoon = ['tt5463162', 'tt7959026', 'tt1477834',
              'tt1255919', 'tt2126357', 'tt4701182']

# Cria um dictionary com objetos do tipo media.Movie recebendo como parametro
# o codigo deles no IMDB
movies = []
for x in range(len(comingSoon)):
    image_path = 'https://image.tmdb.org/t/p/w500'
    video_path = 'https://www.youtube.com/watch?v='
    movies.append(
        media.Movie(
            getInfo(comingSoon[x]).title,
            getInfo(comingSoon[x]).overview,
            image_path + getInfo(comingSoon[x]).poster_path,
            video_path + getTrailer(comingSoon[x])
        )
    )

# Chamada para montar dinamicamente a pagina
fresh_tomatoes.open_movies_page(movies)