from imdb_wrapper import IMDbClient

client = IMDbClient()
movie = client.fetch("tt0241527")
print(movie)
