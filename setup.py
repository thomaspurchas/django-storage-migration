#!/usr/bin/env python
from distutils.core import setup

import storage_migration

setup(name='django-storage-migration',
      version=storage_migration.__version__,
      description=storage_migration.__doc__,
      author='City Live NV',
      author_email='gert.vangool@citylive.be',
      url='http://github.com/citylive/django-storage-migration/',
      packages=['storage_migration'],
      license='BSD',
      include_package_data = True,
      zip_safe = False,
      classifiers = [
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Programming Language :: Python',
          'Operating System :: OS Independent',
          'Environment :: Web Environment',
          'Framework :: Django',
      ],
)

