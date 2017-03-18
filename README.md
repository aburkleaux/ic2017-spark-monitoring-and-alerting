# Hands-on Lab Session 9005
## Demonstrate Monitoring, Alerting and Predictive analytics for IBM Bluemix Cloud Services using Spark

![alerts with Spark](https://github.com/aburkleaux/ic2017-spark-monitoring-and-alerting/blob/master/images/g-forecasting-robert.png "Metrics with Spark")

**Overview**

This lab will take you through a simplified scenario for monitoring usage of a cloud service.  It will demonstrate the workflow using Spark to tranform any kind of timestamped data into metrics. We will also look at how the metrics can be used as the basis for creating alerts on usage and forecasting usage behavior for our service.

**Tools Used**

* **Apache Zeppelin** - is a web-based notebook that enables interactive data analytics. You can make beautiful data-driven, interactive and collaborative documents with SQL, Scala and more. Official Website for Apache Zeppelin is http://zeppelin.apache.org [ref](zeppelin-project.org/)

* **Spark** is a fast, in-memory data processing engine with elegant and expressive development APIs to allow data workers to efficiently execute streaming, machine learning or SQL workloads that require fast iterative access to datasets. [ref](spark.apache.org/)

* **Graphite** is a highly scalable real-time graphing system. As a user, you write an application that collects numeric time-series data that you are interested in graphing, and send it to Graphite's processing backend, carbon, which stores the data in Graphite's specialized database. [ref](graphite.wikidot.com/faq)

* **Grafana** is an open source metric analytics & visualization suite. It is most commonly used for visualizing time series data for infrastructure and application analytics but many use it in other domains including industrial sensors, home automation, weather, and process control. [ref](https://docs.grafana.org/)

**Scenario: Monitoring usage of a Bluemix Service**

Prashant is a Customer Success Manager for the (fictional) CloudKat service on Bluemix.  He wants to monitor the usage patterns of service users in order to identify touchpoints to nurture the customer relationship. Specifically, he wants to be notified whenever:

* a users utilization of the service approaches the limit for their current plan
* a user has a change in usage pattern that decreases the use of their service
* a user has actively used the service for certain number of days

**Data Flow for analytic processing**

We'll be showing tranforming timestamped event data using Spark in a Zeppelin notebook and creating Holt-Winters Forecasts using graphite and grafana.  THe general analytic workflow this might fit into looks like this:

![alerts with Spark](https://github.com/aburkleaux/ic2017-spark-monitoring-and-alerting/blob/master/images/dataflow.png "Dataflow")

Data is ingested through a log management system such as Logstash in and ELK stack and written to a presisitent message BUS such as Kafka.  Event data is processed from the stream to be stored or passed to downstream processiong.  One the data are persisited, it can be accessed by batch jobs or applications.  Some batch jobs may create results that will also be persisted in the data store.  We will show an example of such a job in the notebook.

Spark can serve the processing engine for streaming an stored data from every datasource.
