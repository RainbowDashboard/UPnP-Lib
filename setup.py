from setuptools import setup
from subprocess import call

setup(name='UPnP',
      version='1.0',
      description='Forward a Port with UPnP and pure Python script',
      author='efio',
      license='MIT',
      packages=['UPnP'],
      zip_safe=False)

call('pip install gevent')
call('pip install ipgetter')
