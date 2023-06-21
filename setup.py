# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name='autoeq',
    version='2.0.1',
    author='Jaakko Pasanen',
    packages=['autoeq'],
    scripts=[],
    url='https://github.com/jaakkopasanen/autoeq-pkg',
    licence='MIT Licence',
    description='Tool for equalizing headphones',
    platforms=['any'],
    keywords=['headphones', 'equalization'],
    install_requires=[
        'Pillow',
        'matplotlib',
        'pandas',
        'scipy',
        'numpy',
        'tensorflow',
        'tabulate',
        'soundfile'
    ]
)
