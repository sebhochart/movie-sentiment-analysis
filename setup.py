# setup.py
from setuptools import setup
from setuptools import find_packages

# setup(name='movie_sentiment_analysis',
#       description="Project for analyzing and classifying sentiment arcs from movie scripts",
#       packages=["movie_sentiment_analysis"]) # You can have several packages, try it

# list dependencies from file
with open('requirements.txt') as f:
    content = f.readlines()
requirements = [x.strip() for x in content]

setup(name='movie_sentiment_analysis',
      description="Project for analyzing and classifying sentiment arcs from movie scripts",
      packages=find_packages(), # NEW: find packages automatically
      install_requires=requirements) # NEW
