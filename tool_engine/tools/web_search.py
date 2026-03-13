import requests,urllib.parse
from bs4 import BeautifulSoup

def main(query):

    url="https://duckduckgo.com/html/?q="+urllib.parse.quote(query)

    r=requests.get(url,headers={"User-Agent":"Mozilla"},timeout=10)

    soup=BeautifulSoup(r.text,"html.parser")

    out=[]

    for x in soup.select(".result")[:5]:

        t=x.select_one(".result__a")

        if t:
            out.append(t.text)

    return "\n".join(out)
