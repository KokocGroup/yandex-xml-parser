#! coding: utf-8
import json

import unittest
from yandex_xml_parser.tests import YandexXmlParserTests
from yandex_xml_parser import YandexXmlParser, NoBodyInResponseError


class YandexXmlParserTestCase(YandexXmlParserTests):

    def test1(self):
        u""""
            Проверка ничего не найдено
        """
        xml = self.get_data('not-found.xml')
        y = YandexXmlParser(xml)
        self.assertTrue(y.is_not_found())

    def test2(self):
        u""""
            Ищем кол-во страниц
        """
        xml = self.get_data('2015-10-21.xml')
        y = YandexXmlParser(xml)
        pc = y.get_pagecount()
        self.assertEqual(pc, 102206784)

    def test3(self):
        u""""
            Ищем сниппеты
        """
        xml = self.get_data('error33.xml')
        y = YandexXmlParser(xml)
        serp = y.get_serp()
        self.assertEqual(serp['error']['code'], 33)

    def test4(self):
        u""""
            Ищем сниппеты
        """
        xml = self.get_data('2015-10-21.xml')
        y = YandexXmlParser(xml)
        serp = y.get_serp()
        self.assertEqual(serp['pc'], 102206784)
        self.assertEqual(len(serp['sn']), 10)

        self.assertEqual(serp['sn'][0]['p'], 1)
        self.assertEqual(serp['sn'][0]['d'], 'www.php.su')
        self.assertEqual(serp['sn'][0]['u'], 'http://www.php.su/mysql_query')
        self.assertEqual(serp['sn'][0]['t'], u'PHP.SU - Функция mysql_<hlword>query</hlword>()')
        self.assertEqual(serp['sn'][0]['s'], u'mysql_<hlword>query</hlword>() посылает запрос активной базе данных сервера, на который ссылается переданный указатель. Если параметр link_identifier опущен...')

        self.assertEqual(serp['sn'][9]['p'], 10)
        self.assertEqual(serp['sn'][9]['d'], 'flybase.org')
        self.assertEqual(serp['sn'][9]['u'], 'http://flybase.org/static_pages/cytosearch/cytosearch15.html')
        self.assertEqual(serp['sn'][9]['t'], u'FlyBase CytoSearch <hlword>Query</hlword>')
        self.assertEqual(serp['sn'][9]['s'], u'If your input is not a unique symbol or synonym, a list of options with valid gene symbols will be displayed; use the valid gene symbol with the ‘Gene symbol’ menu option in a new CytoSearch <hlword>query</hlword>.')

    def test5(self):
        u""""
            Ищем сниппеты
        """
        xml = self.get_data('2015-10-22.xml')
        y = YandexXmlParser(xml)
        serp = y.get_serp()
        self.assertEqual(serp['pc'], 18166460)
        self.assertEqual(len(serp['sn']), 10)

        self.assertEqual(serp['sn'][0]['p'], 1)
        self.assertEqual(serp['sn'][0]['d'], 'www.raduga-granit.spb.ru')
        self.assertEqual(serp['sn'][0]['u'], 'http://www.raduga-granit.spb.ru/k10.htm')
        self.assertEqual(serp['sn'][0]['t'], u'<hlword>Столешницы</hlword> в <hlword>Санкт</hlword>-<hlword>Петербурге</hlword> (СПб), продажа производство...')
        self.assertEqual(serp['sn'][0]['s'], u'<hlword>Столешницы</hlword> подоконники, изготовление <hlword>столешниц</hlword> и подоконников из камня, керамогранита, гранита, мрамора в <hlword>Санкт</hlword>-<hlword>Петербурге</hlword>. Радуга, Петербург.')

        self.assertEqual(serp['sn'][9]['p'], 10)
        self.assertEqual(serp['sn'][9]['d'], 'mymansion.ru')
        self.assertEqual(serp['sn'][9]['u'], 'http://mymansion.ru/interer/kak-vyibrat-stoleshnitsu-dlya-kuhni.html')
        self.assertEqual(serp['sn'][9]['t'], u'Как выбрать <hlword>столешницу</hlword> для кухни? | Интерьер')
        self.assertEqual(serp['sn'][9]['s'], u'Основные критерии при выборе <hlword>столешницы</hlword> - материал, из которого она изготавливается и дизайн. Как выбрать <hlword>столешницу</hlword> для кухни, чтобы она была практична...')

    def test6(self):
        u""""
            Ищем сниппеты
        """
        xml = self.get_data('error32.xml')
        y = YandexXmlParser(xml)
        serp = y.get_serp()
        self.assertEqual(serp['error']['code'], 32)

    def test7(self):
        u""""
            Ищем сниппеты
        """
        xml = self.get_data('2015-10-22.1.xml')
        y = YandexXmlParser(xml)
        serp = y.get_serp()
        self.assertEqual(serp['pc'], 194953855)
        self.assertEqual(len(serp['sn']), 50)

        self.assertEqual(serp['sn'][0]['p'], 1)
        self.assertEqual(serp['sn'][0]['d'], 'www.otdelka-trade.ru')
        self.assertEqual(serp['sn'][0]['u'], 'http://www.otdelka-trade.ru/11-stoleshnica')
        self.assertEqual(serp['sn'][0]['t'], u'<hlword>Столешницы</hlword> для кухни <hlword>купить</hlword> в <hlword>Москве</hlword>, выгодная цена...')
        self.assertEqual(serp['sn'][0]['s'], u'В нашей компании, <hlword>купить</hlword> <hlword>столешницу</hlword> не составит труда.')

        self.assertEqual(serp['sn'][49]['p'], 50)
        self.assertEqual(serp['sn'][49]['d'], 'www.stoliarka.ru')
        self.assertEqual(serp['sn'][49]['u'], 'http://www.stoliarka.ru/woodtable.html')
        self.assertEqual(serp['sn'][49]['t'], u'<hlword>Купить</hlword> кухонную <hlword>столешницу</hlword> из дерева на заказ - <hlword>Москва</hlword>')
        self.assertEqual(serp['sn'][49]['s'], u'Так как производство расположено в <hlword>Москве</hlword>, то <hlword>купить</hlword> у нас <hlword>столешницу</hlword> достаточно просто.')

    def test8(self):
        u""""
            Ищем сниппеты
        """
        xml = self.get_data('2015-10-22.2.xml')
        y = YandexXmlParser(xml)
        serp = y.get_serp()
        self.assertEqual(serp['pc'], 381859)
        self.assertEqual(len(serp['sn']), 50)

        self.assertEqual(serp['sn'][0]['p'], 1)
        self.assertEqual(serp['sn'][0]['d'], 'www.avito.ru')
        self.assertEqual(serp['sn'][0]['u'], 'https://www.avito.ru/moskva/avtomobili/audi/tt')
        self.assertEqual(serp['sn'][0]['t'], u'<hlword>Купить</hlword> <hlword>Audi</hlword> <hlword>TT</hlword> – <hlword>продажа</hlword> подержанных и новых автомобилей...')
        self.assertEqual(serp['sn'][0]['s'], u'<hlword>Продажа</hlword> новых или б/у авто <hlword>Audi</hlword> <hlword>TT</hlword> – частные объявления о продаже новых и авто с пробегом.')

        self.assertEqual(serp['sn'][14]['p'], 15)
        self.assertEqual(serp['sn'][14]['d'], 'www.cars.ru')
        self.assertEqual(serp['sn'][14]['u'], 'http://www.cars.ru/find/marka/Audi/TT/')
        self.assertEqual(serp['sn'][14]['t'], u'<hlword>Купить</hlword> <hlword>Ауди</hlword> <hlword>ТТ</hlword> купе, кабриолет, родстер. Новая <hlword>Audi</hlword> <hlword>TT</hlword>...')
        self.assertEqual(serp['sn'][14]['s'], None)

        self.assertEqual(serp['sn'][49]['p'], 50)
        self.assertEqual(serp['sn'][49]['d'], 'kupi-pricep.ru')
        self.assertEqual(serp['sn'][49]['u'], 'http://kupi-pricep.ru/catalog/bagazhniki-dlya-audi-tt')
        self.assertEqual(serp['sn'][49]['t'], u'Багажники для <hlword>Audi</hlword> <hlword>TT</hlword> | Каталог')
        self.assertEqual(serp['sn'][49]['s'], u'Багажник Thule для <hlword>Audi</hlword> <hlword>TT</hlword> 3дв. Купэ 2006г. и по н.в. (аэродинамическая дуга).')

    def test9(self):
        u""""
            Ищем сниппеты
        """
        xml = self.get_data('2017-01-24.xml')
        y = YandexXmlParser(xml)
        serp = y.get_serp()

        self.assertEqual(serp['pc'], 110)
        self.assertEqual(len(serp['sn']), 0)

    def test10(self):
        u""""
            Ищем сниппеты
        """
        xml = self.get_data('error55.xml')
        y = YandexXmlParser(xml)
        serp = y.get_serp()
        self.assertEqual(serp['error']['code'], 55)

    def test11(self):
        u""""
            Ищем сниппеты
        """
        xml = self.get_data('2017-11-29.xml')
        y = YandexXmlParser(xml)
        serp = y.get_serp()
        self.assertEqual(serp['pc'], 175430642)
        self.assertEqual(len(serp['sn']), 50)

        self.assertEqual(serp['sn'][0]['p'], 1)
        self.assertEqual(serp['sn'][0]['d'], u'devaka.ru')
        self.assertEqual(serp['sn'][0]['u'], u'https://devaka.ru/articles/seo-beginning')
        self.assertEqual(serp['sn'][0]['t'], u'План <hlword>раскрутки</hlword>: <hlword>С</hlword> <hlword>чего</hlword> <hlword>начать</hlword> <hlword>продвижение</hlword> <hlword>сайта</hlword>?')
        self.assertEqual(serp['sn'][0]['s'], u'Надеюсь, теперь вы знаете <hlword>с</hlword> <hlword>чего</hlword> <hlword>начать</hlword> <hlword>продвижение</hlword> своего <hlword>сайта</hlword>!Хорошая обзорная статья из разряда “А <hlword>с</hlword> <hlword>чего</hlword> <hlword>начать</hlword> <hlword>сео</hlword>”? Хорошо, что более подробная инфа вынесена в отдельные статьи, на которые проставлены ссылки.')

        self.assertEqual(serp['sn'][46]['p'], 47)
        self.assertEqual(serp['sn'][46]['d'], 'amalbakov.ru')
        self.assertEqual(serp['sn'][46]['u'], 'http://amalbakov.ru/poiskovoe-prodvizhenie/seo/')
        self.assertEqual(serp['sn'][46]['t'], u'')
        self.assertEqual(serp['sn'][46]['s'], u'Что такое <hlword>SEO</hlword> и <hlword>оптимизация</hlword> <hlword>сайта</hlword>? Совокупность действий, выполняемых с целью повышения позиций <hlword>сайта</hlword> в выдачеЕсть ли у Вас время заниматься <hlword>продвижением</hlword> <hlword>сайта</hlword>? Если есть, то необходимо изучить всю информацию и <hlword>начинать</hlword> практиковаться!')

    def test12(self):
        u""""
            Ищем сниппеты
        """
        xml = self.get_data('404.xml')
        y = YandexXmlParser(xml)
        with self.assertRaises(NoBodyInResponseError):
            y.get_serp()

    def print_sn(self, res):
        for i in res['sn']:
            print
            print i['p']
            print i['d']
            print i['u']
            print i['t']
            print i['s']

if __name__ == '__main__':
    unittest.main()
