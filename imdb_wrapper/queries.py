SEARCH_TITLES = """
query($query: String!, $first: Int!) {
  mainSearch(first: $first, options: {
    searchTerm: $query
    type: TITLE
    isExactMatch: false
  }) {
    edges {
      node {
        entity {
          ... on Title {
            id
            titleText { text }
            releaseYear { year }
            titleType { text }
            ratingsSummary { aggregateRating voteCount }
            plot { plotText { plainText } }
            genres { genres { text } }
            runtime { seconds }
            certificate { rating }
            primaryImage { url width height caption { plainText } }
          }
        }
      }
    }
  }
}
"""

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
    primaryImage { url width height caption { plainText } }
    images(first: 8) { edges { node { url width height caption { plainText } } } }
    videoStrip(first: 5) {
      edges { node {
        id
        name { value }
        contentType { displayName { value } }
        runtime { value }
        thumbnail { url width height }
        playbackURLs { displayName { value } url mimeType }
      }}
    }
  }
}
"""
