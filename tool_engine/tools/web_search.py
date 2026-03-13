"""
Web Search Tool
"""
def main(query, num_results=5):
    import requests
    try:
        # Simple DuckDuckGo search
        url = f"https://duckduckgo.com/html/?q={query}"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        return f"Search results for '{query}' (Status: {response.status_code})"
    except Exception as e:
        return f"Search error: {e}"
