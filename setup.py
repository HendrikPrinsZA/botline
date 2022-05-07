from setuptools import setup, find_packages

with open('README.rst') as f:
  readme = f.read()

with open('LICENSE') as f:
  license = f.read()

def parse_requirements(filename):
  lines = (line.strip() for line in open(filename))
  return [line for line in lines if line and not line.startswith("#")]

setup(
  name = 'call-a-bot',
  version = '0.1.0',
  description = 'Call a bot and have a conversation',
  long_description = readme,
  author = 'Hendrik Prinsloo',
  author_email = 'info@hendrikprinsloo.co.za',
  url = 'https://github.com/HendrikPrinsZA/call-a-bot',
  license = license,
  packages = ['call_a_bot'],
  install_requires = parse_requirements('requirements.txt'),
)

