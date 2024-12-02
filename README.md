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
docker run --rm notes-app 
```