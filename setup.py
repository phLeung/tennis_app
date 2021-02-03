from setuptools import setup
setup(
    name='tennis_score_app',
    packages=['tennis_score_app'],
    include_package_data=True,
    install_requires=[
        'flask','flask_sqlalchemy','flask-wtf'
    ],
)
