from setuptools import setup

setup(
    name='maxfield',
    version='4.0',
    description='Ingress Maxfield: An Ingress Linking and Fielding Strategy Generator',
    author='Trey V. Wenger',
    author_email='tvwenger@gmail.com',
    packages=['maxfield'],
    install_requires=['numpy<1.24.0', 'networkx', 'scipy', 'ortools', 'protobuf==4.25.0',
                      'matplotlib', 'imageio', 'pygifsicle'],
    scripts=['bin/maxfield-plan'],
)
