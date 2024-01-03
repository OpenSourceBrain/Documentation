(osbv2:applications:nwbe)=
# NWB Explorer

NWB Explorer is a web application that can be used by scientists to read, visualise and explore the content of NWB:N 2 files.

```{figure} ../images/nwbe.png
:alt: NWB Explorer on OSBv2
:align: center
:width: 700px

An instance of NWB Explorer is hosted on OSBv2.

```

To be able to visualise multiple NWB files, create notebooks to analyse the data they contain, and save/share your work, you can open NWB Explorer as an {ref}`application <osbv2:applications>` in OSBv2. You need to register/log in to do this. 

## Quick access to NWB Explorer

While NWBE is integrated into OSBv2 and can be used as an {ref}`application <osbv2:applications>` for opening  {ref}`workspaces <osbv2:workspaces>` containing NWB files, a **standalone version** of this application can be accessed (without logging in) at http://nwbexplorer.opensourcebrain.org.

This has links to number of example NWB files, and a URL to a publicly accessible NWB file can be entered to visualize its contents:

```{figure} ../images/NWBE_home.png
:alt: Main interface to NWB Explorer
:align: center
:width: 700px

Main interface to NWB Explorer with example files and option to paste in a URL to an externally hosted NWB file.

```


(osbv2:applications:nwbe:links)=
## Constructing direct links (URLs) to open NWB files in NWBE

It is possible to construct direct links (URLs) to open NWB files in NWBE for use in documentation.
The format of the URL should be:

```
http://nwbexplorer.opensourcebrain.org/nwbfile=<path to file>
```


(osbv2:applications:nwbe:links:github)=
### File hosted on GitHub

For files hosted on GitHub, for example, this will be:

```
http://nwbexplorer.opensourcebrain.org/nwbfile=https://github.com/openworm/WormsenseLab_ASH/raw/main/test_data/07-06-25-1.nwb
```

Please note that the URL of the file must be the "raw" URL so that NWBE can download it.

Example badge using this: <a href="http://nwbexplorer.opensourcebrain.org/nwbfile=https://github.com/openworm/WormsenseLab_ASH/raw/main/test_data/07-06-25-1.nwb">![Static Badge](https://img.shields.io/badge/NWB-Open_in_OSB-orange)</a>


(osbv2:applications:nwbe:links:dandi)=
### File hosted on DANDI

For NWB files hosted on DANDI, one can use the direct URL to files obtained by right clicking the "download" button, e.g.:

```
http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/0acc0d47-a8c6-4971-8130-32b0b331c838/download/
```
Example badge using this: <a href="http://nwbexplorer.opensourcebrain.org/nwbfile=https://api.dandiarchive.org/api/assets/0acc0d47-a8c6-4971-8130-32b0b331c838/download/">![Static Badge](https://img.shields.io/badge/NWB-Open_in_OSB-orange)</a>

(osbv2:applications:nwbe:links:figshare)=
### File hosted on Figshare

For NWB files hosted on Figshare, one can use the direct URL to files obtained by right clicking the "download" button, e.g.:
```
http://nwbexplorer.opensourcebrain.org/nwbfile=https://figshare.com/ndownloader/files/34273955
```
Example badge using this: <a href="http://nwbexplorer.opensourcebrain.org/nwbfile=https://figshare.com/ndownloader/files/34273955">![Static Badge](https://img.shields.io/badge/NWB-Open_in_OSB-orange)</a>

