* 创建私有网络
    * `docker network create --driver=bridge self`
* 部署gitlab
    * 10443
    * 10080
    * 10022
```shell script
docker volume create gitlab-runner-config
docker pull gitlab/gitlab-ce
docker run -d --name gitlab -h gitlab.cza.orz --network=self --network-alias=gitlab.cza.orz -p 443:443 -p 80:80 -p 22:22 -v gitlab-runner-config:/etc/gitlab -v /var/run/docker.sock:/var/run/docker.sock gitlab/gitlab-ce
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
* 部署gitlab-runner
    * `docker pull gitlab/gitlab-runner`
    * `docker volume create gitlab-runner-config`
    * `docker run -d --name gitlab-runner --network=self -v gitlab-runner-config:/etc/gitlab-runner -v /var/run/docker.sock:/var/run/docker.sock gitlab/gitlab-runner`
* 注册gitlab-runner
    * `docker run --rm -it --network=self -v gitlab-runner-config:/etc/gitlab-runner gitlab/gitlab-runner register`
    * 注册过程中需要填入gitlab的地址与token，可以指定自己特殊使用的runner
    * 获取直接使用下面的启动指令执行也可
```shell script
docker run --rm -v /srv/gitlab-runner/config:/etc/gitlab-runner gitlab/gitlab-runner register \
  --non-interactive \
  --executor "docker" \
  --docker-image alpine:latest \
  --url "https://gitlab.com/" \
  --registration-token "PROJECT_REGISTRATION_TOKEN" \
  --description "docker-runner" \
  --tag-list "docker,aws" \
  --run-untagged="true" \
  --locked="false" \
  --access-level="not_protected"
```

```shell script
docker run -d --name gitlab -h 192.168.126.129  -p 443:443 -p 80:80 -p 22:22 -v gitlab-runner-config:/etc/gitlab -v /var/run/docker.sock:/var/run/docker.sock gitlab/gitlab-ce
docker run -d --name gitlab-runner -v gitlab-runner-config:/etc/gitlab-runner -v /var/run/docker.sock:/var/run/docker.sock gitlab/gitlab-runner
docker run --rm -it -v gitlab-runner-config:/etc/gitlab-runner gitlab/gitlab-runner register
```

