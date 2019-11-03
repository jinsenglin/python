from setuptools import setup, find_packages

setup(
    name='apicli',
    version='1.0.0',
    author='CC Lin',
    author_email='jimlintw922@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests == 2.20.0'
    ],
)
