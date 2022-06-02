from typing import List

import numpy as np
import pandas as pd

# get rid of averaging
# parameters:
num_samples = control1[(control1.subject == 1)].shape[0]
sample_rate = num_samples / ((control1.time_ms[num_samples - 1] - control1.time_ms[0]) / 1000)
t = np.arange(0, 1, 1 / sample_rate)
n = np.size(t)
nbins = 30
upper_freq_limit = 60
interval = upper_freq_limit / nbins


from enum import Enum

class EEGAggregationMode(Enum):
    AVG = 1
    CONCAT = 2

class EEGPatient:
    def __init__(self, id, sensor_responses):
        self.id: int = id
        self.sensor_responses: List[List[float]] = sensor_responses

    def get_sensor_resp(self, sensor_id):
        return self.sensor_responses[sensor_id]

    # Gets the responses of all sensors and puts them in a vector.
    # Used for classification of the freq responses
    def get_all_resps(self, mode:EEGAggregationMode):
        if mode == EEGAggregationMode.AVG:
            # Average each sensor vector (averaging along axis 0)
            pass
        if mode == EEGAggregationMode.CONCAT:
            # Concat along axis 0
            pass


class EEGDataset:
    def __init__(self, patients):
        self.patients: List[EEGPatient] = patients


def response(group_index, group_data, group_response):
    # loop through each patient
    patients = []
    for pt_idx in group_index:
        pt_data = []
        # loop through sensors for each patient
        for sens_idx in range(2, 11):
            # perform fourier transform
            f = np.fft.fft(group_data[(group_data.subject == pt_idx)].iloc[:, sens_idx])
            # calculate frequency and response
            fr = sample_rate / 2 * np.linspace(0, 1, int(n / 2))
            y_m = 2 / n * abs(f[0:np.size(fr)])
            subject_signals_df = pd.DataFrame(zip(fr, y_m), columns=["frequency", "response"])
            subject_signals_df = subject_signals_df[
                (subject_signals_df["frequency"] < 60) & (subject_signals_df["frequency"] > 0)]
            sum_response = []  # vector of response sums for all bins
            for b in range(nbins):
                lower_bound = b * interval
                upper_bound = lower_bound + interval
                freq_in_range = subject_signals_df[
                    (subject_signals_df["frequency"] <= upper_bound) & (subject_signals_df["frequency"] >= lower_bound)]
                sum_response.append(sum(freq_in_range.response))
            pt_data.append(sum_response)
        patients.append(EEGPatient(id=pt_idx, sensor_responses=pt_data))

    return EEGDataset(patients)

# condition1
condition1response = [0] * 81;
condition1response = response(subjects, condition1, condition1response)

# condition2
condition2response = [0] * 81;
condition2response = response(subjects, condition2, condition2response)

# condition3
condition3response = [0] * 81;
condition3response = response(subjects, condition3, condition3response)
