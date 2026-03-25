(contribute:test)=
# Test OSB

Testing OSB and reporting any issues that you find is another great way of contributing to the development of OSB.
Here is a user testing template that can be used in a GitHub issue.
Each test can be marked `PASS` or `FAIL` to indicate whether an issue was found.
We have marked all tests as passing here as an example.
Please add any tests that we have missed.
The more complete the test list/matrix, the more robust and reliable OSB will be for its users.

The development deployment is tested before being deployed on the production infrastructure.
The URL for the development deployment is: https://v2dev.opensourcebrain.org


```{code-block} markdown

# Testing template for OSBv2.

- Deployment: development/production
- Date/time:

Statuses:

- PASS: test passes
- FAIL: test fails
- NA: not applicable


## Website loading

- Website loads: PASS

### Services

Note that while everyone can check if these services are up, only admins will be able to login to check logs and so on.

- KeyCloak is up: https://accounts.v2dev.opensourcebrain.org/: PASS
- Argo is up: https://argo.v2dev.opensourcebrain.org/: PASS
- Swagger is up: <url>?
- Sentry is up: <url>?


## Left side bar

- All links are valid and work: PASS
- Workspaces button works: PASS
- Repositories button works: PASS
- "Create new" button shows "login" dialog: PASS

## Usage before signing in

- Featured workspaces load: PASS

### Workspaces

- Public workspaces load: PASS
- No private workspaces load: PASS
- Workspaces: icon view works: PASS
- Workspaces: list view works: PASS
- Text search functionality works in both views: PASS
- Text search is maintained when switching between public and featured workspaces: PASS
- Tag search functionality works in both views: PASS
- Tag search is marked when active in both views: PASS
- Deslecting tag removes it from search: PASS
- Selecting a tag activates search: PASS
- Pagination works: PASS
- Clicking on a workspace title opens workspace: PASS

### Repositories

- Repository index loads: PASS
- Text search functionality works in both views: PASS
- Tag search functionality works in both views: PASS
- Tag search is marked when active in both views: PASS
- Deslecting tag removes it from search: PASS
- Pagination works: PASS
- Repository entry username is correct: FAIL (capitalised?)

## Authentication

- Login button goes to the login page: PASS

### New user registration

- New user registration link works: PASS
- Form validation for e-mail works: PASS
- Form validation for username works: FAIL
- Register with Orcid goes to ORCID authentication: PASS
- Register with GitHub goes to GitHub authentication: PASS

### Login

- Logging in with valid username/password works: PASS
- Logging in with invalid username/password works: PASS

## Logged in user

- New user greeted with "Create your first workspace": PASS

### My account

- Link works and page loads: PASS
- "Manage running workspaces" link works: PASS
- "Edit my profile" button works: PASS

#### Edit my profile

- Profile picture URL addition works: PASS
- Changing display name works: FAIL
- Changing e-mail works: PASS
- Adding links works and profile page is updated: PASS

## Adding new repository

### General

- Invalid repository URL shows error: PASS
- Image upload works: PASS
- Valid repository URL loads metadata:

  - GitHub: PASS
  - DANDI: FAIL: intermittently fails when URL is pasted
  - FigShare: FAIL: unclear what valid FigShare URLs are. Perhaps the error message should specify to help users.
  - BioModels: PASS

- Repository is correctly added: PASS

  - GitHub: PASS
  - DANDI: FAIL: intermittently fails when URL is pasted
  - FigShare: NA
  - BioModels: PASS

- Repository listed in user page under repositories tab: PASS

  - GitHub: PASS
  - DANDI: FAIL: intermittently fails when URL is pasted
  - FigShare: NA
  - BioModels:

- Repository duplication is avoided: PASS: looks like one can add duplicates


## Repository detail page


- File list loads correctly:

  - GitHub: PASS
  - DANDI: PASS
  - FigShare: NA
  - BioModels: PASS


## Workspace creation

### From repository

- New workspace from selection works: without selections:

  - GitHub: PASS
  - DANDI: UNTESTED (large data files)
  - FigShare: NA
  - BioModels: PASS

- New workspace from selection works: with selections:

  - GitHub: PASS
  - DANDI: UNTESTED (large data files)
  - FigShare: NA
  - BioModels: PASS

- Workstation files are downloaded correctly

  - GitHub: PASS
  - DANDI: UNTESTED (large data files)
  - FigShare: NA
  - BioModels: FAIL (needs more testing: file list was present, but not the file)


- New workspace from selection: workspaces are private by default: PASS
- Private workspaces are clearly marked: FAIL (no indicator that a workspace is private?)

### Not from repository

- New workspace can be created for JupyterLab: PASS
- New workspace can be created for NetPyNE-UI: PASS
- New workspace can be created for NWBE: PASS

## Applications

- Left side bar works: PASS
- Resources appear in left hand side bar: PASS

### JupyterLab

- JupyterLab loads correctly: PASS

### NWB Explorer

- NWBE loads correctly: PASS
- Clicking on acquisition/stimulus opens plots: FAIL (needs to be checked on prod)

### NetPyNE-UI

- NetPyNE-UI loads correctly: PASS
- Examples are loaded correctly: PASS
- NetPyNE-UI works correctly: PASS (tested with first example)

```
