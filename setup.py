from setuptools import setup, find_packages

setup(
    name='obsidian_agent',
    version='0.1.0',
    description='AI-powered markdown generator and server for Obsidian workflows',
    author='Your Name',
    packages=find_packages(),
    install_requires=[
        'openai',
        'pyyaml',
        'fastapi',
        'uvicorn',
    ],
) 