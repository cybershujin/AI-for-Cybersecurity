import numpy as np
import os
import datetime
import re
import tensorflow as tf
from tensorflow.keras import models
from tensorflow.keras import layers
import matplotlib.pyplot as plt

def plot_history(history):
    accuracy = history['accuracy']
    loss = history['loss']
    val_accuracy = history['val_accuracy']
    val_loss = history['val_loss']
    (figure, axes) = plt.subplots(1,2,figsize=(10,4), dpi=300)
    axes[0].plot(accuracy, label="Training")
    axes[0].plot(val_accuracy, label="Validation")
    axes[0].legend()
    axes[0].set_xlabel("Epoch")
    axes[0].grid()
    axes[0].set_title("Accuracy")
    axes[1].plot(loss, label="Training")
    axes[1].plot(val_loss, label="Validation")
    axes[1].legend()
    axes[1].set_xlabel("Epoch")
    axes[1].grid()
    axes[1].set_title("Loss")
    plt.show()
