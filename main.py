from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


def obtener_blog_data(url):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            blog_elements = soup.find_all('div', class_='card camping-card')

            blog_data = []

            for blog in blog_elements:
                title = blog.find('p', class_="camping-card-title").text
                link = blog.find(
                    'img', class_="camping-card-cover")['data-src']

                blog_info = {
                    'title': title,
                    'link': link
                }

                blog_data.append(blog_info)

            return blog_data
    except Exception as e:
        return []


def obtener_numero_total_de_paginas(current):
    try:
        current_url = f'https://www.ruterocamping.com/blog?page={current}'
        response = requests.get(current_url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            blog_elements = soup.find_all('div', class_='card camping-card')
            if len(blog_elements) > 1:
                current = current+1
                return obtener_numero_total_de_paginas(current)
            else:
                return current
    except Exception as e:
        return 0 


def get_logo():
    url = 'https://www.ruterocamping.com/blog?page=1'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        logo = soup.find('a', class_='navbar-brand')

        if logo:
            src = logo.find('img')["src"]
            return src


def get_pagination(current_url):
    response = requests.get(current_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        ulDiv = soup.find('ul', class_='pagination')
        return ulDiv


def get_partners():
    try:
        url = 'https://www.ruterocamping.com/blog?page=1'
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            partner_logos = soup.find_all('li', class_='partner-logo')

            partners_data = []

            for partner_logo in partner_logos:
                link_element = partner_logo.find('a')
                logo = partner_logo.find('img')['src']

                if link_element:
                    link = link_element["href"]
                else:
                    link = "#"

                partner = {
                    'link': link,
                    'logo': logo
                }

                partners_data.append(partner)

            return partners_data
    except Exception as e:
        return []


@app.route('/')
def index():

    current_page = request.args.get('page', 1, type=int)

    current_url = f'https://www.ruterocamping.com/blog?page={current_page}'

    blog_data = obtener_blog_data(current_url)

    return render_template('./template.html', blog_data=blog_data, current_page=current_page, total_pages=obtener_numero_total_de_paginas(1), logo_navbar=get_logo(), pagination=get_pagination(current_url), partners=get_partners())


def get_top_section(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        section = soup.find('section', class_='blog-bg-section')
        return section

def get_main_section(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        section = soup.find('section', class_='section page-section')
        return section


@app.route('/replicablog')
def replicaBlog():
    current_url = 'https://www.ruterocamping.com/blog/donde-ir-en-fiestas-patrias-tres-lugares-imperdibles-para-planificar-tu-viaje'

    return render_template('./template2.html', logo_navbar=get_logo(), partners=get_partners(), top_section = get_top_section(current_url), main_section = get_main_section(current_url))

if __name__ == '__main__':
    app.run(debug=False)
