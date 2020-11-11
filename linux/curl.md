常用指令：（http://www.ruanyifeng.com/blog/2019/09/curl-reference.html）
* -A: 指定User-Agent，也可以通过 -H 直接指定请求行的形式来指定User-Agent
    * `curl -A 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36' https://www.baidu.com`
* -a: upload文件的时候，可以附件到目标文件
* -b: 添加cookie
    * `curl -b 'foo=bar' https://google.com`
    * `curl -b 'foo1=bar;foo2=bar2' https://google.com` 这种请求
    * `curl -b cookies.txt https://www.google.com` 读取文件中的cookie，文件可以通过 -c 指令生成
* -c: 将响应的cookies写到文件中
    * `curl -c cookies.txt https://www.google.com`
* -d: 在http-post请求时指定数据，使用该参数后，会默认指定Content-Type : application/x-www-form-urlencoded，而且会默认指定 -X 为 Post 请求
    * `curl -d'login=emma＆password=123'-X POST https://google.com/login` 这里 -X 可以指定请求方式
    * `curl -d 'login=emma' -d 'password=123' -X POST  https://google.com/login` 也可以指定多次
    * `curl -d '@data.txt' https://google.com/login` 可以通过 @ 指定存储数据的文件
* --data-urlencode: 该参数与 -d 相同，不过会自动将要发送的数据进行 URL 编码
    * `curl --data-urlencode 'comment=hello world' https://google.com/login`
* -e: 可以设置 Referer，表示请求来源，也可以通过 -H 指定请求头
    * `curl -e 'https://google.com?q=example' https://www.example.com`
* -D: 将接收到的response的headers写到文件中
* -F: 指定文件并上传
    * `curl -F 'file=@photo.png' https://google.com/profile` 上传文件，这种就是作为二进制文件传递，此时会附带 `Content-Type: multipart/form-data` 请求头，并将这张图片作为file字段上传
    * `curl -F 'file=@photo.png;filename=me.png' https://google.com/profile` 可以修改上传参数，此时文件原名则会忽略，服务器接收到的名字为filename指定的名字
    * `curl -F 'file=@photo.png;type=image/png' https://google.com/profile` 可以指定类型，此时则会附带`application/octet-stream`的请求头
    * `curl -F password=@/etc/passwd www.url.com`  表单数据的密码在/etc/passwd路劲下
    * `curl -F "name=daniel;type=text/foo" www.url.com`  指定表单数据name和type
    * `curl -F "file=@localfile;filename=nameinpost" www.url.com`  支持分开指定数据
* -G: 表示请求使用Get方法，默认就是Get请求
    * `curl -G -d 'q=kitties' -d 'count=20' https://google.com/search` 若此时不指定 -G，则该此请求会被作为POST请求处理，此处指定了-G，则该次请求为GET请求，并且-d的参数会作为Get请求的参数传递
    * `curl -G --data-urlencode 'comment=hello world' https://www.example.com` 如果需要url编码，还可以指定`--data-urlencode`
* -H: 指定headers
    * `curl -H "Content-Type: application/json" www.url.com` 支持分开指定数据
    * `curl -H 'Accept-Language: en-US' -H 'Secret-Message: xyzzy' https://google.com` 可以指定多次-H
    * `curl -d '{"login": "emma", "pass": "123"}' -H 'Content-Type: application/json' https://google.com/login` 通过-H指定请求类型为JSON，然后通过-d指定传递的数据
* -i: 打印出响应的报文
    * `curl -i https://www.example.com`
* -I: 打印出部分响应报文，不包括body部分
* -k: 跳过 ssl 证书的验证
    * `curl -k https://www.example.com`
* -L: 让请求跟随重定向，默认是不跟随重定向
    * `curl -L -d 'tweet=hi' https://api.twitter.com/tweet`
* --limit-rate: 限定响应速度，模拟低宽带
    * `curl --limit-rate 200k https://google.com`
* -u: 用于指定请求的账号与密码
    * `curl -u 'bob:12345' https://google.com/login` 会自动将其转化为Authorization: Basic Ym9iOjEyMzQ1
* -v: 输出通信的整个过程。包括请求报文和响应报文
* -o: 将结果保存到目标问价中，等同与wget指令
    * `curl -o example.html https://www.example.com`
* -O: 将结果保存到文件中，不需要指定文件名，会自动将保存
    * `curl -O https://www.example.com/foo/bar.html` 
* -x: 指定请求的代理
* -X: 指定请求方式