echo 'Grabbing files...'
git clone 'https://github.com/TanayB11/chinese-ocr.git'
cd convnet

echo 'About to install TF GPU and CUDA libraries...'
tput setaf 1; echo 'THIS WILL INSTALL ABOUT 3GB OF DATA!'
tput setaf 1; echo 'EXIT WITH CTRL + Z IF YOU DO NOT WISH TO CONTINUE!'

sleep 2
echo 'CONTINUING...'
sleep 3

echo 'Installing TF GPU and CUDA libraries...'
export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-0.12.1-cp27-none-linux_x86_64.whl
sudo pip3 install --upgrade $TF_BINARY_URL
wget "http://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/cuda-repo-ubuntu1604_8.0.44-1_amd64.deb"
sudo dpkg -i cuda-repo-ubuntu1604_8.0.44-1_amd64.deb
sudo apt-get update
sudo apt-get install cuda

echo 'Installing cuDNN for Linux...'
sudo tar -xvf cudnn-8.0-linux-x64-v5.1.tgz -C /usr/local
export PATH=/usr/local/cuda/bin:$PATH
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/local/cuda/lib64:/usr/local/cuda/extras/CUPTI/lib64"
export CUDA_HOME=/usr/local/cuda

echo 'Installing dependencies...'
pip3 install -r requirements.txt

echo 'Running GPU test...'
cd src/gpu-test
python3 gpu-test.py

echo 'Tests complete!'