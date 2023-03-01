# README

# dataSample.json documentaton :

write short description here ...

name of the audio file: {

		"sd_audio": 
            Standard deviation is the measure of the dispersion of the values,
            it's the square root of the ‘variance’.

		"ac_complexity_all":
            The ACI is based on the “observation that many biotic sounds, 
            such as bird songs, are characterized by an intrinsic variability 
            of intensities, while some types of human generated noise (such as car passing or airplane transit) 
            present very constant intensity values” (Pieretti, et al. 2011).

		"bioindex":
            The Bioacoustic Index, from Boelman et al. 2007, is calculated as the 
            “area under each curve included all frequency bands associated with the dB value 
            that was greater than the minimum dB value for each curve. The area values are 
            hus a function of both the sound level and the number of frequency bands used by the avifauna”.

		"duration":
            Duration in seconds of the audio file

		"mean_peaks":
            List of the peaks ([frequency (kHz), amplitude (dB)]) in the frequency spectrum of the audio file

		"spectral_entropy":
            Spectral entropy is a measure of the amount of information contained in the 
            power spectral density (PSD) of a signal. In signal processing, spectral entropy can 
            be used as a tool to identify specific frequency bands in a signal that have high or low complexity.

		"location": 
            Location where the audio was recorded.

		"date":
            Date where the audio was recorded.

		"time":
            Time where the audio was recorded.

	},

# dataSetInfo.json documentaton :

write short description here ...

everything should be self-explanatory (avg: average; std: standard deviation value)

#references :
https://cran.r-project.org/web/packages/soundecology/vignettes/intro.html
https://rug.mnhn.fr/seewave/
https://www.rdocumentation.org/packages/stats/versions/3.6.2/topics/sd
https://search.r-project.org/CRAN/refmans/ForeCA/html/spectral_entropy.html