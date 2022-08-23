import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='quickregress',
    packages=['quickregress'],
    version='0.1.2',
    license='MIT',
    description='Provides a low-effort wrapper for sklearn\'s polynomial regression',
    long_description_content_type="text/markdown",
    long_description=long_description,
    author='Raelynn Hattie',
    author_email='raelynn@hattie.email',
    url='https://github.com/hexaguin/quickregress',
    keywords=['sklearn', 'regression'],
    install_requires=[
        'numpy',
        'sklearn',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
