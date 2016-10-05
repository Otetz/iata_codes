from setuptools import setup, find_packages


def get_file_content(file_name):
    with open(file_name) as f:
        return f.read()


readme = get_file_content('README.md')

exec(open('iata_codes/version.py').read())

setup(
    name="iata_codes",
    version=__version__,
    author="Alexey Shevchenko",
    url="https://github.com/otetz/iata_codes",
    author_email="otetz@me.com",
    description="REST API Client for IATA Codes database",
    long_description=readme,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=get_file_content('requirements.txt'),
    tests_require=get_file_content('requirements_test.txt'),
    test_suite='tests',
)
