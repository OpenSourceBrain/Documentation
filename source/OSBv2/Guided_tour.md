(osbv2:guidedtour)=
# Guided tour of OSBv2

This guide provides a quick tour through the main features of the OSBv2 platform.

(osbv2:guidedtour:register)=
## 1) Register & sign in to OSBv2

To create and open the workspaces mentioned below, you need to have an OSBv2 account (OSBv1 username/password will not work...). To register for an OSBv2 user account [click here](https://accounts.v2.opensourcebrain.org/auth/realms/osb2/login-actions/authenticate?client_id=web-client).

```{figure} ../images/GT0.png
:alt: Guided tour...
:align: center
:width: 600px
Register on OSBv2
```

Once registered, users can sign in by clicking the link on the top right of the homepage, or by [clicking here](https://accounts.v2.opensourcebrain.org/auth/realms/osb2/login-actions/authenticate?client_id=web-client).

More details on OSBv2 user accounts (file storage, quotas, etc.) can be found {ref}`here <osbv2:useraccounts>`.


(osbv2:guidedtour:createworkspace)=
## 2) Create a new workspace

We will now create a {ref}`workspace <osbv2:workspaces>` which will hold files which can be viewed and analysed in our OSBv2 {ref}`applications <osbv2:applications>`.

This workspace will be a copy of a {ref}`repository <osbv2:repositories>`, **OSBv2 Showcase** which contains a number of file types supported by OSBv2.

Go to the repository page at https://www.v2.opensourcebrain.org/repositories/38 to see the current contents of this repository.

```{figure} ../images/GT1.png
:alt: Guided tour...
:align: center
:width: 600px
Create a new workspace from the [OSBv2 Showcase](https://github.com/OpenSourceBrain/OSBv2_Showcase) repository
```

As you can see there is a link to the source of the files on GitHub, https://github.com/OpenSourceBrain/OSBv2_Showcase. Any additions/changes to GitHub will be reflected in the view of it on the OSB repository page.

To create the new workspace, click on the blue button CREATE NEW WORKSPACE. The dialogue that opens allows you to set the title and tags, etc. to associate with the workspace, to make it easier to find.

```{figure} ../images/GT2.png
:alt: Guided tour...
:align: center
:width: 600px
Workspace creation dialogue
```

After it is created, you will get an option to GO TO WORKSPACE. Go here and you get a view of the workspace with a number of options in the top right corner on how to proceed.

```{figure} ../images/GT3.png
:alt: Guided tour...
:align: center
:width: 600px
Options for opening the workspace can be found in the top right corner
```

(osbv2:guidedtour:nwbe)=
## 3) Explore NWB datasets

Select NWB Explorer in the drop down menu and click the button. The {ref}`NWB Explorer <osbv2:applications:nwbe>` interface will open.

```{figure} ../images/GT20.png
:alt: Guided tour...
:align: center
:width: 600px
NWB Explorer main interface
```
The column on the left lists a number of the files of known types (e.g. NWB files, Python notebooks). Select **LanoreEtAl2019.nwb** in this column, and that NWB file will be loaded in to the NWB Explorer interface.

```{figure} ../images/GT21.png
:alt: Guided tour...
:align: center
:width: 600px
NWB Explorer view of Lanore et al. 2019 dataset. 
```

(osbv2:guidedtour:netpyne)=
## 4) Create a network simulation using NetPyNE

...

(osbv2:guidedtour:jupyter)=
## 5) Open notebooks in JupyterLab

...

(osbv2:guidedtour:simulators)=
## 6) Run simulator scripts in JupyterLab
