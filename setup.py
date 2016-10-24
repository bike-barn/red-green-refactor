#!/usr/bin/env python3

import re
import os.path
from setuptools import setup, find_packages
from pip.req import parse_requirements

here = os.path.abspath(os.path.dirname(__file__))

readme_path = os.path.join(here, 'README.md')
with open(readme_path, 'r') as readme_file:
    readme = readme_file.read()

# Borrowed from https://github.com/Gandi/gandi.cli/blob/master/setup.py
version_path = os.path.join(here, 'calc', '__init__.py')
with open(version_path, 'r') as version_file:
    version = re.compile(r".*__version__ = '(.*?)'",
                         re.S).match(version_file.read()).group(1)

req_path = os.path.join(here, 'requirements.txt')
requirements = [str(r.req) for r in parse_requirements(req_path, session=False)]

test_req_path = os.path.join(here, 'dev-requirements.txt')
test_requirements = [str(r.req) for r in parse_requirements(test_req_path, session=False)]

setup(
    name='red-green-refactor',
    version=version,
    description='A very simple calculator designed to teach software testing.',
    long_description=readme,
    author='Reilly Tucker Siemens, Alex LordThorsen',
    author_email='reilly@tuckersiemens.com, alexlordthorsen@gmail.com',
    url='https://github.com/bike-barn/red-green-refactor',
    packages=find_packages(),
    package_dir={'calc': 'calc'},
    include_package_data=True,
    install_requires=requirements,
    license='ISCL',
    zip_safe=False,
    keywords='testing calculator interpreter red green refactor',
    py_modules=['calc'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Education',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Education :: Testing',
        'Topic :: Software Development :: Interpreters',
    ],
    test_suite='tests',
    setup_requires=['pytest-runner'],
    tests_require=test_requirements,
    entry_points={
        'console_scripts': [
            'calc=calc.__main__:main',
        ],
    },
)
