# easyocr-server

EasyOCR Server

## Using EasyOCR Server with Docker

We provide a Dockerfile to build an image.

```shell
docker build -t easyocr-server:latest .
```

Run it with

```shell
docker run -it -v {DATA_DIR}:/workspace/model -p 8083:8080 easyocr-server:latest
```
