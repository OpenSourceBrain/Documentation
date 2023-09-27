(v1:API)=
# API for OSBv1

An API for getting access to information contained in OSB projects has been developed.

See https://github.com/OpenSourceBrain/OSB_API.

## REST API

This is based on the [REST API](http://www.redmine.org/projects/redmine/wiki/Rest_api) which was developed for [Redmine](http://www.redmine.org), the framework on which OSB is based. 

An example of the data returned by this REST API for each project on OSB can be see here: http://www.opensourcebrain.org/projects/thalamocortical.xml.

## Python API

A Python module (osb) has been developed which uses this REST API and allows scripts to be developed which use the information retrieved about OSB projects.

A simple example of usage is shown below:

    import osb

    for project in osb.get_projects(min_curation_level="Low"):

        print "Project: %s has tags: %s" % (project.name, project.tags)
        
and more examples can be found [here](https://github.com/OpenSourceBrain/OSB_API/tree/master/python/examples).


