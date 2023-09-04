from setuptools import setup

setup(
	name='skeins',
	version='0.1.0',
	author='Akshay Balsubramani',
	author_email='akshay@akshay.bio',
	packages=['skeins'],
	url='https://github.com/b-akshay/skeins',
	license='LICENSE.txt',
	description='Python code for efficient algorithmic primitives.',
	install_requires=[
		'numpy >= 1.22.2', 
		'scipy >= 1.10.1',
		'scikit-learn >= 1.0.2', 
        'requests >= 2.27.0'
	]
)