from setuptools import setup, find_packages
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()


setup(name='cybersectk',
    version='1.0',
    url='https://github.com/unspezifische/CyberSecTK',
    license='MIT',
    author='Unspezifische',
    author_email='unspezifische@gmail.com',
    description='Fork of cybersectk, a library for Machine Learning CyberSec feature extraction. Original author: SumendraBSingh',
    long_description=README,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        'scapy',
        'numpy',
        'scikit-learn',
        ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.11',
    include_package_data=True,
    zip_safe=False)
