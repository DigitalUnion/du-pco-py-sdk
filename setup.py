import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dupco",
    version="0.0.6",
    author="gaojian",
    author_email="gaojian@shuzilm.cn",
    install_requires=[
        "pycryptodome==3.15.0",
        "requests==2.28.1"
    ],
    description="A simple way to call DigitalUnion service",
    long_description="",
    url="https://github.com/DigitalUnion/du-pco-py-sdk",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

# python3 -m pip install  --upgrade setuptools wheel
# python3 setup.py sdist bdist_wheel
# python3 -m pip install --user --upgrade twine
# python3 -m twine upload dist/*
