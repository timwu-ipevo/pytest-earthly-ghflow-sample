# pytest-earthly-ghflow-sample

## run tests
```
earthly +test
```

## build image
```
earthly +build
```

## check and run the image
```
docker images|grep note
docker run --rm -ti -p 8000:8000  notes-app
```

## check the docs 
* check docs
```
#using browser to open
http://<host IP>>:8000/api/v1/docs
http://<host IP>>:8000/api/v1/openapi.json
```