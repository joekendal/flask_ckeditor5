"""
Flask-CKEditor5
---------------

Integrates version 5 of CKEditor into flask context
"""
from setuptools import setup

setup(
    name='Flask-CKEditor5',
    version='1.0',
    license='MIT',
    author='Joe Kendal',
    description='Integrate CKEditor5 into a Flask app',
    long_description=__doc__,
    py_modules=['flask_ckeditor5'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=['Flask'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
