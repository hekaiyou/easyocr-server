# easyocr-server

EasyOCR Server is a python module for extracting text from image. It is a general OCR that can read both natural scene text and dense text in document. are currently supporting 80+ languages and expanding.

## Installation Steps

**Step 0.** Download and install [easyocr-server](https://github.com/hekaiyou/easyocr-server) from the GitHub.

```shell
git clone https://github.com/hekaiyou/easyocr-server.git
```

**Step 1.** Install [easyocr](https://pypi.org/project/easyocr/), [bottle](https://pypi.org/project/bottle/) and [gevent](https://pypi.org/project/gevent/) using PyPI.

```shell
cd easyocr-server
pip install -r requirements.txt
```

## Verify the installation

```shell
python main.py
```

- **Browser**: http://localhost:8080/ocr/
- **CMD**: `curl http://localhost:8080/ocr/ -F "language=en" -F "img_file=@examples/english.png"`

You should be able to see the inference result printed out in the Browser upon successful verification.

![demo.png](https://raw.githubusercontent.com/hekaiyou/easyocr-server/main/examples/demo.png)

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
| Maithili | mai |
| Maori | mi |
| Mongolian | mn |
| Marathi | mr |
| Malay | ms |
| Maltese | mt |
| Nepali | ne |
| Newari | new |
| Dutch | nl |
| Norwegian | no |
| Occitan | oc |
| Pali | pi |
| Polish | pl |
| Portuguese | pt |
| Romanian | ro |
| Russian | ru |
| Serbian (cyrillic) | rs_cyrillic |
| Serbian (latin) | rs_latin |
| Nagpuri | sck |
| Slovak | sk |
| Slovenian | sl |
| Albanian | sq |
| Swedish | sv |
| Swahili | sw |
| Tamil | ta |
| Tabassaran | tab |
| Telugu | te |
| Thai | th |
| Tajik | tjk |
| Tagalog | tl |
| Turkish | tr |
| Uyghur | ug |
| Ukranian | uk |
| Urdu | ur |
| Uzbek | uz |
| Vietnamese | vi |
