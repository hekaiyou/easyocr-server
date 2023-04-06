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
    p = Popen(
        ['./venv/Scripts/python', './ocr.py', img_upload_filename, language])
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
            <option value="en">English</option>
            <option value="ch_sim">Simplified Chinese</option>
        </select>
        <p><b>Step 3: </b>Identify image</p>
        <button id="proxySubmit">Process</button>
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
                        success: (res) => {
                            console.log(res);
                        },
                        error: function(err) {
                            console.log(err);
                        }
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
    run(host='0.0.0.0', port=8080, debug=True, server='gevent')
