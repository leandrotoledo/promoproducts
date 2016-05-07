# -*- coding: utf-8 -*-

import urllib
import re
from bs4 import BeautifulSoup
from promoproducts import Promoproducts

class Store(object):
    def __init__(self, store):
        self.encoding = Promoproducts().encoding
        self.stores = Promoproducts().get_stores()

        self.store = store

        self.departments = [
                                'Beleza e Saúde', 'Brinquedos',
                                'Cama, Mesa e Banho', 'Eletrodomésticos',
                                'Eletroportáteis', 'Esporte e Lazer', 'Games',
                                'Informática', 'Livros', 'Tablets',
                                'Telefones e Celulares', 'TV e Vídeo',
                                'Telefonia', 'Eletrônicos'
        ]

    def call_me(self):

        store_prods = []

        # retorna uma list de dicts com todos os departamentos
        depts = self.get_departments(self.store, [])

        print(depts)

        if not depts:
            return []

        for d in depts:
            d['department_categories'] = self.get_categories(d['department_href'])

            print(d['department_href'])

            for c in d['department_categories']:
                c['category_products'] = self.get_products(c['category_href'])

            print(d)

        return store_prods

    def get_departments(self, depto_css):
        depts = []

        # HTML of coupons page
        html = urllib.urlopen(self.store).read()

        # making a soup
        soup = BeautifulSoup(html, "html.parser", from_encoding=self.encoding)

        departments_link = soup.select(depto_css)

        for d in departments_link:
            if d.text.encode('utf8') in self.departments:
                depts.append({
                    'department_name': d.text.encode('utf8'),
                    'department_href': d['href']
                })

        return depts

    def get_categories(self, dept, category_css):
        """
        Get all categories from Extra departments.
        E.g. Bonecos, Playground etc from Brinquedos

        Args:
            :param dept: (str) a link to department link

        Return:
            :return:
        """

        categories = []

        # HTML of department page
        html = urllib.urlopen(dept).read()

        # making a soup
        soup = BeautifulSoup(html, "html.parser", from_encoding=self.encoding)

        # all categories available
        categories_link = soup.select(category_css)

        for c in categories_link:
            categories.append({
                'category_name': c.text.encode('utf8'),
                'category_href': c['href']
            })

        return categories

    def get_products(self, category, product_css):
        """
        Get all products from one category.

        Param:
            :param category: (str) a link to the category from department
            :param product: (str) the CSS of product wrapper
            :param from_price: (str) the CSS of normal price of product
            :param on_sale: (str) the CSS of on sale price of product
            :param next_page: (str) the CSS of next page link

        Return:
            :return: Returns a list of products informations
        """
        products = []

        # HTML of category page
        html = urllib.urlopen(category).read()

        # making a soup
        soup = BeautifulSoup(html, "html.parser", from_encoding=self.encoding)

        # prods from page
        ps = soup.select(product_css)

        # infos of single prod
        for p in ps:
            # if prod is available then will be 1
            available = 1

            # prod price
            from_price = p.find('span', attrs={'class': 'from price regular'})
            on_sale = p.find('span', attrs={'class': 'for price sale'})

            if on_sale is None:
                os = 0
                available = 0  # when the product is not available
            else:
                os = re.findall(r'([0-9]+\W+[0-9].)', str(on_sale).replace(',', '.'))[0]
                # import pdb; pdb.set_trace()
            if from_price is None:
                fp = os
            else:
                fp = re.findall(r'([0-9]+\W+[0-9].)', str(from_price).replace(',', '.'))[0]

            # all info of prod together
            prod = {
                'product_name': p.a['title'],
                'product_img': p.span.img['data-src'],
                'product_href': p.a['href'],
                'product_from_price': float(fp),
                'product_on_sale': float(os),
                'product_available': available,
            }

            # print(prod)

            products.append(prod)

        return products


        # products_list = []
        #
        # first_time = True
        #
        # # just for loop works for the first time
        # next_page = True
        #
        # while next_page:
        #
        #     if first_time:
        #         # HTML of category page
        #         html = urllib.urlopen(category).read()
        #
        #         first_time = False
        #     else:
        #         # HTML of category page
        #         html = urllib.urlopen(category_next_page).read()
        #
        #     # making a soup
        #     soup = BeautifulSoup(html, "html.parser", from_encoding=self.encoding)
        #
        #     # prods from page
        #     products = soup.select('div.lista-produto div.hproduct')
        #
        #     # infos of single prod
        #     for p in products:
        #         # if prod is available then will be 1
        #         available = 1
        #
        #         # prod price
        #         from_price = p.find('span', attrs={'class': 'from price regular'})
        #         on_sale = p.find('span', attrs={'class': 'for price sale'})
        #
        #         if on_sale is None:
        #             on_sale = "R$ 0"
        #             available = 0 # when the product is not available
        #         else:
        #             on_sale = on_sale.strong.text
        #
        #         if from_price is None:
        #             from_price = on_sale
        #         else:
        #             from_price = from_price.strong.text
        #
        #         # all info of prod together
        #         prod = {
        #             'product_name': p.a['title'],
        #             'product_img': p.span.img['data-src'],
        #             'product_href': p.a['href'],
        #             'product_from_price': from_price,
        #             'product_on_sale': on_sale,
        #             'product_available': available,
        #         }
        #
        #         products_list.append(prod)
        #
        #         category_next_page = soup.select('div.pagination li.next > a')
        #
        #         if category_next_page:
        #             category_next_page = category_next_page[0]['href']
        #         else:
        #             next_page = False


class Extra(Store):
    def call_me(self):
        super(Extra, self).call_me()
    
    def get_departments(self, depto):
        return super(Extra, self).get_departments(depto)

    def get_categories(self, dept, category):
        return super(Extra, self).get_categories(dept, category)

    def get_products(self, category, product_css):
        return super(Extra, self).get_products(category, product_css)

class PontoFrio(Store):
    def call_me(self):
        super(PontoFrio, self).call_me()

    def get_departments(self, depto_css):
        return super(PontoFrio, self).get_departments(depto_css)

    def get_categories(self, dept, category_css):
        return super(PontoFrio, self).get_categories(dept, category_css)

    def get_products(self, category, product_css):
        return super(PontoFrio, self).get_products(category, product_css)

class RicardoEletro(Store):
    def call_me(self):
        super(RicardoEletro, self).call_me()

    def get_departments(self, depto_css):
        return super(RicardoEletro, self).get_departments(depto_css)

    def get_categories(self, dept, category_css):
        return super(RicardoEletro, self).get_categories(dept, category_css)

    def get_products(self, category, product_css):
        return super(RicardoEletro, self).get_products(category, product_css)