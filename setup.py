from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='cbpi4-NotifyShell',
      version='0.0.1',
      description='CraftBeerPi4 Plugin to forward Notifications to a Command Line program, parameter1=title, parameter2=text',
      author='David Jungwirth',
      author_email='',
      url='',
      license='GPLv3',
      include_package_data=True,
      package_data={
        # If any package contains *.txt or *.rst files, include them:
      '': ['*.txt', '*.rst', '*.yaml'],
      'cbpi4-NotifyShell': ['*','*.txt', '*.rst', '*.yaml']},
      packages=['cbpi4-NotifyShell'],
      long_description=long_description,
      long_description_content_type='text/markdown'
     )
