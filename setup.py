from setuptools import setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(
    name='primaoLIB1',
    version='0.0.1',
    url='https://github.com/massakiigarashi2/primaoLIB1.git',
    license='MIT License',
    author='Massaki',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='prof.massakie@gmail.com',
    keywords='Pacote',
    description='Exemplo de pacote PyPI',
    packages=['primaoLIB1'],
    install_requires=['numpy'],
)