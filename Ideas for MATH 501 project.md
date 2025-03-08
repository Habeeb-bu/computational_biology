Ideas for MATH 501 project


The goal of this project is to perform simple experiments using a genetic algorithm (GA). The experiment should compare related evolutionary processes, i.e. how fitness or other factors evolve, for different evolutionary models. Possible experiments include testing the effects of changing basic parameters of the GA:

Population size
Mutation rate
Selection pressure
Selection method
More involved experiments could include:

Testing the effect of incorporating more accurate biological concepts: diploid genomes, dominance, more accurate versions of crossover, etc.
Complex fitness functions that are biologically more relevant.
Incorporating bottlenecks.
Incorporating merging or divergent populations.
Etc., etc., etc. 
Note that there are many ways to measure the effect of a parameter. Does it cause fitness to improve faster or slower? Does it cause the fitness to reach a maximum sooner or later? How does it affect population diversity? Etc. Think about what metric(s) you want to use to measure your results. 

If there is a way to relate your experiment to your graduate research, I strongly encourage you to do so, even if it means going a bit outside the box with regards to the project description.

You need to pick the details of the GA: population size, mutation rate, etc. If you are testing the impact of an adjustable parameter, then you should test a range of values. For example, if you are looking at mutation rate, you should test several different mutation rates, not just two.

Multiple Runs - The results should be based on the average of multiple independent runs of your evolutionary algorithm. 

Example - A simple example would be to pick 2 different mutation rates and 2 population sizes (4 experimental conditions) and run each condition 20 times. Then look at (i.e.) plot how fitness changes over time for each of the four conditions. 

Teams - You may work in teams, if you want. Ideally in teams of two, but if you have a good justification for a team of three (and are proposing a bit more) that should be fine, just ask. 

Project Write-up - Write a short research paper (typically 3-5 pages) describing the results of your project that includes the following sections:

Abstract - a short summary of what you did and what the results were.
Experiment Description - A description of your experiment, what you are testing and how. 
Algorithm descriptions - clear, complete descriptions of your GA. Be careful to include all of the details someone would need to replicate your work. Examples of necessary details include (there are others):
How fitness is measured
Exactly how initial random individuals are generated
Mutation rates
Selection method
Etc.
Basically, every time you make a decision about how the algorithm works (what type of crossover it uses, how mutation is performed, etc.) you should make a note of it and include it in the algorithm description.

Results - include graphs and/or tables to make it easy to understand the results. Make sure that the graphs and table are clearly labeled.
Conclusions - based on your results draw some specific conclusions about how the algorithm performed.
Code - attached as an appendix
Do not upload a zipped file. You may upload multiple files (the project and the code).


IDEA:
- fitness is based on where you are on a 2D scale model/3D scale. 
 - maybe more food in the center, maybe the center are changing

 - changes based on a time constrait/limit before dying. -> or only those can have children
 take or use a diffusion equation.
 - maybe give a change to mutated for a higher movement value(?) 

RESULTS:
 - what type of mutation lead to the best fitness. 
 - perhaps a bar graph/a fitness landscape based on 