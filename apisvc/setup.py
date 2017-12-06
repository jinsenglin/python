from setuptools import setup, find_packages

setup(
    name='apisvc',
    version='1.0.0',
    author='CC Lin',
    author_email='jimlintw922@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask == 0.12.2',
        'flask-restful == 0.3.6',
        'openstacksdk == 0.9.19',
        'kubernetes == 4.0.0b1',
        'etcd3 == 0.7.0',
        'requests == 2.18.4',
        'fasteners == 0.14.1'
    ],
)
