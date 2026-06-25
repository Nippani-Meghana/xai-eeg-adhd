#nasarbadi_helper.py

import pandas as pd
import EegDataset

def get_dataset_info():
    # Load the raw data
    data = pd.read_csv("./datasets/raw_data/adhdata.csv")

    # Create an instance of EegDataset
    dataset_info = EegDataset.EegDataset(
        name="nasarbadi_adhd",
        sampling_freq_hz=128.0,
        participants=len(data["ID"].unique()),
        num_channels=19,
        adhd_num=data[data["Class"] == "ADHD"]["ID"].nunique(),
        control_num=data[data["Class"] == "Control"]["ID"].nunique(),
        channel_names=[f"Channel_{i}" for i in range(19)],
        raw_data_path="./datasets/raw_data/adhdata.csv",
        interim_data_path="./datasets/interim_data/nasarbadi/",
        metadata_path = "./datasets/metadata"
    )

    return dataset_info

def get_subject_info(subject_id):
    # Load the raw data
    subject_data = pd.read_csv(f"./datasets/interim_data/nasarbadi/{subject_id}.csv")

    if subject_data.empty:
        raise ValueError(f"No data found for subject ID: {subject_id}")

    class_label = pd.read_csv("./datasets/metadata/nasarbadi_subject_index.csv").loc[pd.read_csv("./datasets/metadata/nasarbadi_subject_index.csv")["ID"] == subject_id, "Class"].values[0]
    return [subject_data, class_label]