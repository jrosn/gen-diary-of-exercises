from setuptools import setup

setup(
    name='gen_diary_of_exercises',
    version='',
    packages=['gen_diary_of_exercises'],
    url='',
    license='',
    author='Roman Sosnovsky',
    author_email='rmnssnvsk@gmail.com',
    description='The generator of diary of exercises',
    entry_points={
        'console_scripts': [
            'gen-diary-of-exercises = gen_diary_of_exercises:main',
        ]
    },
)
