from setuptools import setup, find_packages

setup(
    name="weather_api",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Flask",
        "Flask-Limiter",
        "requests",
        "redis",
        "python-dotenv"
    ],  
    entry_points={  
        "console_scripts": [
            "weather-api=weather_api.app:app.run" 
        ]
    },
    author="Lewie Jackson",
    author_email="LewieJ08@gmail.com",
    description="A simple weather api built with flask that uses redis for caching",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/LewieJ08/weather_api",  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)