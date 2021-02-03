from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='python_binance_x',
      version='0',
      description='A Simple and fast api wrapper for binance exchange.',
      long_description=readme(),
      url='https://github.com/cursedclock/python_binance_x',
      author='cursedclock',
      author_email='mos01naj@gmail.com',
      license='MIT',
      packages=['python_binance_x'],
      insall_requires=[],
      include_package_data=True,
      zip_safe=False)
