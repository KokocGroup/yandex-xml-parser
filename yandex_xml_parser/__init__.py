#! coding: utf-8

import re
from yandex_xml_parser.exceptions import EmptySerp, NoBodyInResponseError, BadYandexXmlParserError, BadUrlError, \
    SnippetsParserException

__all__ = ['YandexXmlParser']

YANDEX_XML_ERROR_CODE_NOT_FOUND = 15


class YandexXmlParser(object):
    def __init__(self, content, snippet_fields=('d', 'p', 'u', 't', 's', 'm')):
        self.content = content.decode('utf8') if isinstance(content, str) else content
        self.snippet_fields = snippet_fields

    def get_serp(self):
        res = re.compile('<yandexsearch.*?</yandexsearch>', re.I | re.M | re.S).search(self.content)
        if not res:
            raise NoBodyInResponseError()

        error = self.get_error()

        if error and error['code'] == YANDEX_XML_ERROR_CODE_NOT_FOUND:
            return {'pc': 0, 'sn': []}

        if error:
            return {
                'error': error
            }

        pagecount = self.get_pagecount()
        snippets = self.get_snippets()

        return {'pc': pagecount, 'sn': snippets}

    def get_pagecount(self):
        pagecount = 0
        response = self.content
        res = re.search(
            ur'<found-docs priority="all">(\d+)</found-docs>', response, re.I | re.M | re.S | re.U
        )
        if res:
            pagecount = int(res.group(1))
        return pagecount

    def get_snippets(self):
        result = []
        pattern = re.compile(ur'(<group>.*?</group>)', re.I | re.M | re.S)
        items = pattern.findall(self.content)
        for i, item in enumerate(items):
            p = i + 1
            result.append({
                'p': p,
                'u': self._get_snippet_url(item),
                'd': self._get_domain(item),
                'm': False,
                't': self._get_title(item),
                's': self._get_descr(item),
            })

        return result

    def _get_snippet_url(self, item):
        pattern = re.compile(ur'<url>\s*([^<]+)\s*</url>', re.I | re.M | re.S)
        res = pattern.search(item)
        if res:
            return res.group(1)

        raise SnippetsParserException()

    def _get_domain(self, item):
        pattern = re.compile(ur'<domain>\s*([^<]+)\s*</domain>', re.I | re.M | re.S)
        res = pattern.search(item)
        if res:
            return res.group(1)

        raise SnippetsParserException()

    def _get_title(self, item):
        if 't' not in self.snippet_fields:
            return

        pattern = re.compile(ur'<title>\s*(.+?)\s*</title>', re.I | re.M | re.S)
        res = pattern.search(item)
        if res:
            return res.group(1).replace('\n', ' ').strip()

        raise SnippetsParserException()

    def _get_descr(self, item):
        if 's' not in self.snippet_fields:
            return

        pattern = re.compile(ur'<passages>(.*?)</passages>', re.I | re.M | re.S)
        res = pattern.search(item)
        if res:
            descr = res.group(1).replace('<passage>', '')
            descr = descr.replace('</passage>', '')
            descr = descr.replace('\n', ' ')
            return descr.strip()

        pattern = re.compile(ur'<headline>(.*?)</headline>', re.I | re.M | re.S)
        res = pattern.search(item)
        if res:
            return res.group(1).strip()

    def get_error(self):
        pattern = re.compile(
            ur'<response[^>]+>\s*<error code="(\d+)">\s*(.+?)<\/error>\s*</response>',
            re.DOTALL | re.IGNORECASE | re.UNICODE | re.MULTILINE
        )
        res = pattern.search(self.content)
        if res:
            return {
                'code': int(res.group(1)),
                'msg': res.group(2),
            }

    def is_not_found(self):
        return u'<error code="15">Искомая комбинация слов нигде не встречается</error>' in self.content
