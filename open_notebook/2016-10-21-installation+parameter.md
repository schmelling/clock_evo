## Installation

Last week I ran into installation problems of Avida on a Linux Ubuntu machine. I filed an issus at the Avida repo. They reported that say didn't see that error I got when installing a fresh Avida version, however, my problems persisted. They also had a solution if the same problem still occurs. Luckly this worked perfectly and I now have Avida running on Mac and Linux Ubuntu. 1-0 for open communication :-). The solution can be found in the [closed issue #7](https://github.com/schmelling/clock_evo/issues/7).

## Set Up and Parameter Search

Having Avida installed, I started working on experimental set ups and parameters. In the following I will write down changes to the individual files.

### clock.org

This file stores the starting organisms genome. I just had to change the first line, where you specify, which genetic code is underlying.

```
#inst_set clock
```

### instset-clock.cfg

This file stores the genetic code. So all possible instructions that an organisms can have in its genome. I had to add three new instructions, which was `time`, `sleep`, and `sense`. `sense` and `time` are necessary for the experiment as it needs to be possible the sense resources and the time between the occurence of these resources. I also allow `sleep` in the instruction set, because it got be a valid strategy to just do nothing for a while instead of using the second resource. Furthermore I had to change the default organism name in the first line.

```
INSTSET clock:hw_type=0
...
INST sense
INST sleep
INST time
```

### environment_clock.cfg

The environment file stores information about resources and their availability as well as reaction i.e. logic tasks and their reward and dependence on a resource. I added a first resource and removed some more difficult tasks as in the adaptive sleep experiment. Furthermore, I added some dependences for the tasks such that they rely on the presence of the resource, their reward, as well as the fraction of that resource that can maximally be consumed.

```
```

### events_clock.cfg

The events file stores the instructions for data collection and changes to the environment during a Avida run. I added some new data collection to default set. This can still be extended. Right now I'm just playing with different options. The hardest part here was to get the resource oscillating i.e. alternating between presence and absence. For now I have only one resource oscillating to first reproduce the results of the adaptive sleep experiment. If I have sensing/sleeping organisms I will start to add the second resource. I get the resource to oscillate, however, I see a decrease in the amount of the resource over time, which should not be happening. This is problem I need to solve next week.

```
```

### avida.cfg

The avida config file stores more or less all of the information about the experiment. I didn't change much here, however I neede to change the file paths for events, environment, etc. and as in the adaptive sleep experiment I allow for only one CPU cycle per update.

```
```
## First Avida test runs

To get started I ran one Avida experiment with default setting to get an idea about the different data and what a "normal" value for example merit is. I also ran some shorter runs to test my parameter settings for the oscillating resource. After that was good I ran one longer experiment with "sleeping" settings. I also took a quick look at the data and found some unexpected behavior of the resource, which needs to be fixed.

## Open Science Side Projects

During the Avida experiments, which usually run for ~30 min on my computer, I had time to start working on my Python reference repo. There I just organized to first directories for different topics and added some first links to jupyter notebooks and other online resources. 

-- Cheers, Nic
