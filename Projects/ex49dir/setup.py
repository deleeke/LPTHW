try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = [
    'description' : 'Excercise 49',
    'author' : 'Elijah DeLee',
    'download_url' : 'https://github.com/deleeke/',
    'author_email' : 'deleeke@gmail.com',
    'version' : '0.1',
    'install_requires' : ['nose'],
    'packages' : ['ex49'],
    'scripts' : [],
    'name' : 'Exercise 49'
]

setup(**config)
