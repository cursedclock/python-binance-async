from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='python_binance_async',
      version='0',
      description='Simple api wrapper for binance exchange with async support',
      long_description=readme(),
      url='https://github.com/cursedclock/python_binance_async',
      author='cursedclock',
      author_email='mos01naj@gmail.com',
      license='MIT',
      packages=['python_binance_async'],
      insall_requires=['grequests'],
      include_package_data=True,
      zip_safe=False)
