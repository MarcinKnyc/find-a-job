from setuptools import setup

setup(
    name='job_offer_exporter',
    version='0.1.0',    
    description='Scripts for connecting offers from Postgres and Qdrant databases',
    author='Marcin Knyć',
    # author_email='na@na.com',
    license='GNU GENERAL PUBLIC LICENSE',
    packages=['exporter'],
    install_requires=[
        'job_search_postgres',
        'job_search_qdrant'
    ]
)