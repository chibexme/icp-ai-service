# icp-ai-service

run the dev server:
```commandline
uvicorn main:app --port 8080 --reload
```

# build the image and run the container
```commandline
docker build -t "tag" .
```
Make sure to edit the `environment` section of the `docker-compose.yaml` file.
Start the server and postgresql db using compose
```commandline
docker-compose -f docker-compose.yaml up -d
```

# Deploy via Dockerfile to fly.io
Based on this https://fly.io/docs/languages-and-frameworks/dockerfile/

The launch command is optional since there is a `fly.toml` file already
```commandline
fly launch --no-deploy
```
create a `fly-secrets.sh` file and add the following:
```text
flyctl secrets set SECRET_KEY='' CL_NAME="" CL_API_KEY="" CL_SECRET="" DB_URL='' EMAIL_CLIENT_NAME='' M_MAIL_KEY='' Z_MAIL_KEY='' SENDER_EMAIL=''
fly secrets list
```
run the bash file to create the secrets
```commandline
bash fly-secrets.sh
```
deploy app
```commandline
fly deploy --ha=false
```
scale the memory
```commandline
flyctl scale memory 2048 -a termitebk
```
scale the vm
```commandline
fly scale vm shared-cpu-2x --vm-memory 4096 -a termitebk
```