try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
config = {
    'description':'My Project',
    'author':'Rill',
    'url':'URL to get it at.',
    'download_url':'where to download it.',
    'author_email':'My email',
    'version':'0.1',
    'insta;;_requires':['nose'],
    'packages':['Name'],
    'script':[],
    'name':'projectname'
    }
    
serup(**config)