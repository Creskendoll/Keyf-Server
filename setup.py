from setuptools import setup

setup(
    name='Keyf',
    packages=['Keyf'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask_pymongo',
        'flask_restful'
    ],
)