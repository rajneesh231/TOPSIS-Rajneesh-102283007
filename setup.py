import setuptools

def readme():
    with open('README.md') as file:
        README = file.read()
    return README

setuptools.setup(
    name="TOPSIS-Rajneesh-102283007",
    version="0.3",
    description="A Python package for implementing TOPSIS technique.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    author="Rajneesh Bansal",
    author_email="rajneeshb231@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        "Programming Language :: Python :: 3.7",
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    packages=["TOPSIS-Rajneesh-102283007"],
    include_package_data=True,
    install_requires=[                      'numpy',
                      'pandas',
     ],
     entry_points={
        "console_scripts": [
            "topsis=src.topsis:main",
        ]
     },
)