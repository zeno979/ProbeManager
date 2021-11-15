from setuptools import setup

with open('requirements/base.txt', 'r') as reqs:
    requirements = reqs.read().splitlines()
with open('requirements/test.txt', 'r') as reqs:
    requirements_test = reqs.read().splitlines()

setup (
    name='probemanager',
    version='1.3.0.dev1',
    packages=['probemanager'],
    install_requires=requirements,
    test_requires=requirements_test
)
