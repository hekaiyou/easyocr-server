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

## Supported Languages

| Language | Code Name |
|--|--|
| Abaza | abq |
| Adyghe | ady |
| Afrikaans | af |
| Angika | ang |
| Arabic | ar |
| Assamese | as |
| Avar | ava |
| Azerbaijani | az |
| Belarusian | be |
| Bulgarian | bg |
| Bihari | bh |
| Bhojpuri | bho |
| Bengali | bn |
| Bosnian | bs |
| Simplified Chinese | ch_sim |
| Traditional Chinese | ch_tra |
| Chechen | che |
| Czech | cs |
| Welsh | cy |
| Danish | da |
| Dargwa | dar |
| German | de |
| English | en |
| Spanish | es |
| Estonian | et |
| Persian (Farsi) | fa |
| French | fr |
| Irish | ga |
| Goan Konkani | gom |
| Hindi | hi |
| Croatian | hr |
| Hungarian | hu |
| Indonesian | id |
| Ingush | inh |
| Icelandic | is |
| Italian | it |
| Japanese | ja |
| Kabardian | kbd |
| Kannada | kn |
| Korean | ko |
| Kurdish | ku |
| Latin | la |
| Lak | lbe |
| Lezghian | lez |
| Lithuanian | lt |
| Latvian | lv |
| Magahi | mah |
