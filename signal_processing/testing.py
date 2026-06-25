#signal_processing/testing.py
import mne

import pandas as pd
import matplotlib.pyplot as plt
import nasarbadi_helper

all_subjects = pd.read_csv("./datasets/metadata/nasarbadi_subject_index.csv")["ID"].tolist()

#plot a subject's 1 channel data

subject_id = all_subjects[0]
subject_data, class_label = nasarbadi_helper.get_subject_info(subject_id)



