from setuptools import setup, find_packages

setup(
    name = "tabcli",
    version = "0.1",
    packages = find_packages(),
    scripts = ['bin/tabcli', 'bin/tabserver'],
    author = "Matthew Hooker",
    author_email = "mwhooker@gmail.com",
    description = "Interact with Chrome over the command line",
    license = "GPL3",
    url = "https://github.com/mwhooker/tabcli",

)
