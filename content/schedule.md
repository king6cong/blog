Title: Schedule
Date: 2010-12-03 10:20
Category: Tech
Tags: Python

#project *bungee*

#Bungeer项目的诞生

##server
a. server
   1. restful
   2. nginx
   3. to-do
   
##client
a. web
   1. jquery/bootstrap
   2. nodejs
b. app
   1. ios 
   2. android

##res
1. pic
2. relation

##mng
1. scm git
2. python supervisor 





###python:
yaourt -S python2-pip

###virtualenv: http://www.virtualenv.org/en/latest/
sudo pip2 install virtualenv
virtualenv ENV
virtualenv --system-site-packages ENV
virtualenv --distribute ENV
virtualenv --extra-search-dir=/path/to/dists --extra-search-dir=/path/to/other/dists ENV
source bin/activate
deactivate

###pip-tools
https://github.com/nvie/pip-tools
pip install pip-tools

###gevent https://github.com/surfly/gevent
pip install cython -e git://github.com/surfly/gevent.git@1.0rc2#egg=gevent


###git


###gunicorn http://gunicorn.org
pip install gunicorn
gunicorn -w 4 -b :5000 fv:app


###nginx
pacman -S nginx

###flask
pip install Flask
pip install -e 'git+http://github.com/sjl/flask-lesscss.git@v0.9.1#egg=flask-lesscss'

pip install Flask-Coffee

pip install flask-security flask-sqlalchemy

###coffee
sudo npm install -g coffee-script


###less http://lesscss.org/
sudo npm install -g less
lessc styles.less styles.css


###pip tips
pip uninstall flask-lesscss

###https://github.com/blueimp/jQuery-File-Upload

###https://github.com/blueimp/JavaScript-Load-Image
###https://github.com/blueimp/JavaScript-Canvas-to-Blob

###riak
pip install riak

###celery

pip install -U Celery

###redis
pip install redis

###rabbitmq
yaourt  -S rabbitmq
pip install librabbitmq

###flake8
pip install flake8

###Fabric http://docs.fabfile.org
pip install fabric
fab -i /mnt/air/Dropbox/diary/king6cong.pem -H localhost,www.chuckjane.com -f fabric_test.py host_type
fab -f fabric_test.py host_type


###git
git config --global user.name "king6cong"
git config --global user.email king6cong@gmail.com

git config --global core.editor vim

git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.up rebase
git config --global alias.ci commit

git config --global --edit
git log --author="John Smith" -p hello.py
git log --oneline master..some-feature
git log --grep="<pattern>"
git log -p
git log --stat
git log --oneline
git log -n <limit>

###http://python-rq.org
pip install rq



###git tips
mkdir /path/to/your/project
git init
git remote add origin https://king6cong@bitbucket.org/king6cong/bungee.git

git remote add origin https://king6cong@bitbucket.org/king6cong/bungee.git
git push -u origin --all   # to push changes for the first time

git reset --hard
git clean -f
git clean -dfx

git branch
git branch <branch>
git branch -d <branch>
git branch -D <branch>
git branch -m <branch>

git checkout <commit> <file>
git checkout <commit>
git checkout <existing-branch>
git checkout -b <new-branch>
git checkout -b <new-branch> <existing-branch>

git commit --amend
git commit --amend --no-edit
android update adb

git remote
git remote -v
git remote add <name> <url>
git remote rm <name>
git remote rename <old-name> <new-name>

git checkout master
git fetch origin master
git rebase -i origin/master
# Squash commits, fix up commit messages etc.
git push origin master

git clone git@github.com:king6cong/flask.git

###pelican https://github.com/getpelican/pelican
pip install pelican Markdown
pip install ghp-import

###nltk
sudo pip install -U pyyaml nltk
python -m nltk.downloader -d /Users/cong/store/nltk

###sass
gem install sass

###PyMC
pip install pymc

sudo pacman -S gcc-fortran

###popup
http://dimsemenov.com/plugins/magnific-popup/

sudo pip install requests
sudo pip install scrapy
sudo pip install ujson
sudo pip install beautifulsoup4


sudo pacman -S sqlite
sudo pacman -S svn

svn checkout http://py-leveldb.googlecode.com/svn/trunk/ py-leveldb-read-only
cd py-leveldb-read-only
./compile_leveldb.sh
python setup.py build
sudo python setup.py install

gunicorn gserver:http_server -k gevent -b 127.0.0.1:80
gunicorn app:app -k gevent -b 0.0.0.0:80 --debug
scp redis_3888.rdb root@107.20.212.56:/root





###basic
play video
1. iqiyi youku tudou sohu qq sina || mp4 m3u8 flv || stream download || notify || continue || web android ios
2. comment || chat
3. tv


PYTHONUNBUFFERED


sudo pacman -S nginx


pip install Flask-Mail

