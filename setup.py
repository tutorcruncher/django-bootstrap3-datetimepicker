from setuptools import setup


setup(
    name='django-bootstrap3-datetimepicker',
    packages=['bootstrap3_datetime'],
    include_package_data=True,
    version='2.4',
    description='Bootstrap3 compatible datetimepicker for Django projects.',
    long_description=open('README.md').read(),
    author='Nakahara Kunihiko/Samuel Colvin',
    author_email='nakahara.kunihiko@gmail.com/s@muelcolvin.com',
    url='https://github.com/samuelcolvin/django-bootstrap3-datetimepicker',
    license='Apache License 2.0',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',
        'Environment :: Web Environment',
        'Framework :: Django',
    ],
)
