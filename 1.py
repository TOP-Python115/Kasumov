class FilmcardFactory:
    def create_movie(self, genre_name:str, movie_name:str):
        """Фабрика для каталога онлайн-кинотеатра"""
        f = Filmcard(genre_name, movie_name)
        return f


class Filmcard:
  
    factory = FilmcardFactory()
  
    def __init__(self, genre_name:str, movie_name:str):
        self.genre_name = genre_name
        self.movie_name = movie_name

    def __str__(self):
        """Строковое представление Фабрики"""
        return f" {self.genre_name} {self.movie_name}  "
    

print('         Catalog of movies by genre')
print()
mov1 = Filmcard.factory.create_movie('Drama:','Purple Hearts, Where are cancers sings, 13 lives')
mov2 = Filmcard.factory.create_movie('Comedy:','The Big Lebowski, The Naked Gun, GhostBusters')
mov3 = Filmcard.factory.create_movie('Horror:','Scream, Friday 13-th, Haloween')
mov4 = Filmcard.factory.create_movie('Thriller:','Shutter Island, Gone girl, Parasites')
mov5 = Filmcard.factory.create_movie('Action:','Terminator, Kill Bill, Die Hard')

print(mov1, mov2, mov3, mov4, mov5, sep = '\n')
