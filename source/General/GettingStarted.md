(getting_started_osb)=
# Getting started with OSB

There are currently two versions of OSB: OSBv1, and the new version that is under active development, OSBv2.

- **{ref}`OSBv1 <v1:getting_started>`** is a web platform for sharing, viewing, analysing, and simulating models standardized in the [NeuroML 2](https://docs.neuroml.org) format from different brain regions and species. This is the version described in detail in [Gleeson et al. 2019](https://www.cell.com/neuron/fulltext/S0896-6273(19)30444-1).
- **{ref}`OSBv2 <osbv2>`** is a new integrated research platform that builds on the features of OSBv1.
  It aims to help neuroscientists close the loop between experimental data and data-driven computational/theoretical modelling.
  It integrates:

  - {ref}`NWB Explorer <osbv2:applications:nwbe>` for the visualisation and analysis of data in the [Neurodata Without Borders](https://www.nwb.org) (NWB) format
  - {ref}`NetPyNE <osbv2:applications:netpyne>` for computational modelling and simulation
  - {ref}`JupyterLab <osbv2:applications:jupyterlab>` for general Python workflows

  in a powerful cloud based web application.
  Researchers can save their work on workspaces on OSBv2, and use it for their daily research.

(getting_started_osb:which)=
## Which version of OSB should I use?

Please use **{ref}`OSBv1 <v1:getting_started>`**:

- if you want to explore the models described in [Gleeson et al. 2019](https://www.cell.com/neuron/fulltext/S0896-6273(19)30444-1) {cite}`Gleeson2019`
- if you want to visualise, analyse and simulate [NeuroML 2](https://docs.neuroml.org) models in your web browser

Please use **{ref}`OSBv2 <osbv2>`**:

- if you want to share, visualise, and analyse neuroscience data in standardised {ref}`NWB <osbv2:applications:nwbe>` format
- if you want to create, simulate, and share computational models using the {ref}`NetPyNE <osbv2:applications:netpyne>` platform
- if you want to create and share general Python based workflows using packages from the {ref}`Python ecosystem <osbv2:applications:jupyterlab>` (including [NeuroML 2](https://docs.neuroml.org))

Since OSBv2 uses cloud based infrastructure, you can save your work and data on the provided cloud storage itself, and continue where you left off at a later time.


OSBv2 is under heavy development, and all features of OSBv1 will be migrated over to OSBv2 over time.
