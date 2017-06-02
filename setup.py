from setuptools import setup


setup(
    name='uni-slugify',
    version='0.1.4',
    description='A slug generator that turns strings into unicode slugs.',
    long_description='https://github.com/nitely/unicode-slugify',
    url='https://github.com/nitely/unicode-slugify',
    license='BSD',
    packages=['slugify'],
    include_package_data=True,
    package_data={'': ['README.md']},
    zip_safe=False,
    install_requires=['six', 'unidecode'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Environment :: Web Environment :: Mozilla',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)


