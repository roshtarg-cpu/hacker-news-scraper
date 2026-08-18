from bs4 import BeautifulSoup

def parse_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = []
    rows = soup.select('tr.athing')
    for row in rows:
        title_line = row.select_one('span.titleline a')
        if not title_line:
            continue
        title = title_line.get_text(strip=True)
        url = title_line.get('href', '')
        if not url.startswith('http'):
            url = 'https://news.ycombinator.com/' + url
        rank = row.get('id', '')

        subline = row.find_next_sibling('tr')
        if not subline:
            continue
        score = subline.select_one('span.score')
        points = score.get_text(strip=True).replace(' points', '').replace(' point', '') if score else '0'
        user = subline.select_one('a.hnuser')
        user_text = user.get_text(strip=True) if user else ''
        age = subline.select_one('span.age')
        time_text = age.get_text(strip=True) if age else ''
        links = subline.find_all('a')
        comments = '0'
        if links:
            comments = links[-1].get_text(strip=True).replace(' comments', '').replace(' comment', '')
            if comments == 'discuss':
                comments = '0'
        items.append({
            'title': title,
            'url': url,
            'points': points,
            'user': user_text,
            'time': time_text,
            'comments': comments,
            'rank': rank
        })
    return items
