from setuptools import setup


VERSION = "0.0.1"

setup(
    name='yandex-xml-parser',
    description="Convert html to snippets",
    version=VERSION,
    url='https://github.com/KokocGroup/yandex-xml-parser',
    download_url='https://github.com/KokocGroup/yandex-xml-parser/tarball/v{0}'.format(VERSION),
    packages=['yandex_xml_parser'],
    install_requires=[],
)