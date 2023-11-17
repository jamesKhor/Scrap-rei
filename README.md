# The follow script make use of scrapy to scape product information from site.
## Installation
```
pip install scrapy
```
## Running
```python
scrapy crawl products
```
Json output
```python
scrapy crawl products -o product.json
```
CSV output
```python
scrapy crawl products -o product.csv
```
## Configuration
Modify URLs, and Domains spiders/products.py
- Item loaders class must matches the css selector and elements id, or class name
- Rule, link extractor have to matches the URI, URL. The syntax have to be tuple.

## Notes
on terminal 
```bash
#interactively see the output of css selector and elements output
scrapy shell <domain.com> 
```
