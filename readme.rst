sudo echo "deb http://ftp.fr.debian.org/debian testing main" >> /etc/apt/sources.list

sudo apt-get update
sudo apt-get install -y python3.6

python3.6 -m pip install arcade
