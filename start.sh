echo "Starting containers"
sudo docker run -d --net=host apsm/graphite_ic
sudo docker run -d --net=host -e GF_AUTH_ANONYMOUS_ENABLED=true -e GF_AUTH_ANONYMOUS_ORG_ROLE=Admin apsm/grafana
sudo docker run -d --net=host -v /shared/data:/shared/data apsm/zeppelin

sudo docker ps

echo "Preparing data files"
cd /home/localuser/ic2017-spark-monitoring-and-alerting
#gunzip faker-user-jobs.csv.gz
cp faker-user-jobs.csv /shared/data  

sleep(5)

echo "Configuring grafana"
curl 'http://localhost:3000/api/datasources' -X POST -H 'Content-Type: application/json;charset=UTF-8' --data-binary '{"name":"ic2017","type":"graphite","url":"http://localhost:80","access":"proxy","isDefault":true}'
