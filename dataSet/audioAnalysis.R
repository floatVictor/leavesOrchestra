library(tuneR)
library(seewave)
library(soundecology)
library(jsonlite)

folder_path <- "E:/Etudes/IMAC3/PROJET/Nia_sample"
audio_files <- list.files(folder_path, pattern = ".wav", full.names = TRUE)

# file_path_test <- "E:/Etudes/IMAC3/PROJET/Nia_sample/4_20180907_181000_Rec [-2.9274 -55.0027].wav"
# audio_test <- readWave(file_path_test)

# Initialize empty list to store results
results_list <- list()

#-------------------------------------------------------------------#

#test analyse

# bioindex <- bioacoustic_index(audio_test)$left_area
# print(bioindex)

# soundfile.aci <- acoustic_complexity(audio_test)
# print(soundfile.aci$AciTotAll_left)
# print(soundfile.aci$AciTotAll_left_bymin)

#-------------------------------------------------------------------#

# Loop through audio files, extract features, and add to results list
for (file in audio_files) {

	audio <- readWave(file)
	print(basename(file))
	features <- list(
		duration = duration(audio),
		mean_peaks = fpeaks(meanspec(audio)), #peaks
		sd_audio <- sd(as.vector(audio@left)), #standard deviation value
		spectral_entropy = H(audio, audio@samp.rate), #entropy
		ac_complexity_all <- acoustic_complexity(audio)$AciTotAll_left,
		bioindex <- bioacoustic_index(audio)$left_area
	)
  	results_list[[basename(file)]] <- features
}

# Convert results list to JSON and write to file
results_json <- toJSON(results_list)
write(results_json, file = "results.json")