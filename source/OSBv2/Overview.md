(osbv2)=
# Open Source Brain v2

```{admonition} OSBv2 is under active development
The beta release of OSBv2 is at https://www.v2.opensourcebrain.org. Subject to change without notice. Please {ref}`get in touch <contact>` if you have questions or would like to help with user testing.
```

Open Source Brain v2 is structured around 3 key concepts: **Repositories**, **Workspaces** and **Applications**.


```{figure} ../images/OSBv2Overview.png
:alt: OSBv2 Overview
:align: center
:width: 600px

Relationship between Repositories, Workspaces and Applications on OSBv2.

```

(repositories)=
## Repositories

Repositories are links to sets of files and data in public resources like GitHub

- OSBv2 lists the **current contents** of the remote resource
- All users can browse the repositories
- Interfaces to Figshare, DANDI Archive and others are planned

(workspaces)=
## Workspaces

Workspaces can be created by users from a subset (or all) of the contents of repositories

- These are a **snapshot** of the repository contents, each saved on a **persistent cloud volume**
- Additional files (analysis outputs, simulation results) can be added to the volume
- Users can keep them private or make them public
- New empty workspaces can also be created


(applications)=
## Applications

Workspaces can be opened in any of the OSBv2 Applications

- **NWB Explorer** allows interactive exploration of the contents of Neurodata Without Borders files
- The **NetPyNE** graphical user interface allows construction and simulation of neural networks
- Both above have inbuilt Python consoles
- **JupyterLab** is a complete environment for running Python notebooks and managing/viewing multiple file types. Many neuroscience libraries are preloaded.
