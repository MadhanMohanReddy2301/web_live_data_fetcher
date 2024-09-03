from .google_search import google_search
from .web_scraper import fetch_page_content, extract_body_content

def live_data(query1):
    query = query1
    num_urls = 5
    urls = google_search(query, num_results=num_urls)
    collected_data = ""

    for i, url in enumerate(urls):
        print(f"Fetching URL {i + 1}: {url}")
        html_content = fetch_page_content(url)
        if html_content:
            title, body_text = extract_body_content(html_content)
            collected_data += f"Title: {title}\n{body_text}\n\n"

    return collected_data
