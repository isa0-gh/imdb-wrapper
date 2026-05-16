# imdb-wrapper

A minimal Python wrapper for the IMDb GraphQL API.

> **⚠️ Educational Purposes Only**
> This project is intended strictly for educational and personal learning purposes. Commercial or public use of IMDb data is not permitted. See [IMDb's data usage policy](https://help.imdb.com/article/imdb/general-information/can-i-use-imdb-data-in-my-software/G5JTRESSHJBBHTGX).

## Installation

```bash
pip install -e .
```

## Usage

```python
from imdb_wrapper import IMDbClient

client = IMDbClient()
movie = client.fetch("tt0241527")

print(movie.title)          # Harry Potter and the Sorcerer's Stone
print(movie.rating.score)   # 7.7
print(movie.director())     # Chris Columbus
print(movie.stars())        # ['Daniel Radcliffe', ...]
print(movie.box_office)     # BoxOffice(budget=125000000, ...)
```

## Structure

```
imdb_wrapper/
├── models.py    # dataclasses: Movie, Rating, BoxOffice, Credit, Person, AKA, ReleaseDate
├── queries.py   # GraphQL query strings
├── client.py    # IMDbClient
└── __init__.py  # public exports
```

## License

MIT — see [LICENSE](LICENSE).
