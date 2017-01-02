## General
This week I had to unexpectedly pause the project, because of the planning of next semesters Python data analysis class at [HHU](http://www.biologie.hhu.de). However, this allowed me to work more extensively on the [Python reference project](https://github.com/schmelling/python_materials), since I'm reconstructing parts of the class and needed new resources for this. Besides this I tried to work on different smaller tasks to still keep the project running, such as learning about screencasts and docker.

I also contact [protocols.io](https://www.protocols.io), a platform for wet lab protocols, in order to suggest the integration of a [JATS](http://jats4r.org) export format. I already got a positive reply saying that they try to implement it in the near future.

Finally, I booked my plane tickets to the US for my stay at MSU in January/February.

### Events

I'll be attending the following events the next couple of weeks:

* [Google Digital Workshop](https://digitalworkshop.withgoogle.com/events#!/duesseldorf) at HHU
* Synthetic Microbiology Retreat (including presentation about the project)
* [OpenCon 2016](http://www.opencon2016.org/opencon_2016_berlin) in Berlin

### In Lab Learning

We started a small learning environment in our lab based on the model that is already working in Titus Brown's lab at UC Davis. This "in lab learning" should provide an environment where we meet for an hour each week and learn something together or get guided instructions. The idea is that people in the lab have a place where they can go to get advice and help when they are struggling with something so they don't have to learn everything on their own. We are probably starting with some guided introductions about programming with Python or R. Daniel was wondering if we document our activities and thought it would great to have some kind of readthedocs where we post the material and tutorials.

## Screencast

Daniel suggested to record some screencasts for the  installation of Python and Avida to begin with. So I did some research on how to record a screencast and found an easy solution, where I use Quicktime and iMovie on my Mac. We also talked about using open source solutions for that but couldn't come up with an answer. So if you have an answer please let me know.    
I will try to create my first screencast about Python installation next week. However, I'm a little bit confused about how to make a screencast about the installation of something I already have installed. Do I uninstall it and reinstall it? In the case of Python I thought about a virtualenv in which I show the command line instructions for installing additional packages. But this woundn't help with the initial set up of miniconda for example. In the case of Avida I thought about using a docker container, which brings me to my next point.

## Docker

As already mentioned last week I had some problems with installing Avida on my Linux machine and I thought about by passing this with a docker container. I couldn't find an Avida docker container in the docker hub, even though I'm sure that there were some a couple of months ago. Since I'm new to docker I have no idea how to create a new docker image/file. However, I like the idea of having an Avida container and a container for my whole project. So I will start learning more about docker and hopefully end up creating a solid Avida container.
