from setuptools import setup, find_packages

setup(
    name='promptground',
    version='1.1.1',
    author='NoCode, Inc.',
    description='A Python SDK for interacting with PromptGround API.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://promptground.io',
    packages=find_packages(),
    install_requires=[
        'requests>=2.25.1',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
