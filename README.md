# Recursion Syntax Test
by mas 10.2018
hi

## Overview
* Test performance of different loop syntax

* Code recursive operation in three different styles 

* Time execution of recursive operation

* Repeat many times to get some stats

* Plot mean and standard deviation

## Examples

* An example plot of elapsed execution time (in seconds) for three different loop syntax styles is provided as "timing_comparison.png" and shown below. 

* The plot shows 50 unique trials (shown as individual data points on the plot) using each style to execute a recursive list operation 1000 times. 

* For clarity, the mean and standard deviation are shown as the color-coded box plots. 

* The "Pythonic" style (red) which utilizes list comprehension is nearly 2x faster than the "Clunky" style (blue) which utilizes temporary lists. 

![](timing_comparison.png)
