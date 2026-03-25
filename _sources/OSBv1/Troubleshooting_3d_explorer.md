(v1:troubleshooting_3d)=
# Troubleshooting the 3D explorer

When viewing larger and more complex models in the {ref}`3D explorer <v1:five_min_intro:explorer>` on OSBv1, and depending on the computing load that the OSB cluster is experiencing (with multiple users for example), it can sometimes take longer than expected to load the explorer interface.
Here are some general tips to follow if you experience delays when loading the project:

- If you see a white page with the text "Loading project .." but the explorer does not load, please **refresh the page** a few times (using `control + r` or `F5` in most browsers, or the "reload" button). This re-initialises the explorer.

- After the 3D explorer has loaded you may see the Open Source Brain logo rotating in the page (either in the centre of the top left hand corner), this is the progress timer showing that the operation you attempted to carry out (for example: loading connections or recorded data in plots) is being processed.
Depending on the amount of data being loaded, this may take a few minutes.
If it does not load after a few (say 3-5 minutes), please refresh the page.

(v1:troubleshooting_3d:contact)=
## Contact us

If waiting and refreshing the page does not solve the issue, please {ref}`contact us <contact>` and provide us with the following information:

- the time at which you were accessing the platform (with your time zone information)
- what project(s) you were working with
- what operations you were attempting to carry out.

This will allow us to check the platform logs to see if there's an issue that we should fix.

Alternatively, there are more specific details of the scenarios when the 3D interface fails to load in **[this issue](https://github.com/OpenSourceBrain/geppetto-osb/issues/347)**. Please see there or add comments with your experiences. 
