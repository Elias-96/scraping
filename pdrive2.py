from urllib.request import urlopen
from urllib.parse import urljoin
from bs4 import BeautifulSoup

all_links = set()
visited_links = set()
crawl_queue = set()
absolute = set()


def crawl_page(page):
    visited_links.add(page)
    print("crawling\t"+page)
    html = urlopen(page)
    bsObj = BeautifulSoup(html.read(), 'lxml')
    titles = bsObj.find_all('h2')
    for bk in titles:
        print(bk.text)
    tags = bsObj.find_all('a')
    for tag in tags:
        if 'href' in tag.attrs:
            link = (tag.attrs['href'])
            if link.startswith('/'):
                final = urljoin(page, link)

                print("added\t"+final)
            else:
                if link.startswith('http' or 'https'):
                    absolute.add(link)
                    for x in absolute:
                        print("absolute\t\t" + x)
                        if final not in all_links:
                            print("+all_links\t"+final)
                            all_links.add(final)



if __name__ == "__main__":
    crawl_page("https://www.example.com")
