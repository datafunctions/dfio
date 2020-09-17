import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()
setup(
  name="dfio",
  packages=["dfio"],
  version="0.0.3",
  description="",
  long_description=README,
  long_description_content_type="text/markdown",
  author="Jim Barlow",
  author_email="jim@beepbeep.technology",
  license='Apache License 2.0',
  download_url='https://github.com/datafunctions/dfio/archive/0.0.3.tar.gz',
  zip_safe=False,
  install_requires=
  [
    'bleach==3.2.0',
    'cachetools==4.1.1',
    'certifi==2020.6.20',
    'chardet==3.0.4',
    'colorama==0.4.3',
    'docutils==0.16',
    'google-api-core==1.22.2',
    'google-auth==1.21.2',
    'google-cloud-core==1.4.1',
    'google-cloud-storage==1.31.0',
    'google-crc32c==1.0.0',
    'google-resumable-media==1.0.0',
    'googleapis-common-protos==1.52.0',
    'idna==2.10',
    'keyring==21.4.0',
    'packaging==20.4',
    'pkginfo==1.5.0.1',
    'protobuf==3.13.0',
    'pyasn1==0.4.8',
    'pyasn1-modules==0.2.8',
    'Pygments==2.7.0',
    'pyparsing==2.4.7',
    'pytz==2020.1',
    'readme-renderer==26.0',
    'requests==2.24.0',
    'requests-toolbelt==0.9.1',
    'rfc3986==1.4.0',
    'rsa==4.6',
    'six==1.15.0',
    'tqdm==4.49.0',
    'twine==3.2.0',
    'urllib3==1.25.10',
    'webencodings==0.5.1'
  ]
)
