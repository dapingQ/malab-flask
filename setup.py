from setuptools import setup

setup(
    name='app',
    packages=['app'],
    include_package_data=True,
    install_requires=[
        'flask',
        'flask-wtf',
        'flask-sqlalchemy',
        'flask-script',
        'flask-migrate'
    ],
)