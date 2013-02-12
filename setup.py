"""
Flask-Wdb
-------------

Integrate Wdb instead of Werkzeug debugger for Flask applications
"""
from setuptools import setup


setup(
    name='Flask-Wdb',
    version='0.0.1',
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
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
