import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'pyramid',
    'pyramid_chameleon',
    'pyramid_debugtoolbar',
    'pyramid_tm',
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
    'psycopg2',
]

test_requires = [
    'pytest',
    'tox',
    'pytest-watch',
]


dev_requires = [
    'ipython',
]

setup(name='testapp',
      version='0.0',
      description='testapp',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
                  "Programming Language :: Python",
                  "Framework :: Pyramid",
                  "Topic :: Internet :: WWW/HTTP",
                  "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
      ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='testapp',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = testapp:main
      [console_scripts]
      initialize_testapp_db = testapp.scripts.initializedb:main""",
      extras_require={'test': test_requires, 'dev': dev_requires},
      )
