(osbv2:workspaces)=
# Workspaces

Workspaces are spaces for users to work in.
Each workspace is saved on a persistent cloud volume, allowing users to save their work and resume it at a later time.
Users can add files to workspaces from {ref}`repositories <osbv2:repositories>`, or uploaded them from their computers.
Workspaces can be public, private, or featured.

- **private workspaces** are only visible and accessible to the user that created them
- **public workspaces** are visible to everyone but can only be modified by their creators
- **featured workspaces** are public workspaces that have been curated by the OSBv2 administrators

(osbv2:workspaces:existing)=
## Working with existing workspaces

All of these workspaces can be seen on the OSBv2 homepage in the right hand panel.
Users can select the appropriate tab to switch between different types of workspaces.

```{figure} ../images/osbv2-workspaces-homepage-with-text.png
:alt: Figure showing workspaces listed on the OSBv2 homepage
:align: center
:width: 500px

Workspaces can be seen on the OSBv2 homepage.

```

Workspaces can be opened in any of the OSBv2 applications.
This can be done either directly from the homepage by using the context menu for each workspace in the list, or from the workspace information page.

```{figure} ../images/osbv2-workspaces-page-with-text.png
:alt: Figure showing workspace information page
:align: center
:width: 500px

The workspace information page shows details about the workspace, including what resources it includes.

```
Workspaces include files, and they can also include **resources**.
Resources are special files that OSBv2 knows can be opened in one of the OSBv2 applications.
These can be seen in the resources side bar in the left hand pane in workspaces and applications.

Clicking on a resource will open it in the associated application:

- NWB files will open in NWB Explorer
- NetPyNE files will open in NetPyNE
- Jupyter Notebooks will open in JupyterLab

(osbv2:workspaces:creating)=
## Creating a new workspace

There are two ways to create workspaces on OSBv2, both available on the OSBv2 homepage.
You can either create blank/empty workspaces without any files/resources, or you can seed workspaces from files included in a repository that you have access to.

```{figure} ../images/osbv2-workspaces-homepage-create-with-text.png
:alt: Figure showing options on homepage to create a new workspace.
:align: center
:width: 500px

Workspaces can be created using the options on the OSBv2 homepage.

```
A new workspace can be created from a repository from two views:

- from the OSBv2 homepage by selecting the "Workspace from repository" button
- from the repository information page, as explained {ref}`here <osbv2:repositories:viewing>`.

Clicking on the "Workspace from repository" button on the main page opens the "Create a new workspace" dialogue box.
Here, you can select what repository you would want to use to include files from in your new workspace.

```{figure} ../images/osbv2-workspaces-from-repo-dialog.png
:alt: Figure showing repository selection dialogue box for new workspace creation.
:align: center
:width: 500px

Select a repository from the list.

```
This will take you to the file selection panel.
Select the files you want you would like to include, and click "Continue" to proceed.

```{figure} ../images/osbv2-workspaces-from-repo-file-select-dialog.png
:alt: Figure showing file selection dialogue box for new workspace creation.
:align: center
:width: 500px

Select files to include in your workspace from the list.
```

The last screen allows you to set up your workspace.
Here, you can add a name, tags, a description, and a thumbnail for your workspace.

```{figure} ../images/osbv2-workspaces-create-dialog.png
:alt: Figure showing repository selection dialogue box for new workspace creation.
:align: center
:width: 500px

Add a name, tags, description, and thumbnail for your workspace.
```


Your workspace will be added to your list of workspaces, and is ready to use.
By default, new workspaces are private.
You can select "Make public" from the menu for each workspace to make them public.


(osbv2:workspaces:addingmore)=
## Adding files to existing workspaces

More files can be added to existing workspaces also.
You can either do this by going to a repository, and selecting files to add from the repository page as documented {ref}`here <osbv2:repositories:viewing>`, or you can go to the workspace information page and add files from there.

```{figure} ../images/osbv2-workspaces-add-new-resources-with-text.png
:alt: Figure showing the "Add new resources" button on the workspace information page.
:align: center
:width: 500px

More files/resources can be added to workspaces.
```

This will bring up the "Add new resources" dialogue box, where you can either add files from a URL, or from OSBv2 repositories.

```{figure} ../images/osbv2-workspaces-add-new-resources-dialog.png
:alt: Figure showing the "Add new resources" dialogue box.
:align: center
:width: 500px

The "Add new resources" dialogue box allows you to add files from a location, or a repository.
```

It is not currently possible to upload files/resources using the resources side bar.
You can, however, upload files using the JupyterLab application.
