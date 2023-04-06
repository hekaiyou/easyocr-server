import os
from gevent import monkey

monkey.patch_all()
from time import time, sleep
from bottle import request, run, post, get
from subprocess import Popen
from json import load


@post('/ocr/')
def ocr_post():
    language = request.forms.get('language', 'ch_sim,en')
    upload_file = request.files.get('img_file')
    img_upload_filename = f'upload/{"".join(str(time()).split("."))}'
    upload_file.save(img_upload_filename, overwrite=True)
    print(f'启动 {img_upload_filename} OCR 进程')
    p = Popen(['python', './ocr.py', img_upload_filename, language])
    while not os.path.exists(f'{img_upload_filename}.json'):
        sleep(1)
    print(f'完成 {img_upload_filename} OCR 进程')
    with open(f'{img_upload_filename}.json', 'r', encoding='UTF-8') as f:
        ocr_results = load(f)
    print(f'关闭 {img_upload_filename} OCR 进程')
    p.terminate()
    os.remove(img_upload_filename)
    os.remove(f'{img_upload_filename}.json')
    return ocr_results


@get('/ocr/')
def curtain_get():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>EasyOCR</title>
        <script src="https://apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js"></script>
    </head>
    <body>
        <h1>EasyOCR Demo</h1>
        <p><b>Step 1: </b>Choose image file</p>
        <input type="file" id="imgFile" placeholder="image file: jpg, png, tiff only" />
        <p><b>Step 2: </b>Enter Language Codes</p>
        <select id="language" value="en">
            <option value="abq">Abaza</option>
            <option value="ady">Adyghe</option>
            <option value="af">Afrikaans</option>
            <option value="ang">Angika</option>
            <option value="ar">Arabic</option>
            <option value="as">Assamese</option>
            <option value="ava">Avar</option>
            <option value="az">Azerbaijani</option>
            <option value="be">Belarusian</option>
            <option value="bg">Bulgarian</option>
            <option value="bh">Bihari</option>
            <option value="bho">Bhojpuri</option>
            <option value="bn">Bengali</option>
            <option value="bs">Bosnian</option>
            <option value="ch_sim">Simplified Chinese</option>
            <option value="ch_tra">Traditional Chinese</option>
            <option value="che">Chechen</option>
            <option value="cs">Czech</option>
            <option value="cy">Welsh</option>
            <option value="da">Danish</option>
            <option value="dar">Dargwa</option>
            <option value="de">German</option>
            <option value="en">English</option>
            <option value="es">Spanish</option>
            <option value="et">Estonian</option>
            <option value="fa">Persian (Farsi)</option>
            <option value="fr">French</option>
            <option value="ga">Irish</option>
            <option value="gom">Goan Konkani</option>
            <option value="hi">Hindi</option>
            <option value="hr">Croatian</option>
            <option value="hu">Hungarian</option>
            <option value="id">Indonesian</option>
            <option value="inh">Ingush</option>
            <option value="is">Icelandic</option>
            <option value="it">Italian</option>
            <option value="ja">Japanese</option>
            <option value="kbd">Kabardian</option>
            <option value="kn">Kannada</option>
            <option value="ko">Korean</option>
            <option value="ku">Kurdish</option>
            <option value="la">Latin</option>
            <option value="lbe">Lak</option>
            <option value="lez">Lezghian</option>
            <option value="lt">Lithuanian</option>
            <option value="lv">Latvian</option>
            <option value="mah">Magahi</option>
            <option value="mai">Maithili</option>
            <option value="mi">Maori</option>
            <option value="mn">Mongolian</option>
            <option value="mr">Marathi</option>
            <option value="ms">Malay</option>
            <option value="mt">Maltese</option>
            <option value="ne">Nepali</option>
            <option value="new">Newari</option>
            <option value="nl">Dutch</option>
            <option value="no">Norwegian</option>
            <option value="oc">Occitan</option>
            <option value="pi">Pali</option>
            <option value="pl">Polish</option>
            <option value="pt">Portuguese</option>
            <option value="ro">Romanian</option>
            <option value="ru">Russian</option>
            <option value="rs_cyrillic">Serbian (cyrillic)</option>
            <option value="rs_latin">Serbian (latin)</option>
            <option value="sck">Nagpuri</option>
            <option value="sk">Slovak</option>
            <option value="sl">Slovenian</option>
            <option value="sq">Albanian</option>
            <option value="sv">Swedish</option>
            <option value="sw">Swahili</option>
            <option value="ta">Tamil</option>
            <option value="tab">Tabassaran</option>
            <option value="te">Telugu</option>
            <option value="th">Thai</option>
            <option value="tjk">Tajik</option>
            <option value="tl">Tagalog</option>
            <option value="tr">Turkish</option>
            <option value="ug">Uyghur</option>
            <option value="uk">Ukranian</option>
            <option value="ur">Urdu</option>
            <option value="uz">Uzbek</option>
            <option value="vi">Vietnamese</option>
        </select>
        <p><b>Step 3: </b>Identify image</p>
        <button id="proxySubmit">Process</button>
        <p><b>Step 4: </b>Check OCR results</p>
        <textarea id="results" rows="20" cols="60"></textarea>
        <script type="text/javascript">
            $(function () {
                $('#proxySubmit').on('click', function(e) {
                    let files = $("#imgFile")[0].files;
                    if (files.length <= 0) {
                        return alert('Please choose image file');
                    }
                    var formData = new FormData();  // 创建formData数据格式, 传递HTML对象
                    // 把传递给服务器数据, 追加到formData对象里面
                    formData.append('img_file', files[0]);
                    formData.append('language', $('#language').val());
                    // 发送请求
                    $.ajax({
                        url: '/ocr/',
                        type: 'post',
                        contentType:false, // 不修改contentType, 使用FormData默认的
                        processData:false,  //不对FormData中的数据进行url编码, 而是将FormData数据原样上传到服务器
                        cache: false,
                        data: formData,
                        beforeSend: function() {
                            $('#proxySubmit').attr('disabled', true);
                        },
                        success: (res) => {
                            $("#results").val(JSON.stringify(res, null, 4));
                        },
                        error: function(err) {
                            $("#results").val(err);
                        },
                        complete: function() {
                            $('#proxySubmit').removeAttr('disabled');
                        },
                    })
                });
            });
        </script>
    </body>
    </html>
    '''


if __name__ == '__main__':
    # Browser: http://localhost:8080/ocr/
    # CMD: curl http://localhost:8080/ocr/ -F "language=en" -F "img_file=@examples/english.png"
    run(host='0.0.0.0', port=8080, debug=False, server='gevent')
