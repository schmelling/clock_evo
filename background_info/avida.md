## Digital Organisms

Evolution is a process that is very slow, which makes it hard to study it in nature. Usually evolution acts on timescale of millions to billions of years. However, it is still possible to study evolution. One prominent experiment that is often mentioned in regard to experimental evolution is the [_E.coli_ long-term evolution experiment](https://en.wikipedia.org/wiki/E._coli_long-term_evolution_experiment) by Richard Lenksi and his lab, where they are evolving bacteria in a laboratory environment since 25 years.

According to Daniel Dennett evolution has the meet three criteria to occur:

- __replication__
- variation (__mutation__)
- differential fitness (__competition__)

Researches tried to overcome the challenges posed by the speed of evolution and one solution were digital organisms. Digital organisms are tiny computer programs that life in an artificial world inside of your computer. However, these organisms replicate, mutate, and compete for resources, and thus meeting all criteria need for evolution to occur. Computers have the huge potential to unravel evolutionary mechanisms by speeding up the evolutionary process. They can simulate thousand of generations in a fraction of an hour and measure anything with arbitrary precision. Avida, the most advanced software platform for studying digital organisms, enables detailed control over environmental settings, a variety of organism-environment interaction, as well as manipulation of organisms.

## Avida

The Avida software is composed of three main modules:

1. a core, which maintains a __population of digital organisms__ (each with its own genome, virtual hardware, etc.), an __environment__ that maintains the reactions and resources with which the organisms interact, a __scheduler__ to allocate __CPU cycles__ to the organisms, and various __data collection objects__.
2. the __graphical user interface__ (GUI), which the researcher can use to interact with the rest of the Avida software.
3. a __collection of analysis and statistics tools__, including a test environment to study organisms outside the population, data manipulation tools to rebuild phylogenies and examine lines of descent, mutation and local fitness analysis tools, and many others, all bound together in a simple scripting language.

The Avida core comprises multiple files, including:
- the __genesis file__, which contains a list of variables that control all of the basic settings of a run, including the population size, the mutation rates, and the names of all of the other configuration files to use.
- the __instruction set__, which describes the specific genetic language used in the experiment.
- the __ancestral organism__ that the population should be seeded with.
- the __environment file__ that describes which resources are available to the organisms, and defines reactions by the tasks that trigger them, their value, the resource that they use, and any by-products that they produce.
- the __events file__ is used to describe specific actions that should occur at designated time points during the experiment, including most data collection, as well as direct disruptions to the population.


### Organisms

In Avida, each digital organism is a self-contained, little computer program that has the ability to construct new programs. In an Avida experiment, self-replicating digital organisms compete against each other in a fixed-size steady-state population. The core of the machine is the central processing unit (CPU), which processes each instruction in the genome (circular list of assembly-like instructions) and modifies the states of its components appropriately. Instructions are executed one after the other, unless an instruction (such as a jump) explicitly interrupts sequential execution. Technically, the memory space is organized in a circular fashion, such that after the CPU executes the last instruction in memory, it will loop back and continue execution with the first instruction again. However, at the same time the memory has a well-defined starting point, important for the creation of offspring organisms. To reproduce, an organism must perform three distinct functions:

1. __allocate__ space at the end of its genome for its offspring’s genome,
2. __duplicate__ its own genome instruction by instruction into that space,
3. __divide__ the resulting genome into two parts.

Variation among organisms in the population occurs when instructions are copied. Each copied instruction is subject to three types of mutation (modifying the instruction, deleting the instruction, or inserting an additional instruction) that occur at user defined rates. The phenotype of an organism comprises all observable characteristics of that organism. As an organism in Avida goes through its life cycle, it will self replicate and, at the same time, interact with the environment. The primary mode of environmental interaction is by inputting numbers from the environment, performing computations on those numbers, and outputting the results. The organisms receive a benefit for performing specific computations associated with resources. In addition to tracking computations, the phenotype also monitors several other aspects of the organism’s behavior, such as its gestation length (the number of instructions it executes to produce an offspring, often also called gestation time), its age, whether it has been affected by any mutations, how it interacts with other organisms, and its overall fitness.

### World

In general, the Avida world has a fixed number N of positions, or cells. Each cell can be occupied by exactly one organism, so that the maximum population size at any given time is N. In the simplest of Avida experiments, all virtual CPUs run at the same speed. This method of time sharing is simulated by executing one instruction on each of the N virtual CPUs in order, then starting over to execute a second instruction on each one, and so on.      
An __update__ in Avida is defined as a point where the average organism has executed k instructions (where k = 30 by default). In this simple case, for one update we carry out k rounds of execution. Each organism has associated with it a value called merit. The __merit__ indicates how fast the CPU should run. Merit is only meaningful when compared with the merits of other organisms.     
Thus, if organism A has twice the merit of organism B, then A should execute twice as many instructions in any given time frame as B.

Avida handles this with two different schedulers:

1. a perfectly integrated scheduler, which comes as close as possible to portioning out CPU cycles in proportion to merit.
2. a probabilistic scheduler. At each point in time, the next organism to be selected is chosen at random, but with the probability of an individual being chosen proportional to its merit. Thus on average this scheduler is perfect, but there are no guarantees.

The N cells of the Avida world can be assembled into different topologies that affect how offspring organisms are placed and how organisms interact. Currently, there are two world topologies:

- a __2D grid with Moore neighborhood__ (each cell has eight neighbors)
- a __fully connected__ (sometimes called well-stirred or mass action) topology.

In the fully connected topology each cell is a neighbor to every other cell. When a new organism is about to be born, it will replace either the parent cell or another cell from the neighborhood. The specifics of this placement are set up by the experimenter. The two most commonly used methods:

- __replace random__, which chooses randomly from the neighborhood
- __replace oldest__, which picks the oldest organism from the neighborhood to replace (with a preference for empty cells if any exist).

All organisms in Avida are provided with the ability to absorb a default resource that gives them their base merit. An Avida environment can, however, contain other resources that the organisms can absorb to modify their merit. The organisms absorb a resource by carrying out the corresponding computation, or task.

A __reaction__ is defined by:

- a __computation__ that the organism must perform to trigger it,
- a __resource__ that is consumed by it,
- a __merit__ effect on the organism (which can be proportional to the amount of resource absorbed or available).

A __resource__ is described by:
- an __initial quantity__ (which can be infinite if a resource should not be depletable),
- an __inflow rate__ (the amount of that resource that should come into the population per update), and
- an __outflow rate__ (the fraction of the resource that should be removed each update).

The default Avida environment rewards __nine boolean logic operations__.

In the simplest Avida experiments, the only interaction between organisms is that an organism is killed when another gives birth, in order to make room for the offspring. In slightly more complex experiments, the organisms are rewarded with a higher merit and hence a larger share of the CPU cycles for performing tasks. Since there are only a fixed number of CPU cycles given out each update, the competition for them becomes a second level of indirect interaction among the organisms. In the end, however, all these interactions boil down to the indirect competition for space:

More resources imply a higher merit, which in turn grants the organisms a larger share of the CPU cycles, allowing them to replicate more rapidly and claim more space for their genotype.

### Further Reading  

Carl Zimmer. Testing Darwin. February 05, 2005. [Discover Magazine](http://discovermagazine.com/2005/feb/cover/#.URRxZOjZrbI)

Charles Ofria and Claus O. Wilke. Avida: A Software Platform for Research in Computational Evolutionary Biology. 2004. [Artificial Life. 10(2), 191–229](http://www.ofria.com/pubs/2004OfriaEtAl.pdf)

Benjamin E. Beckmann, Philip K. McKinley, and Charles Ofria. Evolution of adaptive sleep response in digital organisms. 2007. [Proceedings of the 9th European Conference on Artificial Life](http://www.ofria.com/pubs/2007bBeckmannEtAl.pdf)

### Resources  
- [Avida GitHub](https://github.com/devosoft/avida)
- [Avida Wiki](https://github.com/devosoft/avida/wiki)
