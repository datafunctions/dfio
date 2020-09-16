import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()
setup(
  name="dfio",
  packages=["dfio"],
  version="0.0.1",
  description="",
  long_description=README,
  long_description_content_type="text/markdown",
  author="Jim Barlow",
  author_email="jim@beepbeep.technology",
  license='Apache License 2.0',
  zip_safe=False
)
