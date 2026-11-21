#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="django-ical",
    description="iCal feeds for Django based on Django's syndication feed framework.",
    long_description="\n".join(
        [
            open("README.rst", encoding="utf-8").read(),
            open("CHANGES.rst", encoding="utf-8").read(),
        ]
    ),
    keywords="ical calendar django syndication feed",
    author="Ian Lewis",
    license="MIT License",
    url="https://github.com/django-commons/django-ical",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Environment :: Plugins",
        "Framework :: Django",
        "Framework :: Django :: 5.2",
        "Framework :: Django :: 6.0",
        "Framework :: Django :: 6.1",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.11",
    install_requires=["django>=5.2", "icalendar>=4.0.3", "django-recurrence>=1.11.1"],
    packages=find_packages(),
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
)
