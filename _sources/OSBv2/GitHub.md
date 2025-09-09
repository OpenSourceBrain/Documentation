(osbv2:github)=
# Interacting with GitHub

[GitHub](https://github.com/) is one of the main sources for code and data on OSBv2.

Any public GitHub repository can be used as the source of an {ref}`OSB repository <osbv2:repositories>`. For example, the main repository in the {ref}`Guided tour of OSBv2 <osbv2:guidedtour>` has its source on GitHub ([GitHub repository](https://github.com/OpenSourceBrain/OSBv2_Showcase), [OSBv2 repository](https://www.v2.opensourcebrain.org/repositories/38)).

Note for GitHub based repositories and workspaces:

- Currently only **public** GitHub repositories can be used as a source for OSBv2 repositories.
- What is copied to a {ref}`workspace <osbv2:workspaces>` when it is created from a GitHub repository is a **snapshot** of the repository contents, i.e. whatever is committed to the specified branch at that time.

## Using git on workspace contents in JupyterLab

When a workspace created from a GitHub based OSB repository is opened in {ref}`JupyterLab <osbv2:applications:jupyterlab>` (e.g. from the {ref}`Guided tour OSBv2 showcase <osbv2:guidedtour>`), you can use the `git` command line tool to investigate changes in your files from the version when the workspace was created, and pull any changes from the remote repository:


```{figure} ../images/github_jlab.png
:alt: Interacting with a GitHub remote repo on JupyterLab
:align: center
:width: 700px

Interacting with a GitHub remote repo on JupyterLab

```