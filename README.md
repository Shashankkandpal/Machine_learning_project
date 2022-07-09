# Machine_learning_project
 ## Start Machine Learning Project.

### Software and Account Requirement.

1. [Github Account](https://github.com)
2. [Heroku Account]( https://dashboard.heroku.com/login)
3. [VS code IDE]( https://code.visualstudi.com/download)
4. [GIT cli](https://git-scm.com/downloads)
5. [GIT Documentation](https://git-scm.com/docs/gittutorial)


Creating conda environment
```
conda create -p venv python==3.7 -y
(-y means we are saying yes, when it asks yes or no before hand only )
( -p means it will create virtual environment in the same project folder , advantage of
which is when you will delete project folder , venv will also get deleted will not occupy
additional space in your system)
(-n in place of -p will create the virtual environment in anaconda directory)
```
```
conda activate venv/
```
OR
```
conda activate venv
```

```
pip install -r requirements.txt
```
To Add files to git
```
git add .
```

OR
```
git add <file_name>
```

> Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status 
```
git status
```
To check all version maintained by git
```
git log
```

To create version/commit all changes by git
```
git commit -m "message"
```

To send version/changes to github
```
git push origin main
```

To check remote url 
```
git remote -v
```

To setup CI/CD pipeline in heroku we need 3 information
1. HEROKU_EMAIL = anishyadav7045075175@gmail.com
2. HEROKU_API_KEY = <>
3. HEROKU_APP_NAME = ml-regression-app

BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
```
> Note: Image name for docker must be lowercase


To list docker image
```
docker images
```

Run docker image
```
docker run -p 5000:5000 -e PORT=5000 f8c749e73678
```

To check running container in docker
```
docker ps
```

Tos stop docker conatiner
```
docker stop <container_id>
```



```
python setup.py install
```


Install ipykernel

```
pip install ipykernel
```


Data Drift:
When your datset stats gets change we call it as data drift
