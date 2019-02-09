import setuptools
import pypyrus_tables as tables

with open('README.md', 'r') as fh:
    long_description = fh.read()

author = tables.__author__
email = tables.__email__
version = tables.__version__
description = tables.__doc__
license = tables.__license__

setuptools.setup(
    name='pypyrus-tables',
    version=version,
    author=author,
    author_email=email,
    description=description,
    long_description=long_description,
    long_description_content_type='text/markdown',
    license=license,
    url='https://github.com/t3eHawk/tables',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
