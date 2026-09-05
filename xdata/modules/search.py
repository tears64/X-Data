from urllib.parse import quote_plus

ENGINES = {
    "Google": "https://www.google.com/search?q={}",
    "Bing": "https://www.bing.com/search?q={}",
    "DuckDuckGo": "https://duckduckgo.com/?q={}",
}

def run(value):
    query = value.strip()
    encoded = quote_plus(query)
    return {
        "type": "search",
        "query": query,
        "engines": {name: url.format(encoded) for name, url in ENGINES.items()},
    }


# Compatibility entry point used by the X-Data CLI.
def generate(value):
    return run(value)
