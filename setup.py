from setuptools import setup

setup(
    name='SaveDesktop',
    version='3.3.2',
    install_requires=[
        'PyGObject>=3.40',  # Required for GTK4 and LibAdwaita
        'gtk4>=4.10',
        'libadwaita>=1.3',
    ],
)

