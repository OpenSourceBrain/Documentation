(contribute:test)=
# Test OSB

Testing OSB and reporting any issues that you find is another great way of contributing to the development of OSB.
Here is a user testing template that can be used in a GitHub issue.
Each test can be marked `PASS` or `FAIL` to indicate whether an issue was found.
We have marked all tests as passing here as an example.
Please add any tests that we have missed.
The more complete the test list/matrix, the more robust and reliable OSB will be for its users.


```{code-block} markdown
## Website loading

- Website loads: PASS

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
- Logging in with invalid username/passworkd works: PASS



```
