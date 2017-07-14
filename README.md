# Amazon Review Scrapy

This is a Python Scrapy project which is done on Amazon Product review.

# Requirements
1) Python 2.7
2) Scrapy

# Introduction to Python
Python is a widely used high-level programming language for general-purpose programming, created by Guido van Rossum and first released in 1991.
Official Website :- https://www.python.org/

# Introduction to Scrapy
An open source and collaborative framework for extracting the data you need from websites.In a fast, simple, yet extensible way.
Official Website :- https://scrapy.org/

# Install Scrapy
$ pip install scrapy

# Create Scrapy project
1) Start to create scrapy project
$ scrapy startproject amazonscrapy
2) Move to folder.
$ cd amazonscrapy
3) Generate Spider
$ scrapy genspider amazonspider amazon.com
Note:- genspider -> use to generate spider
       amazonspider -> spider name
       amazon.com -> domain name

# Run Spider 
$ scrapy crawl amazonspider

# Terms and Condition 
Anyone can use and push it for use. Please use and modify. In case of any modification please raise pull request which may be helpful for others in future.
