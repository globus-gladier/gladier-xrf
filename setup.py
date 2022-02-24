import os
from setuptools import setup, find_packages

# single source of truth for package version
version_ns = {}
with open(os.path.join('gladier_xrf', 'version.py')) as f:
    exec(f.read(), version_ns)
version = version_ns['__version__']

install_requires = []
with open('requirements.txt') as reqs:
    for line in reqs.readlines():
        req = line.strip()
        if not req or req.startswith('#'):
            continue
        install_requires.append(req)


setup(
    name='gladier-xrf',
    description='The Gladier Client for XRF Maps',
    url='https://github.com/globus-gladier/gladier-xrf',
    maintainer='The Gladier Team',
    maintainer_email='',
    version=version_ns['__version__'],
    packages=find_packages(),
    install_requires=install_requires,
    scripts=[],
    dependency_links=[],
    license='Apache 2.0',
    classifiers=[
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX',
        'Operating System :: MacOS :: MacOS X',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]
)