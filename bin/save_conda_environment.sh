#!/bin/bash

source activate openvault_rpi

conda env export > /home/pi/workspace/openvault_rpi/environment.yml
