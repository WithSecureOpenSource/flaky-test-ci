from setuptools import setup

setup(
    name="flaky-ci",
    install_requires=["pandas", "junitparser"],
    extras_require={"dev": ["pytest", "black"]},
)
