import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    
__version__ = "0.0.0"

repository_name = "Text-Summarise"  
author_user_name = "shadow-warrior123" 
src_repo = "text summarizer"
author_email = "f20212735@pilani.bits-pilani.ac.in"
setuptools.setup(
    name=src_repo,
    version=__version__,
    author=author_user_name,
    author_email=author_email,
    description="A python package for text summarization using NLP techniques.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{author_user_name}/{repository_name}",
    project_urls={
        "Bug Tracker": f"https://github.com/{author_user_name}/{repository_name}/issues",
    },
        package_dir={"": "src"},
        packages=setuptools.find_packages(where="src")
    )

