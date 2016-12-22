# Simple test of the Central Limit Theorem

A program to test the CLT through experimentation.

Steps: 

* Generates a set of random numbers.
* Takes a large number of samples from the population
* The expectation is that 68.27% of the sample means will be within +/- 1 times the Standard Error

Standard Error = Standard Deviation of Sampling Distribution

Standard Error = (Population Standard Deviation) / (sqrt(Sample Size))

After running a million trials, the accuracy was within 0.1 percent. 

Possible improvements: 

* Try with a population of integers instead of floating point numbers.
* Run this on a computer with more computing power. 
* Differences amounting to 0.1% don't likely matter in practice \.\.\.
* ... eHow many samples need to be taken to get a good estimate? 
