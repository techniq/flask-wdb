"""
Flask-Wdb
---------

Integrate Wdb instead of Werkzeug debugger for Flask applications
"""
from setuptools import setup

VERSION = '0.0.2'

setup(
    name='Flask-Wdb',
    version=VERSION,
    url='https://github.com/techniq/flask-wdb/',
    license='BSD',
    author='Sean Lynch',
    author_email='techniq35@gmail.com',
    description='Integrate Wdb instead of Werkzeug debugger for Flask applications',
    long_description=__doc__,
    py_modules=['flask_wdb'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'wdb'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Software Development :: Debuggers'
    ]
)
