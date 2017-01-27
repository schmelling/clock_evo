## Parameter selection in Avida
In the last two weeks I tried a lot of different parameters for cyclic resources, reward and punishment cycles,
maximal number of tasks per update and resource to restrict the organisms options and to force them to learn
to adapt to cyclic environments. In the following I'll explain in more detail every single parameter I used and
discuss problems and solutions for working with them

### Avida.cfg
#### CPU Cycles per Update
The default value for this is 30 CPU cycles per update, however, in the publication I tried to reproduce they
used just 1 CPU cycle per update. I learned in yesterday's lab meeting that it makes no difference wether I
use 1 or 30, because they are just 30 times faster regarding the number of updates they need to learn something.
They only difference is that each update takes longer to calculate, because the organisms can simply do more
during one update. I decided to go back to the default settings because then I can compare my results to other
studies. Regarding the publication I tried to reproduce, I stopped that, because it is different from any other
studies in a lot regards and a lot of these settings are not working so reliable.

Changing to 30 CPU cycles per update, however, means that I have to reevaluate the cycle length of resources.

### Environment.cfg
#### Reaction
```
REACTION  NOT  not   process:type=pow:value=1.0:resource=day:product=day  requisite:max_count=5
```
#### Value
Right now I set the resource values to:

not    value=1.0    
nand   value=1.0    
and    value=2.0    
orn    value=2.0    
or     value=4.0    
andn   value=4.0    
nor    value=8.0    
xor    value=8.0    
equ    value=16.0    

but I'm thinking about going back to the default values.
#### Product
I use product and set it to the same resource as the one that is needed for the reaction.
This allows to have a constant resource level.
#### Max_Count
I use max_count to restrict the number of rewarded reaction per update, because I have basically unlimited resources due to
the product parameter described above.

### Events.cfg
####SetResource
I use this action to set resource amounts and their cycling length.
```
u 4:4:end SetResource day 10
u 2:4:end SetResource day 0
```
This code snippet will cycle resource abundance between 0 and 10 every two updates.
#### SetReactionMaxCount
I use this action to restrict the organisms ability to get reward for performed tasks. I have to do it, because they are not
consuming the resource, since they produce the resource as a product of its consumption (see above). I set this action also
on a cycling rhythm that fits the one from the resource.
```
u 2:4:end SetReactionMaxTaskCount NOT 0
u 4:4:end SetReactionMaxTaskCount NOT 5
```
*ATTENTION: You have to write the task name in uppercase letters, because that is the right resource name. I used lowercase
letters in the beginning and was wondering why it is not working properly.*
#### SetReactionValue
I use two different ways to punish the organisms when they perform a task at the wrong time.

I set the reaction value to either -1 for the easier tasks *not* and *nand* and -1 for all other tasks. This is way to punish
the organisms just a little bit, bt it seems that -1 and -2 are still to high.
#### SetReactionValueMult
The other way to punish, is to multiply the existing value. I use -1 to reverse the the value. This has the effect that task
with higher reward get punish a lot. Preliminary results suggest that I kill all organisms when I use this action.

### Instset.cfg
#### Time
I activated the time instruction so that organisms have a chance to measure time.
#### Sleep
I did not activate sleep, even though, it is the most important instruction for the reproduction of the Beckmann et al. paper.
However, sleep requires the activation of the energy model, which doesn't work reliably and I choose not to use it.
#### Sense
Their are several sense instruction that I can use and I have not a clear idea which one the best instruction is.
Right now I use sense-resource0 and sense-resource1, because I have two resources that either cycle or are both present
depending on the environment settings.

-- Cheers, Nic
