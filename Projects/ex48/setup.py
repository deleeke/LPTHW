try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = [
    'description' : 'Exercise 48',
    'author' : 'Elijah DeLee',
    'download_url' : 'https://github.com/deleeke/LPTHW',
    'author_email' : 'deleek@gmail.com',
    'version' : '0.1',
    'install_requires' : ['nose'],
    'packages' : ['Exercise 48'],
    'scripts' : [],
    'name' : 'Excercise 48'
]

setup(**config)
