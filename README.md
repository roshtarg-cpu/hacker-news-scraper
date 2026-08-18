# Hacker News Scraper — Stories, Comments & Developer Sentiment

Scrape Hacker News front page and paginated stories with this fast, reliable Apify actor. Extract titles, URLs, points, authors, timestamps, and comment counts for trend analysis, developer sentiment tracking, and AI-powered content monitoring.

## What data you get

- `title` — Story headline
- `url` — External link URL
- `points` — Upvote count
- `user` — Author username
- `time` — Relative timestamp (e.g. "3 hours ago")
- `comments` — Number of comments
- `rank` — Position on the page
- `scrapedAt` — ISO timestamp of the scrape

## Example input

```json
{
  "maxResults": 50,
  "proxyConfiguration": {
    "useApifyProxy": true,
    "apifyProxyGroups": ["RESIDENTIAL"]
  }
}
```

## Example output

```json
{
  "title": "Show HN: My new AI tool",
  "url": "https://example.com",
  "points": "142",
  "user": "pg",
  "time": "2 hours ago",
  "comments": "56",
  "rank": "1",
  "scrapedAt": "2026-08-18T12:34:56.000Z"
}
```

## Use cases

- Track trending tech stories in real time
- Monitor competitor mentions and sentiment
- Build AI agents that summarize developer discussions
- Feed data into Claude, ChatGPT, or MCP pipelines

## Queries this ranks for

- hacker news scraper
- scrape hacker news stories
- hn comments scraper
- developer sentiment tracker
- hacker news api alternative
- hn trends scraper
- ycombinator scraper
- hacker news dataset
- hacker news points scraper
- hn pagination scraper

## Who this is for

Developers, data analysts, and AI agents who need structured Hacker News data without hitting rate limits or parsing HTML manually.

## Works with

Claude, ChatGPT, and AI agents via Apify MCP.
