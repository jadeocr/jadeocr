# One script to set up the repo 

echo 'Downloading datasets...'
wget http://www.nlpr.ia.ac.cn/databases/download/feature_data/HWDB1.1trn.zip -O ../../data/
wget http://www.nlpr.ia.ac.cn/databases/download/feature_data/HWDB1.1tst.zip -O ../../data/
echo 'Downloaded datasets'

echo 'Installing dependencies...'
pip3 install -r ../requirements.txt
echo 'Installed dependencies'

