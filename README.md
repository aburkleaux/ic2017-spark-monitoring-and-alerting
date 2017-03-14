# 9005 
Demonstrate using Apache Spark for monitoring, alerting and predictive analytics on Bluemix services

This tutorial will demonstrate using Apache Spark in monitoring and alerting workflows for a cloud SaaS.  

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

### 

## Scenario 2: Log monitoring

Annette is an Operations Engineer for the mini-spark service.  She knows that often the first sign there is a problem with the service comes when there is either excessive logging from one or more of the micro-services that compose her service or the logs suddenly go "silent".  
