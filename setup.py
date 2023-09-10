from setuptools import setup

setup(
	name='skeins',
	version='0.1.5',
	author='Akshay Balsubramani',
	author_email='akshay@akshay.bio',
	packages=['skeins'],
	url='https://github.com/b-akshay/skeins',
	license='LICENSE.txt',
	description='Some efficient algorithmic primitives for data analysis.',
    install_requires = [
        'numpy',
        'scipy',
        'scikit-learn', 
        # 'pytorch', 
        'scanpy>=1.7', 
        'requests'
    ], 
    tests_require = [
        'pytest'
    ],
    platforms=['Linux',
               'Mac OS-X',
               'Unix',
               'Windows'],  
    python_requires=">=3.8",          # Python version restrictions
    package_data={'': ['requirements.txt']}
    extras_require = {
        'viz': ['celluloid'], 
        'chem': ['rdkit-pypi', 'deepchem'], 
        'graph': ['scikit-network', 'hdbscan']
        # 'genomics': ['jupyter']
    }
)