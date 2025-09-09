(osbv2:useraccounts)=
# User Accounts on OSBv2

Users need to register and log in to OSBv2 to open a {ref}`workspace <osbv2:workspaces>` in any of the {ref}`applications <osbv2:applications>`: {ref}`NWB Explorer <osbv2:applications:nwbe>`, {ref}`NetPyNE <osbv2:applications:netpyne>` or {ref}`JupyterLab <osbv2:applications:jupyterlab>`.

(osbv2:useraccounts:register)=
## Registration

```{admonition} OSBv2 has a different user database to OSBv1
Currently there is no overlap between the user database of {ref}`OSBv1 <v1:getting_started>` and OSBv2. You will need to create a new user account to use OSBv2.
```

To register for an OSBv2 user account [click here](https://www.v2.opensourcebrain.org/register).


(osbv2:useraccounts:signin)=
## Signing in

Once registered, users can sign in by clicking the link on the top right of the homepage, or by [clicking here](https://www.v2.opensourcebrain.org/login).


(osbv2:useraccounts:storage)=
## User data storage inside a workspace

```{admonition} Warning about user storage
Note: while we will endeavour to securely store and backup all data during the life of the OSB project (we do our work on the platform too!) **we do not currently offer any guarantees**, and so encourage users to back up any valuable research data regularly.
```

There are a number of locations where data can be stored when a {ref}`workspace <osbv2:workspaces>` is opened:

| Location | Description | Persistence |
|:---|:---|:---|
| `/opt/user` | A private volume which is accessible for this user on **every workspace they open** | Persistent<sup>*</sup> |
| `/opt/workspace` | A volume which is accessible every time **this workspace** is opened (even when workspace is shared and opened by another user - it will be readonly in this case) | Persistent<sup>*</sup> |
| `/opt/workspace/my-shared` | A link to `/opt/user` above (added here so it is visible in the file menu in {ref}`JupyterLab <osbv2:applications:jupyterlab>`) | Persistent<sup>*</sup> |
| `/opt/home` | Local storage to use while using the workspace | Temporary<sup>^</sup> |
| `/opt/conda` | Location for Python packages (those preinstalled and those installed during this session). Note: this is renewed every time the workspace is reloaded, so new packages will need to be installed every session  | Temporary<sup>^</sup> |

<sup>*</sup> See warning above on user storage.

<sup>^</sup> Note: if a workspace is closed, and then opened in the same application shortly afterwards, the same Kubernetes pod may be used, along with the same transient storage, which may result in data on `/opt/home` and `/opt/conda` persisting between these sessions.

The easiest way to browse these locations is by opening the {ref}`JupyterLab <osbv2:applications:jupyterlab>` application, where other files {ref}`can be uploaded and existing files downloaded <osbv2:workspaces:addingmore>`.


(osbv2:useraccounts:quotas)=
## User quotas

Currently, new users are allowed a small number of workspaces which they can create, and there are limits to the number of applications they can run in parallel. 

To view your current quotas, click on your username on the top right when logged in and select **My account**. You can view and stop/delete your currently running workspaces by clicking the link to **Manage Running Workspaces** or by clicking [here](https://notebooks.v2.opensourcebrain.org/hub/home). 

```{admonition} Need more resources?
We're happy to provide additional resources to users and groups who wish to help test the OSBv2 infrastructure. Please {ref}`get in contact <contact>` with your requirements to discuss this further.  
```