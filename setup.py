#from distutils.core import setup
from setuptools import setup
import os, os.path

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="django-cpserver",
    version="1.2",
    description="Management commands for serving Django via CherryPy's built-in WSGI server",
    author="Peter Baumgartner",
    author_email="pete@lincolnloop.com",
    url="https://github.com/manuelnaranjo/django-cpserver",
    packages=[
        "django_cpserver",
        "django_cpserver.management",
        "django_cpserver.management.commands",
    ],
    license="BSD",
    long_description=read("README.rst"),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: CherryPy",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
    ]
)