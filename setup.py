from setuptools import setup, find_packages
setup(
    name="screenpy",
    version="0.1",
    packages=["screenpy", "screenpy.core", "screenpy.web"],
    install_requires=[
        "selenium",
        "pytest",
        "allure-pytest"
    ],
    author="Matthew Williams",
    author_email="matthew.williams@wsp.com",
    description="This package provides tools to aid behaviour-driven testing of systems, based around the screenply pattern",
    license="MIT"
)
