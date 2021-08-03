import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="proto-parser-ng",
  version="1.6.3",
  author="avac74",
  author_email="andre.cruz@aaqua.live",
  description="A package for parsing proto files",
  long_description_content_type="text/markdown",
  url="https://github.com/Aaqua-live/protoparser-ng",
  packages=setuptools.find_packages(),
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: Apache Software License",
    "Operating System :: OS Independent",
    "Topic :: Software Development :: Libraries :: Python Modules",
  ],
  install_requires=[
    'lark-parser>=0.8.6',
    'numpy>=1.14.0'
  ],
)
