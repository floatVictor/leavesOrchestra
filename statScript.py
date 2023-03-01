import json
import statistics
import numpy as np

# Read the JSON file
with open('sampleData.json') as f:
    data = json.load(f)

duration_values = [data[filename]['duration'][0] for filename in data]

print(f"total duration: {sum(duration_values)}")

# Get all the values
sd_audio_values = [data[filename]['sd_audio'][0] for filename in data]
ac_complexity_all_values = [data[filename]['ac_complexity_all'][0] for filename in data]
bioindex_values = [data[filename]['bioindex'][0] for filename in data]
spectral_entropy_values = [data[filename]['spectral_entropy'][0] for filename in data]

# calculate minimum, maximum, average and std
min_bioindex = min(bioindex_values)
max_bioindex = max(bioindex_values)
avg_bioindex = sum(bioindex_values) / len(bioindex_values)
std_bioindex = np.std(bioindex_values)

min_sd_audio = min(sd_audio_values)
max_sd_audio = max(sd_audio_values)
avg_sd_audio = sum(sd_audio_values) / len(sd_audio_values)
std_sd_audio = np.std(sd_audio_values)

min_ac_complexity_all = min(ac_complexity_all_values)
max_ac_complexity_all = max(ac_complexity_all_values)
avg_ac_complexity_all = sum(ac_complexity_all_values) / len(ac_complexity_all_values)
std_ac_complexity_all = np.std(ac_complexity_all_values)

min_spectral_entropy = min(spectral_entropy_values)
max_spectral_entropy = max(spectral_entropy_values)
avg_spectral_entropy = sum(spectral_entropy_values) / len(spectral_entropy_values)
std_spectral_entropy = np.std(spectral_entropy_values)

print(f"min_sd_audio: {min_sd_audio}")
print(f"max_sd_audio: {max_sd_audio}")
print(f"avg_sd_audio: {avg_sd_audio}")
print(f"var_sd_audio: {std_sd_audio}")

print(f"min_bioindex: {min_bioindex}")
print(f"max_bioindex: {max_bioindex}")
print(f"avg_bioindex: {avg_bioindex}")
print(f"std_bioindex: {std_bioindex}")

print(f"min_ac_complexity_all: {min_ac_complexity_all}")
print(f"max_ac_complexity_all: {max_ac_complexity_all}")
print(f"avg_ac_complexity_all: {avg_ac_complexity_all}")
print(f"std_ac_complexity_all: {std_ac_complexity_all}")

print(f"min_spectral_entropy: {min_spectral_entropy}")
print(f"max_spectral_entropy: {max_spectral_entropy}")
print(f"avg_spectral_entropy: {avg_spectral_entropy}")
print(f"std_spectral_entropy: {std_spectral_entropy}")

#calculates first and last dates
sorted_dates = sorted([data[filename]['date'] for filename in data])

first_date = sorted_dates[0]
last_date = sorted_dates[len(sorted_dates) - 1]

print("First date:", first_date)
print("Last date:", last_date)