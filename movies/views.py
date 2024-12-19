import re
import json

from django.http import HttpResponse, JsonResponse
from django.template import loader

def index(request):
    template = loader.get_template("movies/index.html")
    context = {}
    return HttpResponse(template.render(context, request))

def details(request, imdbID):
    template = loader.get_template("movies/details.html")
    db = [{
        "Title": "Blade Runner",
        "Year": "1982",
        "Rated": "R",
        "Released": "25 Jun 1982",
        "Runtime": "117 min",
        "Genre": "Sci-Fi, Thriller",
        "Director": "Ridley Scott",
        "Writer": "Hampton Fancher (screenplay), David Webb Peoples (screenplay), Philip K. Dick (novel)",
        "Actors": "Harrison Ford, Rutger Hauer, Sean Young, Edward James Olmos",
        "Plot": "A blade runner must pursue and terminate four replicants who stole a ship in space, and have returned to Earth to find their creator.",
        "Language": "English, German, Cantonese, Japanese, Hungarian, Arabic",
        "Country": "USA",
        "Awards": "Nominated for 2 Oscars. Another 11 wins & 16 nominations.",
        "Poster": "https://m.media-amazon.com/images/M/MV5BNzQzMzJhZTEtOWM4NS00MTdhLTg0YjgtMjM4MDRkZjUwZDBlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SX300.jpg",
        "Ratings": [
            {
            "Source": "Internet Movie Database",
            "Value": "8.2/10"
            },
            {
            "Source": "Rotten Tomatoes",
            "Value": "90%"
            },
            {
            "Source": "Metacritic",
            "Value": "89/100"
            }
        ],
        "Metascore": "89",
        "imdbRating": "8.2",
        "imdbVotes": "633,160",
        "imdbID": "tt0083658",
        "Type": "movie",
        "DVD": "27 Aug 1997",
        "BoxOffice": "N/A",
        "Production": "Warner Bros. Pictures",
        "Website": "https://www.warnerbros.com/blade-runner",
        "Response": "True"
    }]

    matches = list(filter(lambda movie: movie['imdbID'] == imdbID, db))
    print("matches")
    print(matches[0])

    return HttpResponse(template.render({ "details": matches[0] }, request))

def search(request, query):
    regex = re.compile(query, re.IGNORECASE)
    db = [
        {
                  "Title": "Blade Runner",
                  "Year": "1982",
                  "imdbID": "tt0083658",
                  "Type": "movie",
                  "Poster": "https://m.media-amazon.com/images/M/MV5BNzQzMzJhZTEtOWM4NS00MTdhLTg0YjgtMjM4MDRkZjUwZDBlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SX300.jpg"
                },
        {
                  "Title": "Blade Runner 2049",
                  "Year": "2017",
                  "imdbID": "tt1856101",
                  "Type": "movie",
                  "Poster": "https://m.media-amazon.com/images/M/MV5BNzA1Njg4NzYxOV5BMl5BanBnXkFtZTgwODk5NjU3MzI@._V1_SX300.jpg"
                },
        {
                  "Title": "Blade Runner: Black Out 2022",
                  "Year": "2017",
                  "imdbID": "tt7428594",
                  "Type": "movie",
                  "Poster": "https://m.media-amazon.com/images/M/MV5BZGNiNmNiMTctMDI4OS00OWYxLWE4ZWEtZjFkZjU4ZmY5YzEyXkEyXkFqcGdeQXVyMzgxODM4NjM@._V1_SX300.jpg"
                },
        {
                  "Title": "Dangerous Days: Making Blade Runner",
                  "Year": "2007",
                  "imdbID": "tt1080585",
                  "Type": "movie",
                  "Poster": "https://m.media-amazon.com/images/M/MV5BNzI2NjU0MjY4MF5BMl5BanBnXkFtZTgwMjM0NDQzNjE@._V1_SX300.jpg"
                },
        {
                  "Title": "Blade Runner",
                  "Year": "1997",
                  "imdbID": "tt0126817",
                  "Type": "game",
                  "Poster": "https://m.media-amazon.com/images/M/MV5BYWRkYjczZWMtN2Q5NS00YWFmLTk3M2MtNWUwNWRjYzdkMjZhXkEyXkFqcGdeQXVyNjExODE1MDc@._V1_SX300.jpg"
                },
        {
                  "Title": "Oscar Pistorius: Blade Runner Killer",
                  "Year": "2017",
                  "imdbID": "tt7445510",
                  "Type": "movie",
                  "Poster": "https://m.media-amazon.com/images/M/MV5BZTYxZjU5YTgtN2NmOC00NmQ0LTk4MmEtYjc0YmI5MTI0ZDFhXkEyXkFqcGdeQXVyNTMzNDY2NzU@._V1_SX300.jpg"
                },
        {
                  "Title": "On the Edge of 'Blade Runner'",
                  "Year": "2000",
                  "imdbID": "tt0281011",
                  "Type": "movie",
                  "Poster": "https://m.media-amazon.com/images/M/MV5BZWJmOThjMjItNzE4Ni00YmY3LTk2NzEtMTJlYTQxZGE1MDYyXkEyXkFqcGdeQXVyMTM3NzQ5NzQ@._V1_SX300.jpg"
                },
        {
                  "Title": "Blade Runner: Deleted and Alternate Scenes",
                  "Year": "2007",
                  "imdbID": "tt1165254",
                  "Type": "movie",
                  "Poster": "N/A"
                },
        {
                  "Title": "Blade Runner 2049: To Be Human: - Casting Blade Runner 2049",
                  "Year": "2018",
                  "imdbID": "tt7879362",
                  "Type": "movie",
                  "Poster": "https://m.media-amazon.com/images/M/MV5BMjRjZDVkMTMtMzZlZC00YzBhLWJkYjQtNWVjNzVhNzg1NjAxXkEyXkFqcGdeQXVyMjA3NzQyMA@@._V1_SX300.jpg"
                },
        {
                  "Title": "Blade Runner 60: Director's Cut",
                  "Year": "2012",
                  "imdbID": "tt1846491",
                  "Type": "movie",
                  "Poster": "N/A"
                }
              ]

    matches = list(filter(lambda movie: re.search(regex, movie['Title']) != None, db))
    print('Matches')
    print(matches)
    return JsonResponse(matches, safe=False)
