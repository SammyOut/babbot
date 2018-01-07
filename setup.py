from setuptools import setup

setup(
    # introduction
    name='babbot',
    version='1.0.0',
    url='https://github.com/RISMME/bob-bot',
    description='A package for make kakao-talk school meal bot easily',
    license='MIT',

    # author
    author='RISM',
    author_email='python@istruly.sexy',

    # classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Framework :: Flask',

        'Intended Audience :: Education',
        'Topic :: Education',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',

    ],

    # keyword
    keywords='School Meal Kakaotalk Chatbot',

    # package
    py_modules=['babbot'],

    # requirements
    install_requires=[
        'schapi',
        'flask'
    ],
)