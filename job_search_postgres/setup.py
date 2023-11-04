from setuptools import setup

setup(
    name='job_search_postgres',
    version='0.1.0',    
    description='Scripts for postgres data migrations, access and insertion',
    author='Marcin Knyć',
    # author_email='shudson@anl.gov',
    license='GNU GENERAL PUBLIC LICENSE',
    packages=['repositories'], # todo: change
    install_requires=[
        'alembic',
        'psycopg2-binary',
        'build'
    ]
)