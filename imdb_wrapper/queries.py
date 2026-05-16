FETCH_TITLE = """
query($id: ID!) {
  title(id: $id) {
    titleText { text }
    originalTitleText { text }
    releaseYear { year }
    releaseDate { day month year }
    ratingsSummary { aggregateRating voteCount topRanking { rank } }
    plot { plotText { plainText } }
    runtime { seconds }
    genres { genres { text } }
    certificate { rating }
    productionBudget { budget { amount currency } }
    lifetimeGross(boxOfficeArea: WORLDWIDE) { total { amount currency } }
    openingWeekendGross(boxOfficeArea: DOMESTIC) { gross { total { amount currency } } }
    spokenLanguages { spokenLanguages { text } }
    countriesOfOrigin { countries { text } }
    principalCredits {
      category { text }
      credits { name { nameText { text } id } }
    }
    keywords(first: 10) { edges { node { keyword { text { text } } } } }
    akas(first: 8) { edges { node { text country { text } } } }
    trivia(first: 5) { edges { node { text { plainText } } } }
    goofs(first: 3) { edges { node { text { plainText } } } }
  }
}
"""
