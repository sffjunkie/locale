# Copyright (c) 2015 Simon Kennedy <sffjunkie+code@gmail.com>

from setuptools import setup, find_packages


setup(name='mogul.locale',
    version="0.1",
    description="""mogul""",
#    long_description=open('README.txt').read(),
    author='Simon Kennedy',
    author_email='sffjunkie+code@gmail.com',
    url="http://www.sffjunkie.co.uk/python-mogul.html",
    license='Apache-2.0',
    
    package_dir={'': 'src'},
    packages=['mogul.locale'],
    namespace_packages=['mogul',],

    package_data = {'mogul.locale': ['bcp47_registry.utf8']},
)
