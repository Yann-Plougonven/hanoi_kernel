from setuptools import setup, find_packages

setup(
    name='HanoiKernel',
    version='0.1',
    url='https://github.com/Yann-Plougonven/hanoi_kernel',
    author='Yann Plougonven--Lastennet',
    author_email='plougonven-y@saint-louis29.net',
    description="Hanoi tower game's kernel",
    packages=find_packages(),    
    install_requires=['Stack', 'Sphinx'],
)
