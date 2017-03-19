# Hands-on Lab Session 9005
## Demonstrate Monitoring, Alerting and Predictive analytics for IBM Bluemix Cloud Services using Spark

## Lab Instructions

This lab assumes you are starting from a host VM that has been preconfigured for the lab.  Let's get started!!

### Setup
1. Open a terminal from window the sidebar of the VM desktop and type the following command.  You will be running as **localuser**.  If you are prompted for a sudoer password enter **passw0rd**:

    cd ic2017-spark-monitoring-and-alerting
    git pull
    sh start.sh

2. Open the Firefox web browser
3. Open a browser tab and open the Zeppelin console: http://localhost:8080
4. Open a second broswer tab and open the Grafana console: http://localhost:3000

### Run the Zeppelin notebook

From the Zeppelin tab in you browser:

1. Click on **Import Note** from the home screen.

![Import note image](https://github.com/aburkleaux/ic2017-spark-monitoring-and-alerting/blob/master/images/z-importnote.png)

2. From the **Import** New Note box select **Choose a JSON here**

3. In the File Upload window, navigate to **localuser/ic2017-spark-monitoring-and-alerting** folder

4. Doubleclick on **ic2017-notebook-usage.json**

![select JSON](https://github.com/aburkleaux/ic2017-spark-monitoring-and-alerting/blob/master/images/z-selectNotebook.png)

5. The notebook titled ic2017-notebook-usage should now be loaded in your browser.  Click on the play button and answer "yes" to play all cells.

6. Follow along in the notebook to get an overview of how you can transform timestamped event data into metrics using Spark.

#### How to use Zeppelin

* Execute cells using **Shift+Enter**
* Add a cell by clicking on the '+' character between cells

The first line of each cell tells Zeppelin what language you are going to use.  

* %md for markdown
* %sql for sql
* %python for python
* %pyspark for python with spark
   

Feel free to write your own code to explore the dataset!!

### Load and Explore the Grafana dashboard

The grafana dashboard shows how you can use the [graphite Holt-Winters](http://graphite.readthedocs.io/en/latest/functions.html) forecast API to perform Anomaly Detection on a timeseries.    

1. Open the browser tab with the Grafana console
2. Click on the Grafana Swirling Fire Icon in the top left corner of the page.
3. Hover over the **Dashboards** menu item then click on **Import** from the sub-menu
4. Click on **Upload .json file** from the Import Dashboard window
5. In the File Upload window, navigate to **localuser/ic2017-spark-monitoring-and-alerting** folder
6. Doubleclick on **ic2017-grafana-usage-export.json**

![select JSON](https://github.com/aburkleaux/ic2017-spark-monitoring-and-alerting/blob/master/images/g-select-dashboard.png)

5. The dashboard titled ic2017-grafana-usage should now be loaded in your browser.  

The dashboard visualizes the metrics we generated in the notebook, along with a Holt-Winters predictive model of the expected values of the timeseries.

* You can zoom in and out by adjusting the timepicker in the upper right corner of the dashboard.
* Click on the title bar of each graph to see how the graph was implemented using the metrics we stored in graphite and the graphite API.
* You can also toggle between different users using the users button at the top of the dashboard.
 




 
