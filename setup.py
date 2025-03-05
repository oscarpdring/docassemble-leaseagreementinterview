import os
import sys
from setuptools import setup, find_namespace_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')

def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.leaseagreementinterview',
      version='0.0.1',
      description=('A docassemble extension.'),
      long_description='# Lease Agreement Generator\r\nA DocAssemble interview that generates customizable lease agreements with optional riders.\r\n\r\n## Features\r\n- Dynamic rent schedule calculation (annual increase or custom)\r\n- Conditional document generation\r\n- Number-to-words conversion\r\n- Multiple guarantor support\r\n- Automatic date and financial calculations\r\n\r\n## Required Dependencies\r\n- num2words\r\n- docassemble.base.util\r\n\r\n## Documents Generated\r\n1. Base Lease Agreement (required)\r\n2. Good Guy Guarantee (required)\r\n3. Optional Documents:\r\n  - 111 NCP Lease\r\n  - Food & Beverage Use\r\n  - Broker Agreement\r\n  - Short Form Lease\r\n\r\n## Input Fields\r\n- Lease terms and dates\r\n- Entity information\r\n- Financial details\r\n- Property specifics\r\n- Broker details (if applicable)\r\n- Special conditions\r\n\r\n## Usage\r\n1. Fill out interview questions\r\n2. Review generated documents\r\n3. If approved, download documents\r\n4. If changes needed, select "No" to restart\r\n\r\n## File Structure\r\n- Main interview file\r\n- Document templates (.docx)\r\n- Helper functions for formatting and calculations\r\n\r\n## Version\r\n1.0\r\n\r\n## License\r\n[Your License Here]',
      long_description_content_type='text/markdown',
      author='System Administrator',
      author_email='elestio@daniel.beachlane.nyc',
      license='The MIT License (MIT)',
      url='https://docassemble.org',
      packages=find_namespace_packages(),
      install_requires=['num2words>=0.5.13'],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/leaseagreementinterview/', package='docassemble.leaseagreementinterview'),
     )

