"""
Setup file for emotion detection package
"""
from setuptools import setup, find_packages

setup(
    name='emotion-detector',
    version='1.0.0',
    description='Emotion Detection Application using Watson NLP',
    author='Your Name',
    packages=find_packages(),
    install_requires=[
        'flask>=2.0.0',
        'ibm-watson>=6.0.0',
        'ibm-cloud-sdk-core>=3.0.0'
    ],
    python_requires='>=3.8'
)
