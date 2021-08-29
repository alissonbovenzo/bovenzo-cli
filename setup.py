from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name="bovenzo-cli",
    version='0.3.11',
    py_modules=["bovenzo"],
    include_package_data=True,
    install_requires=["click"],
    entry_points="""
        [console_scripts]
        bovenzo=bovenzo:cli
        bo=bovenzo:cli
    """,
    author="Alisson Desandro Bovenzo",
    author_email="bovenzo@astrahus.tech",
    description="A Simple CLI to help u with commands used commonly by me, Bovenzo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alissonbovenzo/bovenzo-cli",
    project_urls={
        "Bug Tracker": "https://github.com/alissonbovenzo/bovenzo-cli/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

