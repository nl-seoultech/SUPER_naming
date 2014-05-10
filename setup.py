
from setuptools import setup, find_packages

install_requires = [

]

test_requires = [
    'pytest >= 2.3.5'
]

setup(name='SUPER_naming', 
      description=u'naming program with massive files', 
      author = 'Gong Seong Hyeon', 
      author_email = 'tanesia_cou@naver.com',
      packages = find_packages(),
      install_requires = install_requires, 
      test_require = test_requires )
