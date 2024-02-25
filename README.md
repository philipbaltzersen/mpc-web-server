# Simple web server

This project creates a web server using FastAPI and deploys it to EC2 using Docker and NGINX. 


## EC2 set-up
- Create an t4g.nano instance (cheapest arm-based instance) with Ubuntu 22.04 and a 8GiB gp3 volume.
- Ensure that the EC2 instance is deployed into a public subnet and has the correct CIDR block whitelisted for SSH access.
- Remember to `chmod 400` the private key

- Install Docker:
```bash
sudo apt update
sudo apt upgrade

# Add Docker's official GPG key:
sudo apt update
sudo apt install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update

sudo apt install docker-ce docker-ce-cli containerd.io

# Enable running Docker as non-root
sudo groupadd docker
sudo usermod -aG docker ubuntu
# Need to reconnect for changes to take effect
exit

# Verify installation worked
sudo docker run hello-world
```

- Install NGINX: `sudo apt install nginx`
- Create NGINX config file: `sudo nano /etc/nginx/sites-enabled/fastapi-web-server`
- Add the following:
```
server {
    listen 80;
    server_name <PUBLIC_IP>;
    location / {
        proxy_pass http://127.0.0.1:8000;
    }
}
```
- Restart NGINX: `sudo service nginx restart`
- Create a private key for connection to GitHub
```
cd .ssh
ssh-keygen -t ed25519 -C "my_email@mail.com"
ssh-add github
```
- Add `github.pub` to SSH keys in GitHub settings
- Clone repository: `git clone git@github.com:philipbaltzersen/fastapi_web_server.git`
- Build Docker image `docker build . -t server`
- Run container: `docker run --name server -d server`
