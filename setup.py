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
    install_requires = [
        'numpy',
        'scipy',
        'pandas',
        'scikit-learn', 
        'requests'
    ], 
    tests_require = [
        'pytest'
    ],
    platforms=['Linux',
               'Mac OS-X',
               'Unix',
               'Windows'],            # Valid platforms your code works on, adjust to your flavor
    python_requires=">=3.9",          # Python version restrictions
    # extra_requires = {
    #     'viz': ['py3DMol', 'Pillow', 'seaborn'],
    #     'jupyter': ['jupyter'],
    # },
	# install_requires=[
	# 	'numpy >= 1.22.2', 
	# 	'scipy >= 1.10.1',
	# 	'scikit-learn >= 1.0.2', 
    #     'requests >= 2.27.0'
	# ]
)