# Kong API Gateway Test Drive

This repository contains files after a test drive of [Kong API gateway](https://konghq.com/community/). It was meant to better understand the available capabilities and functionality. The current setup uses declarative configuration that does not allow configuring Kong over administrative API (does not use database).

## Getting Started

```bash
# start services
make up

# stop services and clean environment
make down

# restart Kong after configuration updates
make restart-kong
```

## References

- [kong Docker Image](https://hub.docker.com/_/kong)
- [Kong Docs](https://docs.konghq.com/)
- [DB-less and Declarative Configuration](https://docs.konghq.com/gateway-oss/2.3.x/db-less-and-declarative-config/)
- [Prometheus Plugin](https://docs.konghq.com/hub/kong-inc/prometheus/)
- [Kong Grafana Dashboard](https://grafana.com/grafana/dashboards/7424)
- [Kong API Gateway – Observability with Prometheus, Grafana and OpsGenie](https://blog.codecentric.de/en/2019/12/kong-api-gateway-observability-with-prometheus-grafana-and-opsgenie/)
- [How-to - Kong with Keycloak](https://ncarlier.gitbooks.io/oss-api-management/content/howto-kong_with_keycloak.html)