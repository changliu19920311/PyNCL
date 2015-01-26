from setuptools import setup
import pyncl

setup(
    name='pyncl',
    version=pyncl.__version__,
    description='PyNCL: a Python based NCL wrapper.',
    long_description=open('README.md').read(),
    author='Feng Zhu',
    author_email='feng.zhu@ssec.wisc.edu',
    url='https://github.com/lyricorpse/PyNCL',
    license='BSD',
    py_modules=['pyncl'],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python :: 3'
    ]
)
