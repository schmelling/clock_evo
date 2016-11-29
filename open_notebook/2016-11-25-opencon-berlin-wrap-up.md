## Wrap Up OpenCon Berlin
Last week I was back in Berlin for the [OpenCon 2016](http://www.opencon2016.org/opencon_2016_berlin) 'satellite' event. It was a great experience with a lot of smart and inspiring people. Conference from the open science community are so welcoming compared to the most scientific conferences I've been to.     
The conference was structured into three events. Day 1 was a hackathon mainly about reproducibility, but also people from PaperHive, WorldBrain, or the Open Knowledge Maps had some projects to work on. Day 2 was a regular conference with talks and break out sessions. The last day was a focus group discussion on next steps and ideas about how to put open science to action.

### Reproducibility Hackathon
Prior to the [hackathon](https://github.com/annakrystalli/OpenConBerlin_ReproHack) anyone could [submit papers](https://annakrystalli.shinyapps.io/OpenConBerlin_reprohack/) that where then open for attendance to reproduce during the event. In the end 13 papers with different requirements regarding the programming language and difficulty level were submitted. The hackathon was great experience and should try to host some myself as a teaching event for reproducibility.

We, myself and Tim Korjakow, were trying to reproduce a [paper](http://www.journals.uchicago.edu/doi/10.1086/589889) by [Daniel Falster](https://twitter.com/adaptive_plant). This was actually a pretty easy task, because Daniel did a great job writing his code. We only need to download the code from [figshare](http://dx.doi.org/10.6084/m9.figshare.1094315), open R, install a package, and run one command to reproduce all of his figures. A more comprehensive report can be found in the [issue tracker](https://github.com/annakrystalli/OpenConBerlin_ReproHack/issues/3) or the [etherpad](https://public.etherpad-mozilla.org/p/OpenConBerlin2016_ReproHack_blog). The installation of the additional package was not included in his reproduction instructions, however, it was easy to do it ourself. Nevertheless, we suggest to add these information to the instructions for others who might struggle with it.       
The greatest part of the reproducibility hackathon was that Daniel, even though he was in Australia, got back to us and [added the suggestions](https://github.com/dfalster/Falster_2008_AmNat_offspring_model). I was so awesome that it worked so easy and that he responded so quickly and was open for these suggestions.

Other people also had great experiences with reproducing publications, however, there were also some publications we couldn't reproduce at all. It is now planned by [Jon](https://twitter.com/protohedgehog) and [Anna](https://twitter.com/annakrystalli), who organized the hackathon, to write a short article about the experiences and maybe even submit it to [RIO journal](http://riojournal.com/).

### Tools and Projects
In the following I'll list some useful tools and projects that were either presented at OpenCon Berlin or I learned about in conversations.

#### [Open Knowledge Maps](http://openknowledgemaps.org/)
[Open Knowledge Maps](http://openknowledgemaps.org/) present a new way to discover research results by providing a visual interface. They produce a cluster map of the 100 most relevant papers for your search term. The underlying algorithm groups the paper by the amount of shared words.

#### [PaperHive](https://paperhive.org/)
[PaperHive](https://paperhive.org/) is a collaborative reading platform that allows for discussion and research communication. A similar approach that allows you annotate all online material, not only the one that is accessible on the platform, is hypothes.is.

[Live Demo](https://paperhive.org/documents/0tsHJq1-yyVZ)

#### [hypothes.is](https://hypothes.is/)
[hypothes.is](https://hypothes.is/) developed a browser plug-in that lets you annotate web pages. It provides a new layer on top of the normal web pages, where you take notes or discuss content. hypothes.is is also integrated into the Open Knowledge Maps such that you can comment on the publications you found in your search. "It leverages annotation to enable sentence-level critique or note-taking on top of news, blogs, scientific articles, books, terms of service, ballot initiatives, legislation and more."

[Video](https://youtu.be/QCkm0lL-6lc)

#### [WorldBrain](http://www.worldbrain.io/)
[WorldBrain](http://www.worldbrain.io/) offers a full-text search engine for your browser history and bookmarks. It is a browser plug-in that tries to eliminate re-googling things, because you can access your browser history and bookmarks only by keywords and filters. WorldBrain also connects content by analyzing your search history and metadata with the goal to annotate and proofread the internet.

#### [Digital Science](https://www.digital-science.com/)
"[Digital Science](https://www.digital-science.com/) exists to facilitate the flow of scientific information between researchers, and between researchers to society at large" - WIRED

[Digital Science](https://www.digital-science.com/) is a hub that guides researchers to tools that support them at every stage of the research cycle. These tools include Overleaf, figshare, and Altmetric.

#### [Overleaf](https://www.overleaf.com/)
[Overleaf](https://www.overleaf.com/) an online platform for collaborative writing and publishing. It allows you, together with others, to write any kind of document (from research article to presentation) in LaTeX and in a rich text format. Overleaf features also the direct submission to scientific journals and preprint servers. A similar platform is [Authorea](https://www.authorea.com/).

[Video](https://youtu.be/g8Ejj0T0yG4)

#### [ScienceOpen](https://www.scienceopen.com/)
[ScienceOpen](https://www.scienceopen.com/) is a free network for rewarding and encouraging Open Science practices. It allows anyone to discover research results and to rate these results by publicly peer reviewing article. It also allows you to create collection on a specific research topic that is independent of a journal. Furthermore, ScienceOpen provides an open access platform for publishing your research.

[Video](https://youtu.be/pzvDMF2z8_I)

#### [figshare](https://figshare.com/)
"[figshare](https://figshare.com/) wants to open up scientific data to the world" - WIRED

[figshare](https://figshare.com/) is online data repository where researches can store data, code, figures, and presentations. Furthermore, researchers get the get credit they deserve for it by securing the work with a DOI and making it citable.

[Video](https://youtu.be/WlJlPmoJcJk)

#### [RIO Journal](http://riojournal.com/)
"The Research Ideas and Outcomes [(RIO) Journal](http://riojournal.com/) publishes all outputs of the research cycle, including: project proposals, data, methods, workflows, software, project reports and research articles together on a single collaborative platform, with the most transparent, open and public peer-review process."

[Video](https://youtu.be/2QKp4Ttpemw)

#### [F1000Research](https://f1000research.com/)
"[F1000Research](https://f1000research.com/) is an Open Science publishing platform offering immediate publication of articles, posters and slides with no editorial bias. All articles benefit from transparent [post] peer review and the inclusion of all source data."

#### [Sciencematters](https://www.sciencematters.io/)
"Here at [Sciencematters](https://www.sciencematters.io/), we publish the true unit of science, the observation. [...] We guarantee publication of all scientifically solid observations. [...] Standard data, orphan data, negative data, confirmatory data and contradictory data are all published."

[Video](https://vimeo.com/144113476)

#### [Protocols.io](https://www.protocols.io/)
[Protocols.io](https://www.protocols.io/) is "an open access repository of science methods and a collaborative protocol-centered platform". It allows researchers to share and get credit for their methods with the ability of correction and optimization of methods. It is the equivalent of GitHub for methods and protocols. Protocols.io comes with a mobile and browser app for active work at the bench. It also features a growing collection of protocols for commercial products.

[Video](https://youtu.be/wvqw6PPl0eY)

#### [Altmetric](https://www.altmetric.com/)
"Thousands of conversations about scholarly content happen online every day. [Altmetric](https://www.altmetric.com/) tracks a range of sources to capture and collate this activity, helping you to monitor and report on the attention surrounding the work you care about."

[Video](https://youtu.be/M6XawJ7-880)

### Up Next

On the last day of OpenCon Berlin we met for a discussion session in a focus group to talk about how to put Open Science to action. We had a lot of ideas on how to raise awareness about Open Science. However, we didn't could to the point where we actually had some guidelines. Thus, we started a [Google Group](https://groups.google.com/forum/?hl=de#!forum/openconberlin_action) and wrote down some thoughts in an [etherpad](https://public.etherpad-mozilla.org/p/OpenConBerlin2016). The goal is to create a "how to guide" or a collection of resources that helps researchers to get started with Open Science and write an article for RIO journal that summarizes our findings.

-- Cheers, Nic
