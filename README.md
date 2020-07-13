# Giant Plugins

A re-usable package which can be used in any project that requires a base set of plugins. 

This will include a small set of plugins that are used in a large number of projects, but will not necessarily cover the full requirements.

## Installation

To install with the package manager, run:

    $ poetry add giant-plugins

You should then add `"giant_contact"` to the `INSTALLED_APPS` in `base.py`.  


## Configuration

This application exposes the following settings:

 ## Preparing for release
 
 In order to prep the package for a new release on TestPyPi and PyPi there is one key thing that you need to do. You need to update the version number in the `pyproject.toml`.
 This is so that the package can be published without running into version number conflicts. The version numbering must also follow the Semantic Version rules which can be found here https://semver.org/.
 
 ## Publishing
 
 Publishing a package with poetry is incredibly easy. Once you have checked that the version number has been updated (not the same as a previous version) then you only need to run two commands.
 
    $ `poetry build` 

will package the project up for you into a way that can be published.
 
    $ `poetry publish`

will publish the package to PyPi. You will need to enter the username and password for the account which can be found in the company password manager