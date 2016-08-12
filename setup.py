from setuptools import setup

setup(
    name='phoneID21',
    version='0.1',
    py_modules=['phoneID21'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        phoneID21=phoneID21:cli
    ''',
)

