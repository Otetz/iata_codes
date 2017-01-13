from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))


def get_file_content(file_name):
    with open(path.join(here, file_name), encoding='utf-8') as f:
        return f.read()


version = {}
exec(open(path.join(here, 'iata_codes/version.py')).read(), version)

setup(
    name="iata_codes",
    version=version['__version__'],
    description="REST API Client for IATA Codes database",
    long_description=get_file_content('README.rst'),
    url="https://github.com/otetz/iata_codes",
    author="Alexey Shevchenko",
    author_email="otetz@me.com",
    license='MIT',
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Topic :: Software Development :: Libraries",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ],
    keywords='iata development',
    packages=find_packages(),
    include_package_data=True,
    setup_requires=['pytest-runner'],
    install_requires=get_file_content('requirements.txt'),
    tests_require=get_file_content('requirements_test.txt'),
    test_suite='tests',
)
