## It starts to cycle
The last couple of weeks were a long search for suitable parameters. I think I'm still not done with it, but I think I have
a set that seems to work. In the following I will show some preliminary results and discuss some problems and possible next steps.

### Parameters
In the following I list the different parameter sets I use for each environment. You can skip that part, if your not interested
in the details.

**Cyclic (Zero)**
```
RESOURCE day:initial=10
RESOURCE night:initial=0

u 4:4:end SetResource day 10
u 2:4:end SetResource day 0

u 0:2:end SetResource night 0
u 2:4:end SetResource night 10

u 2:4:end SetReactionMaxTaskCount NOT 0
u 2:4:end SetReactionMaxTaskCount AND 0
u 2:4:end SetReactionMaxTaskCount OR 0
u 2:4:end SetReactionMaxTaskCount NOR 0
u 2:4:end SetReactionMaxTaskCount EQU 0
u 4:4:end SetReactionMaxTaskCount NOT 5
u 4:4:end SetReactionMaxTaskCount AND 5
u 4:4:end SetReactionMaxTaskCount OR 5
u 4:4:end SetReactionMaxTaskCount NOR 5
u 4:4:end SetReactionMaxTaskCount EQU 5

u 0:2:end SetReactionMaxTaskCount NAND 0
u 0:2:end SetReactionMaxTaskCount ORN 0
u 0:2:end SetReactionMaxTaskCount ANDN 0
u 0:2:end SetReactionMaxTaskCount XOR 0
u 2:4:end SetReactionMaxTaskCount NAND 5
u 2:4:end SetReactionMaxTaskCount ORN 5
u 2:4:end SetReactionMaxTaskCount ANDN 5
u 2:4:end SetReactionMaxTaskCount XOR 5
```
**Cyclic (Not Zero)**
```
RESOURCE day:initial=10
RESOURCE night:initial=1

u 4:4:end SetResource day 10
u 2:4:end SetResource day 1

u 0:2:end SetResource night 1
u 2:4:end SetResource night 10

u 2:4:end SetReactionMaxTaskCount NOT 1
u 2:4:end SetReactionMaxTaskCount AND 1
u 2:4:end SetReactionMaxTaskCount OR 1
u 2:4:end SetReactionMaxTaskCount NOR 1
u 2:4:end SetReactionMaxTaskCount EQU 1
u 4:4:end SetReactionMaxTaskCount NOT 5
u 4:4:end SetReactionMaxTaskCount AND 5
u 4:4:end SetReactionMaxTaskCount OR 5
u 4:4:end SetReactionMaxTaskCount NOR 5
u 4:4:end SetReactionMaxTaskCount EQU 5

u 0:2:end SetReactionMaxTaskCount NAND 1
u 0:2:end SetReactionMaxTaskCount ORN 1
u 0:2:end SetReactionMaxTaskCount ANDN 1
u 0:2:end SetReactionMaxTaskCount XOR 1
u 2:4:end SetReactionMaxTaskCount NAND 5
u 2:4:end SetReactionMaxTaskCount ORN 5
u 2:4:end SetReactionMaxTaskCount ANDN 5
u 2:4:end SetReactionMaxTaskCount XOR 5
```
**Cyclic and Punishment**
```
RESOURCE day:initial=10
RESOURCE night:initial=1

u 4:4:end SetResource day 10
u 2:4:end SetResource day 1

u 0:2:end SetResource night 1
u 2:4:end SetResource night 10

u 2:4:end SetReactionMaxTaskCount NOT 1
u 2:4:end SetReactionMaxTaskCount AND 1
u 2:4:end SetReactionMaxTaskCount OR 1
u 2:4:end SetReactionMaxTaskCount NOR 1
u 2:4:end SetReactionMaxTaskCount EQU 1
u 4:4:end SetReactionMaxTaskCount NOT 5
u 4:4:end SetReactionMaxTaskCount AND 5
u 4:4:end SetReactionMaxTaskCount OR 5
u 4:4:end SetReactionMaxTaskCount NOR 5
u 4:4:end SetReactionMaxTaskCount EQU 5

u 0:2:end SetReactionMaxTaskCount NAND 1
u 0:2:end SetReactionMaxTaskCount ORN 1
u 0:2:end SetReactionMaxTaskCount ANDN 1
u 0:2:end SetReactionMaxTaskCount XOR 1
u 2:4:end SetReactionMaxTaskCount NAND 5
u 2:4:end SetReactionMaxTaskCount ORN 5
u 2:4:end SetReactionMaxTaskCount ANDN 5
u 2:4:end SetReactionMaxTaskCount XOR 5

u 2:4:end SetReactionValue NOT -0.1
u 2:4:end SetReactionValue AND -0.2
u 2:4:end SetReactionValue OR -0.2
u 2:4:end SetReactionValue NOR -0.2
u 2:4:end SetReactionValue EQU -0.2
u 4:4:end SetReactionValue NOT 1
u 4:4:end SetReactionValue AND 2
u 4:4:end SetReactionValue OR 3
u 4:4:end SetReactionValue NOR 4
u 4:4:end SetReactionValue EQU 5

u 0:2:end SetReactionValue NAND -0.1
u 0:2:end SetReactionValue ORN -0.2
u 0:2:end SetReactionValue ANDN -0.2
u 0:2:end SetReactionValue XOR -0.2
u 2:4:end SetReactionValue NAND 1
u 2:4:end SetReactionValue ORN 2
u 2:4:end SetReactionValue ANDN 3
u 2:4:end SetReactionValue XOR 4
```
**Punishment**
```
RESOURCE day:initial=10
RESOURCE night:initial=10

u 2:4:end SetReactionValue NOT -0.1
u 2:4:end SetReactionValue AND -0.2
u 2:4:end SetReactionValue OR -0.2
u 2:4:end SetReactionValue NOR -0.2
u 2:4:end SetReactionValue EQU -0.2
u 4:4:end SetReactionValue NOT 1
u 4:4:end SetReactionValue AND 2
u 4:4:end SetReactionValue OR 3
u 4:4:end SetReactionValue NOR 4
u 4:4:end SetReactionValue EQU 5

u 0:2:end SetReactionValue NAND -0.1
u 0:2:end SetReactionValue ORN -0.2
u 0:2:end SetReactionValue ANDN -0.2
u 0:2:end SetReactionValue XOR -0.2
u 2:4:end SetReactionValue NAND 1
u 2:4:end SetReactionValue ORN 2
u 2:4:end SetReactionValue ANDN 3
u 2:4:end SetReactionValue XOR 4
```
### Results
**Fitness**      
The figure below shows the average fitness for each environment. For each environment I ran 50 replicates. We see that the
fitness in pure cyclic environments is higher than in environments that also have punishment enabled. We also see that
the fitness in the environment will "zero" cycles is slightly lower. That is simply because in the other environment the organisms
have still a chance to perform tasks in the "wrong" cycle and get some reward, so they don't have so much pressure to switch
between metabolisms. When punishment is enabled the organisms fitness drops to almost half of the cyclic organisms fitness.
However, punishment alone is less detrimental than the combination of cyclic environment and punishment. The reasons for the
fitness differences can be better explained when looking at the different reactions that are performed and how often they are
performed per update.

![Figure 1](../data_analysis/mean_fitness_per_env(n=50).pdf)

**Reactions**       
The difference between the two cyclic environments can be explained by first the possibility of getting reward in the "wrong"
cycle and second by the fact that they learn more difficult tasks much earlier. However, the pressure to schedule their metabolism
is not strong enough, so they perform each task more or less unconditionally and irrespective of the current resource cycle. I think
that two will align, if you run the experiment long enough, which will be one thing I want to do next.
Regarding the punishment, it seems that both environments follow a similar trend as the "not zero" cyclic environment if you look
at the reaction an their respective count per update. That could mean that the pressure by the punishment is lower than in the
"zero" cyclic environment. So the organisms still favor the unconditional performance of reaction over the scheduling of the
metabolism. This will probably chance over time and this is why I need to run the experiment longer. Another idea would be to
increase the punishment and therefore the pressure. The way that punishment works, is that the organisms gets lower reward instead
of negative reward, which would kill it. So performing a task with punishment still results in more reward than not performing that
task. Interestingly, the "zero" cyclic environment shows higher fitness. This could mean that scheduling the metabolism results in
a fitness advantage, because you perform higher reward task at the right time instead of perform a task all the time. I need to
test this in competition experiments between the dominant organisms of each environment. All in all the first preliminary results
show some interesting trends that needs to be investigated further.

![Figure 2](../data_analysis/reactions_per_env(n=50).pdf)
![Figure 3](../data_analysis/reactions_per_env(n=50)_last50u.pdf)

### Still a long way to go
I think I'm still not at the end of the parameter search, since so many different variations are possible and number of combination
grows exponentially. However, I have some ideas for the next experiments and I think I'm closing in on the environment of choice.

I also want try the following changes:
* More updates (200k or more)
* Change punishment (0.5-1 or even higher)
* Change cycle length
* Set MaxTaskCount to 1 and Resource to infinite
* Competition between "zero" cyclic and cyclic punishment environment

-- Cheers, Nic
