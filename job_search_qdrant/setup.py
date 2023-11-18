from setuptools import setup

setup(
    name='job_search_qdrant',
    version='0.1.0',    
    description='Scripts for qdrant collection management, data access and insertion',
    author='Marcin Knyć',
    # author_email='na@na.com',
    license='GNU GENERAL PUBLIC LICENSE',
    packages=[
        'repositories'], # todo: change
    install_requires=[
        'qdrant-client',
        'sentence-transformers',
        'numpy',
        'langchain'
    ]
)