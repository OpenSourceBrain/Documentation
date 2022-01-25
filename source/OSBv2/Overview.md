(osbv2)=
# Open Source Brain v2

```{admonition} OSBv2 is under active development
The beta release of OSBv2 is available at https://www.v2.opensourcebrain.org. It is not currently ready for daily usage because the interface and data stored on the platform may change and be erased from time to time. Please do {ref}`get in touch <contact>` if you have any queries or would like to help with user testing.
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

Repositories are links to files and data in public resources like [GitHub](https://github.com) and [DANDI](https://gui.dandiarchive.org).

- A repository on OSBv2 lists the **current contents** of the remote resource
- Repositories are public: all users can browse repositories that have been added to OSBv2
- Private repositories, and interfaces to other resources such as [Figshare](https://figshare.com/) are also planned

(workspaces)=
## Workspaces

Workspaces are spaces for users to work in.

- Empty workspaces can be created, or they can be seeded from OSBv2 repositories using some or all of the files in the repository at the time
- Each workspace is saved on a persistent cloud volume, allowing users to save their work and resume it at a later time
- Additional files (analysis outputs, simulation results) can also be stored in the workspace
- Users can keep their workspaces private or make them public to share them with the community

(applications)=
## Applications

OSBv2 integrates a number of applications for use by researchers, and workspaces can be opened in any of the supported OSBv2 applications:

- [NWB Explorer](https://nwbexplorer.opensourcebrain.org): for the interactive exploration/visualisation of the contents of [Neurodata Without Borders](https://nwb.org) files
- [NetPyNE](https://netpyne.org): a graphical user interface for the construction and simulation of neuroscience models
- [JupyterLab](https://jupyterlab.readthedocs.io/en/latest/): a complete development environment for the Python programming language

Both NWB Explorer and NetPyNE also include inbuilt Python consoles for ad-hoc scripting and analysis, and a number of Python libraries are pre-loaded into the JupyterLab application for convenience.
