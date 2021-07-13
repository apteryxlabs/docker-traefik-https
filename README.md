

# FastAPI-Docker-Traefik-HTTPS
<p align=center>
<img src="static/images/apteryx_logo.jpg" alt="" width=100> <img src="static/images/plus.svg" alt="" width=100> <img src="static/images/fastapi.svg" alt="" width=100>
</p>


This is a cookiecutter template for quickly generating https-compatible FastAPI web apps. It pre-configures [Traefik](https://doc.traefik.io/traefik/) and the relevant [Docker Compose](https://docs.docker.com/compose/) files to save you time writing boilerplate. We wrote it to save time when deploying new APIs, while keeping things secure. 

This does NOT write your site for you - that would be magic 🧙

## Usage
If you haven't yet installed [cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/installation.html):
```
brew install cookiecutter
```
Then:
```
cd [your_preferred_dev_location_here]
cookiecutter https://github.com/apteryxlabs/fastapi-docker-traefik-https.git
```

You'll be asked a bunch of questions to scaffold our your site. When everything is done, cd into your newly-create project directory, open your IDE of choice, and start writing you app!

## Deployment
Make sure you have
<ol>
<li>A server capable of running docker and docker-compose</li>
<li>A static IP address for that server</li>
<li>A domain name (like example.com) that points to that server's IP address</li>
<li>The ability to ssh to that server as root</li>
</ol>
Once you've done this, the rest should be as simple as:

```
# Sync everything except hidden files
rsync -a ./* root@your.domain.com:/path/to/server/code/dir

# Copy your .env file
scp .env root@your.domain.com:/path/to/server/code/dir/.env

# IN THE REMOTE SERVER:
# Build the traefik service:
docker-compose -f docker-compose.traefik.yml up -d

# Build the app:
docker-compose -f docker-compose.yaml up -d
```

## Questions?
Please open an issue, and we'll try to get back in a timely manner.

## License

This project is licensed under the terms of the MIT license.
