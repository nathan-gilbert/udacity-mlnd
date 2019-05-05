# udacity-mlnd

## Uploading to PyPi
```bash
cd ng_udacity_distributions
python setup.py sdist
pip install twine
```

### commands to upload to the pypi test repository
```bash 
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

pip install --index-url https://test.pypi.org/simple/ dsnd-probability

### command to upload to the pypi repository
```bash
twine upload dist/*
pip install ng-udacity-distributions
```