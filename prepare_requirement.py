import os
import platform

def pytorch_installation():
    if 'macOS' in platform.platform():
        os.system("sh ./prepare_requirement/pytorch_default.sh")
    elif 'Linux' in platform.platform():
        print("Check your hardware info:"
              "(1) CPU only"
              "(2) Nvidia GPU <= 20xx"
              "(3) Nvidia GPU >= 30xx")
        user_input = input()
        if '1' in user_input:
            os.system("sh ./prepare_requirement/pytorch_cpuonly.sh")
        elif '2' in user_input:
            os.system("sh ./prepare_requirement/pytorch_cuda10.sh")
        elif '3' in user_input:
            os.system("sh ./prepare_requirement/pytorch_cuda11.sh")
        else:
            print("Wrong input get, exit.")
            exit(-1)
def basic_installation():
    os.system("sh ./prepare_requirement/basic_requirement.sh")