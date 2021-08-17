from bs4 import BeautifulSoup as bs
import requests
import time


def page_parser(link, num_pages):

    final_list = []
    for index in range(1, num_pages):
        link = f'{link}+{index}'
        try:
            html_text = requests.get(link).text
        except Exception:
            break
        soup = bs(html_text, 'lxml')
        jobs = soup.find_all('article')
        offer_titles = [job.find('span', class_='offer-item-title').text for job in jobs]
        offer_summaries = [job.find('p', class_='text-nowrap').text.split(', ')[1] for job in jobs]
        offer_rooms = [job.find('li', class_='offer-item-rooms hidden-xs').text.split()[0] for job in jobs]
        offer_prices = [job.find('li', class_='offer-item-price').text.lstrip() for job in jobs]
        offer_area = [job.find('li', class_='hidden-xs offer-item-area').text.split()[0] for job in jobs]
        offer_link = [job.h3.a for job in jobs]
        time.sleep(2)

        for i in range(len(offer_titles)):
            final_list.append([offer_titles[i],
                               offer_summaries[i],
                               offer_area[i],
                               offer_rooms[i],
                               offer_prices[i],
                               offer_link[i]])

    return final_list

# print(page_parser('https://www.otodom.pl/sprzedaz/mieszkanie/warszawa/?search%5Bregion_id%5D=7&search%5Bsubregion_id%5D'
#                   '=197&search%5Bcity_id%5D=26&search%5Bpaidads_listing%5D=1&page=', 2)[0][0:5])
