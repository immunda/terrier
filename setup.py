from setuptools import setup

setup(
    name="terrier",
    author="Phil Howell",
    author_email="phil@quae.co.uk",
    version="0.0.1dev",
    url="https://github.com/immunda/terrier",
    install_requires=["click",],
    pymodules=["terrier"],
    entry_points="""
        [console_scripts]
        terrier=terrier:cli
    """,
    license="MIT",
    long_description=open("README.md").read(),
)
