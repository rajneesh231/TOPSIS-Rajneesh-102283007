from setuptools import setup, find_packages
import codecs
import os


VERSION = '0.1'
DESCRIPTION = 'A Python package to perform Multiple Criteria Decision Making using TOPSIS'
LONG_DESCRIPTION = 'A Python package that provides a comprehensive implementation of the TOPSIS method for Multiple Criteria Decision Making (MCDM). The Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS) is a well-established decision-making approach that assists in selecting the best alternative from a set of feasible options based on multiple criteria..'

# Setting up
setup(
    name="TOPSIS-Rajneesh-102283007",
    version=VERSION,
    description = DESCRIPTION,
  author = 'Rajneesh Bansal',                   # Type in your name
  author_email = 'rajneeshb231@gmail.com',
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[            # I get to this in a second
          'numpy',
          'pandas',
      ],
   keywords = ['TOPSIS', 'MCDM', 'Criteria','Multiple','Decision making','Decision','Ranking'],
    classifiers=[
        'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',   
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ] 
)