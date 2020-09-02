from setuptools import setup

setup(
    name='racache',
    author='Gabriel Montagné Láscaris-Comneno',
    author_email='gabriel@tibas.london',
    license='MIT',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'racache = racache.__main__:main'
        ]
    }
)
