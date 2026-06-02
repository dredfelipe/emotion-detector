"""Setup file for the emotion detection package."""

from setuptools import find_packages, setup

setup(
    name='emotion-detector',
    version='1.0.0',
    description='Emotion Detection Application using Watson NLP',
    author='Fhilip',
    packages=find_packages(),
    install_requires=[
        'flask>=2.0.0',
        'requests>=2.25.0',
    ],
    python_requires='>=3.8'
)
