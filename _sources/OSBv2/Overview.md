(osbv2)=
# Open Source Brain v2

```{admonition} OSBv2 is live!
The latest release of OSBv2 is available at **https://v2.opensourcebrain.org**. Please do {ref}`get in touch <contact>` if you have any queries or would like to help with user testing.
```

Open Source Brain (OSB) v2 is a new integrated research platform that builds on the features of {ref}`OSBv1 <v1:getting_started>`.
It is currently under active development, but is stable enough for users to start using it in their research.

OSBv2 is structured around 3 key concepts: **Repositories**, **Workspaces** and **Applications**.

```{figure} ../images/OSBv2Overview.png
:alt: OSBv2 Overview
:align: center
:width: 500px

Relationship between Repositories, Workspaces and Applications on OSBv2.

```

(repositories)=
## Repositories

Repositories are views of sets of files and data in public resources like {ref}`GitHub <osbv2:github>`, {ref}`Figshare <osbv2:figshare>` and {ref}`DANDI Archive <osbv2:dandi>`.

- A repository page on OSBv2 lists the **current contents** of the remote resource (e.g. GitHub repository, FigShare project)
- OSB Repositories are public: all users can [browse repositories](https://v2.opensourcebrain.org/repositories) that have been added to OSBv2
- Private repositories, and interfaces to other neuroinformatics resources are also planned

More details on repositories can be found {ref}`here <osbv2:repositories>`.

(workspaces)=
## Workspaces

Workspaces are persistent spaces for users to carry out their work in.

- Empty workspaces can be created, or they can be seeded from OSBv2 {ref}`repositories <osbv2:repositories>` using some or all of the files in the repository at that point in time
- Each workspace is saved on a {ref}`persistent cloud volume <osbv2:useraccounts:storage>`, allowing users to save their work and resume it at a later time
- Workspaces can be opened in any {ref}`OSBv2 application <osbv2:applications>`, and any files which are generated (e.g. analysis outputs, simulation results) are also stored in the workspace, and other files {ref}`can be uploaded <osbv2:workspaces:addingmore>`
- Users can keep their workspaces private or make them public to share them with the community

More details on workspaces can be found {ref}`here <osbv2:workspaces>`.

(applications)=
## Applications

OSBv2 integrates a number of applications for use by researchers, and workspaces can be opened in any of the supported OSBv2 applications:

- {ref}`NWB Explorer <osbv2:applications:nwbe>`: for the interactive exploration/visualisation of the contents of [Neurodata Without Borders](https://nwb.org) files
- {ref}`NetPyNE <osbv2:applications:netpyne>`: a graphical user interface for the construction and simulation of neuroscience models
- {ref}`JupyterLab <osbv2:applications:jupyterlab>`: a complete development environment for the Python programming language

Both {ref}`NWB Explorer<osbv2:applications:nwbe>` and {ref}`NetPyNE <osbv2:applications:netpyne>` also include inbuilt Python consoles for ad-hoc scripting and analysis, and a number of Python libraries are pre-loaded into the {ref}`JupyterLab <osbv2:applications:jupyterlab>` application for convenience.

More details on OSBv2 applications can be found {ref}`here <osbv2:applications>`.
