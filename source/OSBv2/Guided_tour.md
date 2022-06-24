(osbv2:guidedtour)=
# Guided tour of OSBv2

This guide provides a quick tour through the main features of the OSBv2 platform, using the contents of the [OSBv2 showcase repository](https://www.v2.opensourcebrain.org/repositories/38).

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

To create the new workspace, click on the blue button **CREATE NEW WORKSPACE**. The dialogue that opens allows you to set the title and tags, etc. to associate with the workspace, to make it easier to find.

```{figure} ../images/GT2.png
:alt: Guided tour...
:align: center
:width: 600px
Workspace creation dialogue
```

After it is created, you will get an option to **GO TO WORKSPACE**. Go here and you get a view of the workspace with a number of options in the top right corner on how to proceed.

```{figure} ../images/GT3.png
:alt: Guided tour...
:align: center
:width: 600px
Options for opening the workspace can be found in the top right corner
```

(osbv2:guidedtour:nwbe)=
## 3) Explore NWB datasets

Select **Open with NWB Explorer** in the drop down menu and click the blue button. The {ref}`NWB Explorer <osbv2:applications:nwbe>` interface will open.

```{figure} ../images/GT20.png
:alt: Guided tour...
:align: center
:width: 600px
NWB Explorer main interface. Note the **Resources panel** on the left (with the list of NWB files etc.) can be opened/closed with the arrows (**>**, **<**) at the bottom of the panel.
```
The column on the left lists a number of the files of known types (e.g. NWB files, Python notebooks). Select **LanoreEtAl2019.nwb** in this column, and that NWB file will be loaded in to the NWB Explorer interface.

This [dataset](https://www.biorxiv.org/content/10.1101/567172v1) contains electrophysiological recordings of Golgi cells from the cerebellum. The left hand column below gives general information on the data set extracted fro the metadata of the NWB file. The study examined the spiking behaviour under different conditions: 1) prior to application of a drug norepinephrine, 2) following application of the drug, and 3) after wash out of the drug from the brain slices. The top right panel, **Acquisition** shows the acquired data, membrane potential traces, under these conditions. Typing *Prior* into the text box on the top right selects just the traces prior to application of the drug. Pressing the eye (&#x1F441;) beside one of the individual traces will plot that trace, or the one at the bottom with "41 Matching results" will plot all of these in one figure. Similar traces for the currents injected during these trials can be found under **Stimulus**.

```{figure} ../images/GT21.png
:alt: Guided tour...
:align: center
:width: 600px
NWB Explorer view of Lanore et al. 2019 dataset.
```

(osbv2:guidedtour:netpyne)=
## 4) Create a network simulation using NetPyNE

Now open the same workspace in NetPyNE. To do this you can either go back to the homepage (e.g. click on the OSB logo in the top left corner) and find the link to the workspace page, or from a workspace open in another application, click the 3 dots (**...**) at the top of the Resources panel on the left, and select: Open with NetPyNE.

The interface below should be displayed after NetPyNE opens.

```{figure} ../images/GT31.png
:alt: Guided tour...
:align: center
:width: 600px
NetPyNE interface before a model is loaded/created.
```

There is a simple example network included in the OSBv2 repo. To open this, select menu item File -> Open... and locate the JSON file at `/home/jovyan/netpyne/workspace/OSBv2 Showcase/main/NetPyNE/HHTut/HHTut_data.json` (or paste this path into the top text field in the dialog)


```{figure} ../images/GT32.png
:alt: Guided tour...
:align: center
:width: 600px
Loading a JSON file.
```

After the model has loaded, you can explore the settings, e.g. click on **Populations** tab and then **PYR**, and you will see that this is a population of 20 cells:


```{figure} ../images/GT33.png
:alt: Guided tour...
:align: center
:width: 600px
Viweing the population present.
```

Next, try viewing in 3D (Click **CREATE NETWORK** on the top right) and you will see the view on the left below.

The network can be executed also (Click **SIMULATE** on the top right). To view one of the recorded membrane traces, press the icon on the left for **Cell Traces** and the plot on the right will appear. 


```{figure} ../images/GT34.png
:alt: Guided tour...
:align: center
:width: 600px
After creating and simulating the model.
```


(osbv2:guidedtour:jupyter)=
## 5) Open notebooks in JupyterLab

...

(osbv2:guidedtour:simulators)=
## 6) Run simulator scripts in JupyterLab
