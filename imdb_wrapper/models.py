from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Rating:
    score: float
    votes: int
    top_rank: Optional[int]


@dataclass
class BoxOffice:
    budget: Optional[int]
    budget_currency: str
    gross_worldwide: Optional[int]
    gross_currency: str
    opening_weekend_domestic: Optional[int]


@dataclass
class ReleaseDate:
    day: Optional[int]
    month: Optional[int]
    year: int

    def __str__(self) -> str:
        parts = [str(self.year)]
        if self.month:
            parts.insert(0, f"{self.month:02d}")
        if self.day:
            parts.insert(0, f"{self.day:02d}")
        return "-".join(reversed(parts))


@dataclass
class Person:
    imdb_id: str
    name: str


@dataclass
class Credit:
    category: str
    people: list[Person]

    def names(self) -> list[str]:
        return [p.name for p in self.people]


@dataclass
class AKA:
    title: str
    country: str


@dataclass
class Movie:
    imdb_id: str
    title: str
    original_title: str
    release_date: ReleaseDate
    rating: Rating
    box_office: BoxOffice
    plot: str
    runtime_minutes: int
    genres: list[str]
    certificate: Optional[str]
    languages: list[str]
    countries: list[str]
    keywords: list[str]
    credits: list[Credit]
    akas: list[AKA] = field(default_factory=list)
    trivia: list[str] = field(default_factory=list)
    goofs: list[str] = field(default_factory=list)

    def _credit(self, category: str) -> Optional[Credit]:
        return next((c for c in self.credits if c.category == category), None)

    def director(self) -> Optional[str]:
        c = self._credit("Director")
        return c.names()[0] if c and c.people else None

    def writers(self) -> list[str]:
        c = self._credit("Writers")
        return c.names() if c else []

    def stars(self) -> list[str]:
        c = self._credit("Stars")
        return c.names() if c else []

    def __str__(self) -> str:
        bo = self.box_office
        budget_str = f"${bo.budget:,} {bo.budget_currency}" if bo.budget else "N/A"
        gross_str = f"${bo.gross_worldwide:,} {bo.gross_currency}" if bo.gross_worldwide else "N/A"
        opening_str = f"${bo.opening_weekend_domestic:,}" if bo.opening_weekend_domestic else "N/A"
        akas_str = ", ".join(f"{a.title} ({a.country})" for a in self.akas[:3])

        lines = [
            f"{self.title} ({self.release_date.year})",
            f"  Original Title : {self.original_title}",
            f"  Release Date   : {self.release_date}",
            f"  Certificate    : {self.certificate or 'N/A'}",
            f"  Rating         : {self.rating.score}/10 ({self.rating.votes:,} votes)"
            + (f" | IMDb Top {self.rating.top_rank}" if self.rating.top_rank else ""),
            f"  Runtime        : {self.runtime_minutes} min",
            f"  Genres         : {', '.join(self.genres)}",
            f"  Languages      : {', '.join(self.languages)}",
            f"  Countries      : {', '.join(self.countries)}",
            f"  Budget         : {budget_str}",
            f"  Worldwide Gross: {gross_str}",
            f"  Opening Weekend: {opening_str} (domestic)",
            f"  Director       : {self.director()}",
            f"  Writers        : {', '.join(self.writers())}",
            f"  Stars          : {', '.join(self.stars())}",
            f"  Keywords       : {', '.join(self.keywords)}",
            f"  Also Known As  : {akas_str}",
            f"  Plot           : {self.plot}",
        ]
        if self.trivia:
            lines.append("\n  Trivia:")
            lines += [f"    - {t}" for t in self.trivia]
        if self.goofs:
            lines.append("\n  Goofs:")
            lines += [f"    - {g}" for g in self.goofs]
        return "\n".join(lines)
