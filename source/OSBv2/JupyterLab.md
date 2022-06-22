(osbv2:applications:jupyterlab)=
# JupyterLab

OSBv2 hosts a [JupyterLab](https://jupyterlab.readthedocs.io/en/latest/user/index.html) instance as one of its {ref}`applications <osbv2:applications>`.

```{figure} ../images/jlab.png
:alt: JupyterLab on OSBv2
:align: center
:width: 700px

An instance of JupyterLab is hosted on OSBv2.

```

You must be signed in to open a {ref}`workspace <osbv2:workspaces>` (which may have been originally created for {ref}`NWB Explorer <osbv2:applications:nwbe>` or {ref}`NetPyNE <osbv2:applications:netpyne>`) in the JupyterLab application on OSBv2.

(osbv2:applications:jupyterlab:features)=
## Features

### File management
A significant feature of the JupyterLab application is the file browser, where {ref}`workspace storage <osbv2:useraccounts:storage>` can be viewed, and {ref}`files can be uploaded and existing files downloaded <osbv2:workspaces:addingmore>`.

(osbv2:applications:jupyterlab:configuration)=
## Configuration

What Python packages are available in the JupyterLab environment? Try `pip list` in the Terminal to see the current set of packages.

These are set in the Dockerfile for the JupyterLab application ([master version](https://github.com/OpenSourceBrain/OSBv2/blob/master/applications/jupyterlab/Dockerfile), [latest development version](https://github.com/OpenSourceBrain/OSBv2/blob/develop/applications/jupyterlab/Dockerfile)).
