from setuptools import setup

setup(
    name='apisvc',
    packages=['apisvc'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-restful',
        'openstacksdk',
        'kubernetes',
        'etcd3'
    ],
)
