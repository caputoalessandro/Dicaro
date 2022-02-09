function run_docker() {
  if [ $(docker inspect -f '{{.State.Running}}' 'testneo4j') = "true" ];
  then echo "container in esecuzione";
  else
#    docker run --name testneo4j -d -p 7474:7474 -p7687:7687 -e NEO4J_AUTH=neo4j/test neo4j
    docker start testneo4j
    sleep 5
    echo "container avviato";
    fi
}
