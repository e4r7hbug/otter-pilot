#!/usr/bin/env python3.6
"""Otter Pilot."""
import pathlib
import shlex
import subprocess

from setuptools import find_packages, setup


def tag_version():
    """Generate version number from Git Tag, e.g. v2.0.0, v2.0.0-1."""
    try:
        recent_tag = subprocess.check_output(shlex.split('git describe --long'))
    except subprocess.CalledProcessError:
        recent_tag = b'v0.0-0-00000000'
    tag, count, _ = recent_tag.decode().split('-')
    version = 'a'.join([tag, count]) if int(count) else tag
    return version


with open('requirements.txt', 'rt') as reqs_file:
    reqs_list = reqs_file.readlines()

setup(
    name='otter-pilot',
    version=tag_version(),
    description='CLI otter pilot for running frequent instructions.',
    long_description=open('README.rst').read(),
    author='Nate Tangsurat',
    author_email='e4r7hbug@gmail.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    setup_requires=['setuptools_scm'],
    use_scm_version=True,
    install_requires=reqs_list,
    include_package_data=True,
    namespace_packages=['otter'],
    keywords='python',
    url='https://github.com/e4r7hbug/otter-pilot',
    download_url='https://github.com/e4r7hbug/otter-pilot',
    platforms=['OS Independent'],
    license='MIT License',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points={
        'console_scripts': [
            'otter=otter.__main__:main',
        ],
    }, )
