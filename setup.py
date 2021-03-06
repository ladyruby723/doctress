import setuptools

setuptools.setup(
    name="doctress",
    version="0.1.0",
    url="https://github.com/ryanfreckleton/doctress",

    author="Ryan Freckleton",
    author_email="ryan.freckleton@gmail.com",

    description="A RestructuredText based literate programming and documentation tool.",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),
    entry_points = {
        'console_scripts': ['doctress=doctress:cli'],
    },

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
