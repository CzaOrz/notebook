根据配置文件，定义和运行多个容器  
简单来说就是批量编排启动容器

* services：多个容器
* project：一组关联容器


```text
version: "3.8"  # 不同的docker版本对应的version不一样
services:
    web:
    
volumes:
networks:
configs:

```
