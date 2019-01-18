# Download Docker compose
curl -sSL https://raw.githubusercontent.com/bitnami/bitnami-docker-testlink/master/docker-compose.yml > docker-compose.yml
# Start Bitnami Testlink Docker Image
docker-compose up -d
# Updating the latest image of Testlink Docker
docker pull bitnami/testlink:latest
