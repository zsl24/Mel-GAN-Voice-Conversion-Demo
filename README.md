# Mel-GAN-Voice-Conversion-Demo
A Demo for real-time voice conversion based on Mel-GAN  
The code is borrowed from https://github.com/marcoppasini/MelGAN-VC  
Reference paper is [MelGAN-VC: Voice Conversion and Audio Style Transfer on arbitrarily long samples using Spectrograms](https://arxiv.org/abs/1910.03713)  

## Package Requirements
CUDA 11.0 [Download for here](https://developer.nvidia.com/cuda-11.0-download-archive)  
cudnn 8.0.4 [Download from here](https://developer.nvidia.com/compute/machinelearning/cudnn/secure/8.0.4/11.0_20200923/cudnn-11.0-windows-x64-v8.0.4.30.zip)  
tensorflow 2.4.0  
pytorch 1.7.1  
torchaudio 0.7.2 (CUDA 11.0 cudnn 8.0.4)  
soundfile 0.10.3.post1  
librosa 0.8.1  
numpy 1.19.5  

## Dataset
Dataset used by original paper:[CMU ARCTIC Databases](http://www.festvox.org/cmu_arctic/) includes speech data of 4 speakers, bdl(male), slt(female), clb(female), rms(male)  
We also collected dataset of Trump, and used it to train a VC model which can convert your speech to trump's speech.  
