import asyncio
import json
import sys
from datetime import datetime, timezone
from .parser import parse_page
import httpx

async def main():
    raw = sys.stdin.read()
    try:
        input_data = json.loads(raw) if raw.strip() else {}
    except Exception:
        input_data = {}
    max_results = input_data.get('maxResults', 50)
    proxy_config = input_data.get('proxyConfiguration', {})

    base_url = "https://news.ycombinator.com"
    results = []
    page = 1

    async with httpx.AsyncClient(timeout=30.0, follow_redirects=True) as client:
        while len(results) < max_results:
            url = base_url if page == 1 else f"{base_url}?p={page}"
            try:
                resp = await client.get(url)
                resp.raise_for_status()
            except Exception as e:
                print(json.dumps({"error": str(e)}))
                sys.exit(1)
            items = parse_page(resp.text)
            if not items:
                break
            for item in items:
                item['scrapedAt'] = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.000Z')
                results.append(item)
                if len(results) >= max_results:
                    break
            if len(items) == 0 or 'More' not in resp.text:
                break
            page += 1

    for item in results[:max_results]:
        print(json.dumps(item))

if __name__ == "__main__":
    asyncio.run(main())
