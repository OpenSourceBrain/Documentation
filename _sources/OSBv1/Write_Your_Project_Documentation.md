(v1:document_project)=
# Document your project
There are a number of options for adding documentation and annotating your OSB project:


## Add a README file in your GitHub repository and reuse it on your OSB projects

A [README file](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) is a great way to give a quick overview of the contents of your repository and how to use it. If you share your code on GitHub, adding a README at the top level means that anyone who comes to the repository can see a quick introduction to the contents. These are generally created in easy to edit [Markdown format](https://daringfireball.net/projects/markdown/basics).

To avoid the need to copy/paste the description and to avoid the summary going out of data in one place, you can reuse the exact contents of the README from GitHub for your main description on OSB. Just add the following to the text field for the main project description in Settings:

```{code-block}
github:README.md
```

```{figure} ../images/README_settings.png
:alt: README
:align: center
:width: 50 %
```

For example this: https://github.com/OpenSourceBrain/ACnet2/blob/master/README.md is also used as the project description in the OSB project page here: http://www.opensourcebrain.org/projects/acnet2.

## Set values for custom fields

A number of values can be set for fields of the project in OSB to categorise the model, link to other resources, and facilitate finding the model on OSB. These include the location of the original scripts on [ModelDB](https://senselab.med.yale.edu/ModelDB/default), the species and brain region being modelled, and the state of curation of the model.

These can be accessed at Settings. **Note: you need to click the <u>Custom Fields</u> tab under <u>Admin settings</u> to change these values!**

```{figure} ../images/Settings_fields.png
:alt: README
:align: center
:width: 30 %
```


## Add Wiki pages to OSB projects

To add a new Wiki page to your OSB project click on the "Wiki" link on the project option bar (when logged in) and start editing the wiki page.

OSB documentation is written in [Markdown format syntax](https://daringfireball.net/projects/markdown/basics), together with some further Redmine and OSB specific additions (see below for further information).
Note Markdown allows you to include most HTML syntax (i.e. videos...).
In order to be as compatible as possible with GitHub wikis, OSB uses [GitHub Flavored Markdown](https://help.github.com/articles/markdown-basics).
You can find a cheatsheet [here](https:www.opensourcebrain.org/help/en/wiki_markdown_syntax.html).

We describe briefly below some OSB/Redmine features to enhance Wiki pages on OSB (these can also be used in the text field for the main project description in Settings).

### Reference to a Repository file.

You can point to any file (markdown or plain text) in your GitHub or Bitbucket repository (the repository used in your project).

```{code-block}
github:[path]
bitbucket:[path]
```

This will retrieve the file content and display it in the OSB wiki page. This allows a single file in your repo (e.g. the main README.md) to be the master copy of the documentation for your project, and to make that accessible to someone browsing the project on OSB.

*Example:*

```{code-block}
github:help/readme.md
bitbucket:help.txt
```


### Reference to [PubMed](https://www.ncbi.nlm.nih.gov/pubmed/) publication:

```{code-block}
pubmed:[publicationID]
```

*Example:*

```{code-block}
pubmed:17442244
```

This syntax will generate a reference link like this (link only correctly rendered on OSB): pubmed:17442244 and a bibliography section will be automatically generated at the bottom of the page.


### Create a formula

You can write formulas in your documentation using the LaTeX syntax. You only need to enclose you formula like this:

```{code-block}
{{latex(formula)}}
```

*Example:*

```{code-block}
{{latex(x=\frac{-b\pm\sqrt{b^2-4ac}}{2a})}}
```

This will automatically generate the following image using the [google chart API](https://developers.google.com/chart/infographics/docs/formulas):
![](https://raw.githubusercontent.com/OpenSourceBrain/OSB_Documentation/master/resources/images/formula.png)

### Link to Wiki page

If you want to link to other Wiki page:

```{code-block}
[[Wiki page]]
```

<a href="#">Wiki page</a>

### Link to an Issue

If you want to link to an issue in your project:

```{code-block}
Issue #12
```

Issue <a href="#">#12</a>

### Link to a Commit

If you want to link to a commit in your repository:

```{code-block}
commit:f30e13e43
```

<a href="#">f30e13e4</a>
