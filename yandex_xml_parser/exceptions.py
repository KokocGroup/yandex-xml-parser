# -*- coding:utf-8 -*-


class YandexXmlParserError(Exception):
    pass


class BadYandexXmlParserError(Exception):
    pass


class NoBodyInResponseError(YandexXmlParserError):
    pass


class EmptySerp(YandexXmlParserError):
    pass


class SnippetsParserException(YandexXmlParserError):
    pass


class BadUrlError(YandexXmlParserError):
    pass