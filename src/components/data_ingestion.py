import os
import sys
import pandas as pd
import numpy as np
from src.exception import  CustomException
from src.logger import logging

from sklearn.model_selection import train_test_split
from dataclasses import dataclass  #------------------------------------------------Used to create classs variables--------------------------------


class DataIngestionConfig:
    