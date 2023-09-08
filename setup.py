from setuptools import setup

setup(
	name='skeins',
	version='0.1.5',
	author='Akshay Balsubramani',
	author_email='akshay@akshay.bio',
	packages=['skeins'],
	url='https://github.com/b-akshay/skeins',
	license='LICENSE.txt',
	description='Some efficient algorithmic primitives in Python.',
    install_requires = [
        'numpy',
        'scipy',
        'scikit-learn', 
        'scanpy>=1.7', 
        'requests'
    ], 
    tests_require = [
        'pytest'
    ],
    platforms=['Linux',
               'Mac OS-X',
               'Unix',
               'Windows'],            # Valid platforms your code works on, adjust to your flavor
    python_requires=">=3.8",          # Python version restrictions
    package_data={'': ['requirements.txt']}
    # extra_requires = {
    #     'viz': ['py3DMol', 'Pillow', 'seaborn'],
    #     'jupyter': ['jupyter'],
    # }
)