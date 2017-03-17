echo "Starting containers"
sudo docker run -d --net=host apsm/graphite_ic
sudo docker run -d --net=host -e GF_AUTH_ANONYMOUS_ENABLED=true -e GF_AUTH_ANONYMOUS_ORG_ROLE=Admin apsm/grafana
sudo docker run -d --net=host -v /shared/data:/shared/data apsm/zeppelin

sudo docker ps

echo "Preparing data files"
cd /home/localuser/ic2017-spark-monitoring-and-alerting
gunzip faker-user-jobs.csv.gz
cp faker-user-jobs.csv /shared/data  

echo "Configuring grafana"
python util/setup_grafana.py

