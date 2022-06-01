import os
import platform

def pytorch():
    if 'macOS' in platform.platform():
        os.system("conda install pytorch torchvision torchaudio -c pytorch")
    elif 'Linux' in platform.platform():
        print("Check your hardware info:"
              "(1) CPU only"
              "(2) Nvidia GPU <= 20xx"
              "(3) Nvidia GPU >= 30xx")
        user_input = input()
        if '1' in user_input:
            os.system("conda install pytorch torchvision torchaudio cpuonly -c pytorch")
        elif '2' in user_input:
            os.system("conda install pytorch torchvision torchaudio cudatoolkit=10.2 -c pytorch")
        elif '3' in user_input:
            os.system("conda install pytorch torchvision torchaudio cudatoolkit=11.3 -c pytorch")
        else:
            print("Wrong input get, exit.")
            exit(-1)
def basic():
    os.system("conda install matplotlib pandas seaborn timm tensorboardX pillow jieba opencv -c conda-forge\npip install sklearn")