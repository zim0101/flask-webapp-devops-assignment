COMMIT_HASH=$(git rev-parse --short HEAD)
echo "Commit hash: $COMMIT_HASH"

DOCKER_USERNAME="zim0101"

docker build -t $DOCKER_USERNAME/flask-webapp:$COMMIT_HASH .

docker build -t $DOCKER_USERNAME/flask-webapp:latest .

docker images | grep flask-webapp

docker push $DOCKER_USERNAME/flask-webapp:$COMMIT_HASH

docker push $DOCKER_USERNAME/flask-webapp:latest

echo "Images pushed:"
echo "- $DOCKER_USERNAME/flask-webapp:$COMMIT_HASH"
echo "- $DOCKER_USERNAME/flask-webapp:latest"

docker rmi $DOCKER_USERNAME/flask-webapp:$COMMIT_HASH

docker run -d -p 3000:3000 -e COMMIT_HASH=$COMMIT_HASH --name flask-webapp $DOCKER_USERNAME/flask-webapp:$COMMIT_HASH

sleep 10
curl http://localhost:3000

docker stop flask-webapp && docker rm flask-webapp
