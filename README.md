# 9005 Demonstrate Monitoring, Alerting and Predictive analytics for IBM Bluemix Cloud Services using Spark

This tutorial will demonstrate using Apache Spark in monitoring and alerting workflows for a cloud SaaS.  At the end of this tutorial you will be able to:
* understand a typical monitoring and alerting workflow
* understand how some of the features of Spark can fit into monitoring and analytic workflows
* how advanced analytic techniques such as timeseries forecasting can be used for monitoring and alerting

While we will be using some analytic libraries to forecast or predict values for our metrics, the details of forecasting and predictive analytics are beyond the scope of this lab.  We hope that you will take away a better feel for how these techniques can be used in a fairly generic series of data processing tasks in the moniroing and alerting workflow.

**Tools:**

Apache Spark
Zeppelin Notebooks
Graphite
Grafana
Docker - for setting up the environment

**Setup:***

got to github
get the container
run the container

## Scenario 1: Customer Success

Prashant is a Customer Success Manager for the mini-spark service.  He wants to monitor the usage patterns of service users in order to identify touchpoints to nurture the customer relationship. Specifically, he wants to be notified whenever:
* a users utilization of the service approaches the limit for their current plan
* a user has a change in usage pattern that decreases the use of their service
* a user has actively used the service for certain number of days
* a user has experienced a high number of problems using the service

### The data:

Users of the service are billed per job run on the service.  Job counts are kept by the metering micro-service and sent to the billing system on a regular basis.  The metering service also logs more detailed job information in case they ever need to debug issues with the billing system. This analysis will use the detailed billing data which is stored in JSON format in the log management system.

FIXME: sample raw data here

Raw JSON data is processed daily by parsing out timestamped events and storing them in csv files. (NOTE: this step would actually be done as part of the data pipeline, but is done from csv to resuce the amount of data needed for this lab).

FIXME: csv file

### Explore the data:

Show jobs over time for all users and by user
Show age of users over time
Show jobs that didn't complete

### Use Spark SQL to transform event data into metrics:

Utilization - active jobs

### Use Spark to aggregate historical data within a window 

Days of active use within the last 30 days
Days since active use in the last 30 days
Jobs with no finish after 5 hours in last 3 days

### Simple anamoly detection on tranformed metrics using graphite holt-winters forecasting

### What if we don't want holt-winters?  Use spark-ts package to calculate the anaomaly metric

### Scale out 

What if our service become extremely popular or we want to start processing data for multiple services on our platform?  We can use spark to scale out by partitioning our data across multiple spark workers.

### Speed up with Streams 

What if we want to decrease the time interval that we use to process data from daily down to every minute?

## Scenario 2: Log monitoring

Annette is an Operations Engineer for the mini-spark service.  She knows that often the first sign there is a problem with the service comes when there is either excessive logging from one or more of the micro-services that compose her service or the logs suddenly go "silent".  She wants an alert when the logging rate for her service goes above or below a threshold or is anomalous for the for the time of day.

### The data

All of the log data for the service passes through parsers which transform the data into the following format.  

### Explore the data:


### Use Spark SQL to transform event data into metrics:

Calculates the logging rate at fixed intervals.

### Set fixed upper and lower bounds - visualize in grafana

### Do anomaly detection using holt-winters in graphite

### Do anomlaly detection using ARIMA in spark-ts




