from setuptools import setup

if __name__ == "__main__":
    setup(
        name = "thumbor_google_cloud",
        version = "1.0.0",
        author = "Tripcreator Ehf.",
        author_email = "None",
        description = "Simple storage (non result) for Thumbor on Google Cloud",
        license = "MIT",
        keywords = "thumbor google cloud",
        url = "https://github.com/xperious/thumbor-google-cloud",
        packages=['thumbor_google_cloud'],
        install_requires =  [
        "thumbor>=6.3.0",
        "google-cloud-storage>=1.6.0",
        ],
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Topic :: Software Development :: Libraries :: Python Modules",
            "License :: OSI Approved :: MIT License"
        ],
    )
