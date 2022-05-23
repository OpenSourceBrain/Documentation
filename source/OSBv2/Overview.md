(osbv2)=
# Open Source Brain v2

```{admonition} OSBv2 is under active development
The beta release of OSBv2 is available at https://www.v2.opensourcebrain.org. Please do {ref}`get in touch <contact>` if you have any queries or would like to help with user testing.
```

Open Source Brain (OSB) v2 is a new integrated research platform that builds on the features of {ref}`OSBv1 <v1:getting_started>`.
It is currently under heavy development, and initial releases for use by the research community are planned for mid 2022.

OSB v2 is structured around 3 key concepts: **Repositories**, **Workspaces** and **Applications**.

```{figure} ../images/OSBv2Overview.png
:alt: OSBv2 Overview
:align: center
:width: 500px

Relationship between Repositories, Workspaces and Applications on OSBv2.

```

(repositories)=
## Repositories

Repositories are views of files and data in public resources like [GitHub](https://github.com), [Figshare](https://figshare.com) and [DANDI](https://gui.dandiarchive.org).

- A repository on OSBv2 lists the **current contents** of the remote resource
- Repositories are public: all users can browse repositories that have been added to OSBv2
- Private repositories, and interfaces to other neuroinformatics resources are also planned

More details on repositories can be found {ref}`here <osbv2:repositories>`.

(workspaces)=
## Workspaces

Workspaces are persistent spaces for users to carry out their work in.

- Empty workspaces can be created, or they can be seeded from OSBv2 {ref}`repositories <osbv2:repositories>` using some or all of the files in the repository at the time
- Each workspace is saved on a {ref}`persistent cloud volume <osbv2:useraccounts:storage>`, allowing users to save their work and resume it at a later time
- Additional files (analysis outputs, simulation results) can also be stored in the workspace
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
