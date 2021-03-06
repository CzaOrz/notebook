* 创建私有网络
    * `docker network create --driver=bridge self`
* 部署gitlab
    * 10443
    * 10080
    * 10022
```shell script
docker pull gitlab/gitlab-ce
docker run -d --name gitlab -h gitlab.cza.orz --network=self --network-alias=gitlab.cza.orz -p 10443:443 -p 10080:80 -p 10022:22 gitlab/gitlab-ce
docker exec -it gitlab bash
vim /etc/gitlab/gitlab.rb
---
unicorn['worker_processes'] = 2
unicorn['worker_memory_limit_min'] = "300 * 1 << 20"
unicorn['worker_memory_limit_max'] = "500 * 1 << 20"
sidekiq['concurrency'] = 4
prometheus_monitoring['enable'] = false
postgresql['shared_buffers'] = 256M
---
gitlab-ctl reconfigure
exit
docker restart gitlab
```
登录时指定通用密码，登录账号为root
* 部署jenkins
    * 8800
    * 50000
```shell script
docker pull jenkinsci/blueocean
docker run -u root -d -h jenkins.cza.orz --name jenkins --network=self --network-alias=jenkins.cza.orz -e "JAVA_OPTS=-Xms256m -Xmx768m" -p 8800:8080 -p 50000:50000 jenkinsci/blueocean
docker exec -it jenkins cat /var/jenkins_home/secrets/initialAdminPassword

docker run --rm -u root -it --name jenkins-test --network=self -e "JAVA_OPTS=-Xms256m -Xmx768m" -e DOCKER_TLS_CERTDIR=/certs -v docker-certs-client:/certs/client:ro jenkinsci/blueocean
``` 
创建用户名root，密码为通用密码
* 当你使用window部署jenkins时，可能出现外部无法访问的情况
    * 使用 nginx 作为反向代理，这一步还没有尝试过，可以学nginx的时候试下
    * 添加用户组
        * 打开Administrative Tools，在 CMD 中输入 `shell:common administorative tools`，或者进入这个路径：`C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Administrative Tools`
        * 打开Local Policy，即 本地安全策略
        * 选择 本地策略 - 用户权限分配
        * 点进进去后，选择 作为服务登录
        * 然后将 administrator 加入即可
