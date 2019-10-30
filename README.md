<<<<<<< HEAD
# Vowel Placer
A collection of (mostly) Python scripts to place vowels for any given spoken dataset on the f1-f2 plane. Completed as part of the requirements for the honours spec. linguistics, at Western University. 

## Scripts
### Learn.py
The main learning algorithm. Takes scraped data (from vowelScraper) and trains neural network.

### NotVowel.py
Takes known vowel samples and creates a negative dataset of all measured samples without known samples, to give neural net a negative corpus on which to train.

### ReadSynapses.py
Read synapses from text file so training isn't necessary each time debugging is needed.

### VowelSpace.py
The main script for the algorithm - takes True/False as the 1st arg: True means learn, False means read synapses from text.

## Vowel Scraper
Uses Praat to scrape the potential vowel samples from large spoken copora. Criteria are continuity of formants (do they remain consistent over given frame?), intensity (is the sample in question at a relative max in the intensity curve, indicating a vowel at the nucleus of a syllable), and validity (are there 5 formants within typical ranges?). 
=======
# Geolinguistique_scripts
Scripts used for my 2019 Géolinguistique publication on automatic vowel space generation in successive heritage speaker generations. 
>>>>>>> 4f97d55cbe550d0ff1222abd8c1f8d2efabd219f
