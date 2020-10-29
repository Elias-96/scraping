from urllib.request import urlopen
from urllib.parse import urljoin
from bs4 import BeautifulSoup

all_links = set()
visited_links = set()
crawl_queue = set()
absolute = set()
my_books = set()


def crawl_page(page):
    try:

        visited_links.add(page)
        print("crawling\t" + page)
        html = urlopen(page)
        bsObj = BeautifulSoup(html.read(), 'lxml')
        titles = bsObj.find_all('h2')
        for bk in titles:
            if bk not in my_books:
                my_books.add(bk)
            print(bk.text)
        tags = bsObj.find_all('a')
        for tag in tags:
            if 'href' in tag.attrs:
                link = (tag.attrs['href'])
                if link.startswith('/'):
                    final = urljoin(page, link)
                    print("addedjoin\t" + final)
                    if 'pdfdrive' and 'category' in final:
                        if 'login' not in final:
                            crawl_queue.add(final)
                            print("crawlqueu\t" + final)
                        for mylink in crawl_queue:
                            if mylink not in visited_links:
                                crawl_page(mylink)
                else:
                    if link.startswith('http' or 'https'):
                        absolute.add(link)
                        for x in absolute:
                            if x not in all_links:
                                all_links.add(x)
                                if x not in visited_links:
                                    visited_links.add(x)
                            print("absolute\t\t" + x)
    except BaseException:
        pass


if __name__ == "__main__":
    crawl_page("https://www.EXAMPLE.COM")
    print(len(my_books))
