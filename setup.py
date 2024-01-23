from setuptools import find_packages,setup

setup(
    name="mcqgenerator",
    version='0.0.1',
    auther='vinod tiwari',
    author_email='cpt1995daas@gmail.com',
    install_reqires=["opeai","lamngchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)