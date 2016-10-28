## Installation

Last week, I ran into installation problems of Avida on a Linux Ubuntu machine. I filed an issus at the Avida repo. They reported that they didn't see that error I got when installing a fresh Avida version. However, my problems persisted. They also had a solution if the same problem still occurs. Luckly, this worked perfectly, and I now have Avida running on Mac and Linux Ubuntu. 1-0 for open communication :-). The solution can be found in the [closed issue #7](https://github.com/schmelling/clock_evo/issues/7).

## Set Up and Parameter Search

Having Avida installed, I started working on experimental set ups and parameters. In the following, I will write down changes to the individual files.

### clock.org

This file stores the starting organisms genome. I just had to change the first line, where you specify which genetic code is underlying.

```
#inst_set clock
```

### instset-clock.cfg

This file stores the genetic code. So all possible instructions that an organisms can have in its genome. I had to add three new instructions, which were `time`, `sleep`, and `sense`. `sense` and `time` are necessary for the experiment, as it needs to be possible [!!something missing here] the sense resources and the time between the occurence of these resources. I also allow `sleep` in the instruction set, because it got to be a valid strategy to just do nothing for a while instead of using the second resource. Furthermore, I had to change the default organism name in the first line.

```
INSTSET clock:hw_type=0
...
INST sense
INST sleep
INST time
```

### environment_clock.cfg

The environment file stores information about resources and their availability as well as reaction, i.e. logic tasks and their reward and dependence on a resource. I added a first resource and removed some more difficult tasks as in the adaptive sleep experiment. Furthermore, I added some dependences for the tasks such that they rely on the presence of the resource, their reward, as well as the fraction of that resource that can maximally be consumed.

```
RESOURCE day:inflow=1:outflow=0.01

REACTION  NOT  not   process:resource=day:value=1500.0:frac=0.0025:max=20
REACTION  NAND nand  process:resource=day:value=1500.0:frac=0.0025:max=20
REACTION  AND  and   process:resource=day:value=2000.0:frac=0.0025:max=13
REACTION  ORN  orn   process:resource=day:value=2000.0:frac=0.0025:max=13
```

### events_clock.cfg

The events file stores the instructions for data collection and changes to the environment during a Avida run. I added some new data collection to default set. This can still be extended. Right now, I'm just playing with different options. The hardest part here was to get the resource oscillating i.e. alternating between presence and absence. For now I have only one resource oscillating to first reproduce the results of the adaptive sleep experiment. If I have sensing/sleeping organisms I will start to add the second resource. I get the resource to oscillate, however, I see a decrease in the amount of the resource over time, which should not be happening. This is a problem I need to solve next week.

```
u 0:10:end PrintTasksExeData
...
u 0:10:end PrintSenseData
u 0:10:end PrintSenseExeData
u 0:10:end PrintSleepData

u 1280:2560:end SetResource day 10000
u 1280:2560:end SetResourceInflow day 100

u 2560:2560:end SetResource day 0
u 2560:2560:end SetResourceInflow day 0    
```

### avida.cfg

The avida config file stores more or less all of the information about the experiment. I didn't change much here, however, I neede to change the file paths for events, environment, etc. and as in the adaptive sleep experiment, I allow for only one CPU cycle per update.

```
### CONFIG_FILE_GROUP ###
# Other configuration Files
DATA_DIR data                           # Directory in which config files are found
EVENT_FILE events_clock.cfg             # File containing list of events during run
ANALYZE_FILE analyze.cfg                # File used for analysis mode
ENVIRONMENT_FILE environment_clock.cfg  # File that describes the environment

#include INST_SET=instset-clock.cfg
...
# Time Slicing
AVE_TIME_SLICE 1            # Average number of CPU-cycles per org per update 
```
## First Avida test runs

To get started, I ran one Avida experiment with default setting to get an idea about the different data and what a "normal" value for example merit is. I also ran some shorter runs to test my parameter settings for the oscillating resource. After that was good, I ran one longer experiment with "sleeping" settings. I also took a quick look at the data and found some unexpected behavior of the resource, which needs to be fixed.

## Some Thoughts

Even though it doesn't seem like much, it was a week of work to get the information needed. This got me thinking that there is some work that needs to be done in the documentation of Avida, which is by the way great and comprehesive, but lacks some entry level introduction and some more explanations here and there. For now I will write down ideas, thoughts, and more here. But I will definitely help to improve their documentation later on in the project.

## Open Science Side Projects

During the Avida experiments, which usually run for ~30 min on my computer, I had time to start working on my Python reference repo. There, I just organized to first directories for different topics and added some first links to jupyter notebooks and other online resources.

-- Cheers, Nic
