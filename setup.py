from setuptools import setup


VERSION = "0.0.9"

setup(
    name='yandex-xml-parser',
    description="Yandex xml parser",
    version=VERSION,
    url='https://github.com/KokocGroup/yandex-xml-parser',
    download_url='https://github.com/KokocGroup/yandex-xml-parser/tarball/v{0}'.format(VERSION),
    packages=['yandex_xml_parser'],
    install_requires=[],
)
