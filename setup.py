import os
from setuptools import setup, find_packages


def read_file(filename):
    """Read a file into a string"""
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except IOError:
        return ''


setup(
    name='django-facebook_gallery',
    version=__import__('facebook_gallery').__version__,
    author='Viktor Nagy',
    author_email='viktor.nagy@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/nagyv/facebook_gallery',
    download_url='https://github.com/nagyv/facebook_gallery/zipball/master',
    description=u' '.join(__import__('facebook_gallery').__doc__.splitlines()).strip(),
    classifiers=[
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',      
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Framework :: Django',
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
    ],
    long_description=read_file('README.rst'),
    test_suite="runtests.runtests",
    zip_safe=False,
    requires=['django(>=1.4)','facepy']
)
