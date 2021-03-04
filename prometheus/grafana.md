* grafana
    * 是一个前端展示工具
* DataSource
    * 数据来源，支持Prometheus、Elasticsearch
* DashBoard
* Row
* Panel
* QueryEditor
* Organization

* docker pull prom/prometheus
    * docker run -d --name prometheus -p 9090:9090 -v C:\web\prometheus.yml:/etc/prometheus/prometheus.yml prom/prometheus --config.file=/etc/prometheus/prometheus.yml --web.enable-lifecycle
* docker pull grafana/grafana
    * docker run --name grafana -d -p 3000:3000 grafana/grafana