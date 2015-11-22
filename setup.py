"""
see: http://python-packaging-user-guide.readthedocs.org/en/latest/distributing
see: https://youtu.be/kNke39OZ2k0?t=47
"""

from setuptools import setup

setup(
    name='ami-kiln',
    version='v0.1.0',
    py_modules=['kiln'],
    install_requires=[
        'Click',
        'pytz',
        'PyYAML'
    ],
    entry_points={
        'console_scripts': [
            'kiln=kiln.application:main'
        ]
    },
)
