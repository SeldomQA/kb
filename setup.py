# coding=utf-8
import re
import ast
from setuptools import setup, find_packages

_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('kb/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))


setup(
    name='kb',
    version=version,
    url='https://github.com/seldomQA/kb/',
    license='BSD',
    author='bugmaster',
    author_email='fnngj@126.com',
    description='kb is a simple performance testing tool.',
    long_description='',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'httpx>=0.16.1',
        'gevent>=20.9.0',
        'numpy>=1.19.2',
        'tqdm>=4.54.0',
        'rich>=10.12.0'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        "Topic :: Software Development :: Testing",
    ],
    entry_points='''
        [console_scripts]
        kb=kb.run:console_main
    ''',
    py_modules=['whyteboard'],
)
