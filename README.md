# Mel-GAN-Voice-Conversion-Demo
A Demo for real-time voice conversion based on Mel-GAN  
The code is borrowed from https://github.com/marcoppasini/MelGAN-VC  
Reference paper is [MelGAN-VC: Voice Conversion and Audio Style Transfer on arbitrarily long samples using Spectrograms](https://arxiv.org/abs/1910.03713)  

## Package Requirements

>  CUDA 11.0 [Download from here](https://developer.nvidia.com/cuda-11.0-download-archive)  
cudnn 8.0.4 [Download from here](https://developer.nvidia.com/compute/machinelearning/cudnn/secure/8.0.4/11.0_20200923/cudnn-11.0-windows-x64-v8.0.4.30.zip)  
tensorflow 2.4.0  
pytorch 1.7.1  
torchaudio 0.7.2 (CUDA 11.0 cudnn 8.0.4)  
soundfile 0.10.3.post1  
librosa 0.8.1  
numpy 1.19.5  

## Dataset
Dataset used by original paper:[CMU ARCTIC Databases](http://www.festvox.org/cmu_arctic/) includes speech data of 4 speakers, bdl(male), slt(female), clb(female), rms(male)  
We also collected dataset of Trump, and used it to train a VC model which can convert your speech to trump's speech, if you need this trump dataset, please contact me [zengsunlu30@163.com] . The data is not necessarily parallel, neithor for duration of speech, nor for linguistic content of speech.  

## Folders
### models
`/models` provides trained models with different pairs of source speaker and target speaker.  
### results
`/results` stores wave result of converted voice.  
### dataset
`/dataset` provides dataset from different speakers. Speech data is stored in .wav file with 16kHz sample rate.

## Files
### train.py
This file contains entire network architecture, and code from training.  
### test.py
This file contains code from testing, generating results and plotting figures.  
### streamtest.py
This file is the real-time demo for voice conversion. You should run this file through cmd, and make sure your computer has a mic.  

