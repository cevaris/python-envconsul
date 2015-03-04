readme = open('README.md').read()

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='envconsul',
    version='0.0.1',
    description="""Environment Variable and Settings Management via Consul""",
    long_description="""TODO""",
    author='Adam Cardenas',
    author_email='cevaris@gmail.com',
    url='https://github.com/cevaris/python-envconsul',
    packages=['envconsul',],
    include_package_data=True,
    install_requires=[
        'consulate==0.2.0',
        'tornado==4.1',
    ],
    license="MIT",
    zip_safe=False,
    keywords='envconsul',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        ],

)
