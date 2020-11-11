常用指令：（http://www.ruanyifeng.com/blog/2019/09/curl-reference.html）
* -A: 指定User-Agent，也可以通过 -H 直接指定请求行的形式来指定User-Agent
    * `curl -A 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36' https://www.baidu.com`
* -a: upload文件的时候，可以附件到目标文件
* -b: 添加cookie
    * `curl -b 'foo=bar' https://google.com`
    * `curl -b 'foo1=bar;foo2=bar2' https://google.com` 这种请求
* -d: 在http-post请求时指定数据
* -D: 将接收到的response的headers写到文件中
* -F: 指定表单数据
    * `curl -F password=@/etc/passwd www.url.com`  表单数据的密码在/etc/passwd路劲下
    * `curl -F "name=daniel;type=text/foo" www.url.com`  指定表单数据name和type
    * `curl -F "file=@localfile;filename=nameinpost" www.url.com`  支持分开指定数据
* -G: 表示请求使用Get方法，默认就是Get请求
    * `curl https://www.baidu.com`
* -H: 指定headers
    * `curl -H "Content-Type: application/json" www.url.com`  支持分开指定数据
* -h: 
* -i: 
* -k: 
* -j: 
* -l: 
* -L: 
* -M: 
* -m: 
* -n: 
* -N: 
* -o: 
* -x: 
* -U: 
* -p: 