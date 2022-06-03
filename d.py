import requests
from bs4 import BeautifulSoup


def get_data(url):
    headers = {
        'authority': 'codeforces.com',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://codeforces.com/gyms',
        'accept-language': 'en-US,en;q=0.9,ru;q=0.8',
        'cookie': 'lastOnlineTimeUpdaterInvocation=1639823397778; _ga=GA1.2.746464951.1589376065; RCPC=efd9a2e49487f29a406cfae791eefc8c; X-User-Sha1=40106dd8ee064d80c52f1a7ae6ac8aec148b3329; X-User=a5aae879b0a4d91fdd9a3e6f8db5dbfca65e9e3c60fc86394ebed9fff1356090911858f21521fff5; nocturne.language=ru; __utmz=71512449.1638352178.1333.95.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __atuvc=0%7C46%2C0%7C47%2C0%7C48%2C0%7C49%2C4%7C50; JSESSIONID=E88ECD619FC9ED6300445495B020DE22-n1; 39ce7=CFXV1WJA; __utma=71512449.746464951.1589376065.1639757610.1639821945.1352; __utmc=71512449; evercookie_png=tewylgcu47ql7mw855; evercookie_etag=tewylgcu47ql7mw855; evercookie_cache=tewylgcu47ql7mw855; 70a7c28f3de=tewylgcu47ql7mw855; __utmb=71512449.58.10.1639821945',
    }
    #
    # req = requests.get('https://codeforces.com/gym/103483', headers=headers)
    # with open("index.html", "w") as file:
    #     file.write(req.text)
    with open("index.html") as file:
        src = file.read()
    soup = BeautifulSoup(src, "lxml")
    table = soup.find(class_="problems").find_all("tr")
    problems = []
    problem_links = []
    for i in table[1:]:
        problems.append(i.find_all("td")[1].find("a"))
    for problem in problems:
        link = problem.get("href")
        problem_links.append(f"https://codeforces.com/{link}")
    print(*problem_links, sep='\n')


get_data("https://codeforces.com/profile/MDastan")
