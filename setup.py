#from distutils.core import setup
from setuptools import setup
setup(name='pyjugex',
      version='0.6',
      packages=['pyjugex'],
      license='BSD',
      description='Perform differential gene expression on two chosen brain regions',
      url='https://github.com/haimasree/pyjugex',
      author='Big Data Analytics Group, INM-1, Research Center Juelich',
      author_email='h.bhattacharya@fz-juelich.de',
      py_modules=['pyjugex', 'hbp_human_atlas'],
      install_requires=['numpy', 'scipy', 'statsmodels', 'requests', 'nibabel', 'xmltodict'], 
      )
