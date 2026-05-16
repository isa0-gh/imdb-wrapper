import json
import urllib.request

from .models import AKA, Credit, Image, Movie, BoxOffice, Person, PlaybackURL, Rating, ReleaseDate, Video
from .queries import FETCH_TITLE

API_URL = "https://api.graphql.imdb.com/"


def _image(node: dict) -> Image:
    return Image(
        url=node["url"],
        width=node["width"],
        height=node["height"],
        caption=node.get("caption", {}).get("plainText") if node.get("caption") else None,
    )


class IMDbClient:
    def fetch(self, imdb_id: str) -> Movie:
        payload = json.dumps({"query": FETCH_TITLE, "variables": {"id": imdb_id}}).encode()
        req = urllib.request.Request(
            API_URL,
            data=payload,
            headers={"Content-Type": "application/json"},
        )
        with urllib.request.urlopen(req) as resp:
            t = json.loads(resp.read())["data"]["title"]

        rd = t["releaseDate"]
        budget = t.get("productionBudget")
        gross = t.get("lifetimeGross")
        opening = t.get("openingWeekendGross")

        videos = [
            Video(
                imdb_id=e["node"]["id"],
                name=e["node"]["name"]["value"],
                content_type=e["node"]["contentType"]["displayName"]["value"],
                runtime_seconds=e["node"]["runtime"]["value"],
                thumbnail=_image(e["node"]["thumbnail"]),
                playback_urls=[
                    PlaybackURL(
                        quality=p["displayName"]["value"],
                        url=p["url"],
                        mime_type=p["mimeType"],
                    )
                    for p in e["node"]["playbackURLs"]
                ],
            )
            for e in t["videoStrip"]["edges"]
        ]

        return Movie(
            imdb_id=imdb_id,
            title=t["titleText"]["text"],
            original_title=t["originalTitleText"]["text"],
            release_date=ReleaseDate(rd["day"], rd["month"], rd["year"]),
            rating=Rating(
                score=t["ratingsSummary"]["aggregateRating"],
                votes=t["ratingsSummary"]["voteCount"],
                top_rank=t["ratingsSummary"]["topRanking"]["rank"] if t["ratingsSummary"]["topRanking"] else None,
            ),
            box_office=BoxOffice(
                budget=budget["budget"]["amount"] if budget else None,
                budget_currency=budget["budget"]["currency"] if budget else "USD",
                gross_worldwide=gross["total"]["amount"] if gross else None,
                gross_currency=gross["total"]["currency"] if gross else "USD",
                opening_weekend_domestic=opening["gross"]["total"]["amount"] if opening else None,
            ),
            plot=t["plot"]["plotText"]["plainText"],
            runtime_minutes=t["runtime"]["seconds"] // 60,
            genres=[g["text"] for g in t["genres"]["genres"]],
            certificate=t["certificate"]["rating"] if t.get("certificate") else None,
            languages=[l["text"] for l in t["spokenLanguages"]["spokenLanguages"]],
            countries=[c["text"] for c in t["countriesOfOrigin"]["countries"]],
            keywords=[e["node"]["keyword"]["text"]["text"] for e in t["keywords"]["edges"]],
            credits=[
                Credit(
                    category=c["category"]["text"],
                    people=[Person(n["name"]["id"], n["name"]["nameText"]["text"]) for n in c["credits"]],
                )
                for c in t["principalCredits"]
            ],
            poster=_image(t["primaryImage"]) if t.get("primaryImage") else None,
            images=[_image(e["node"]) for e in t["images"]["edges"]],
            videos=videos,
            akas=[AKA(e["node"]["text"], e["node"]["country"]["text"]) for e in t["akas"]["edges"]],
            trivia=[e["node"]["text"]["plainText"] for e in t["trivia"]["edges"]],
            goofs=[e["node"]["text"]["plainText"] for e in t["goofs"]["edges"]],
        )
