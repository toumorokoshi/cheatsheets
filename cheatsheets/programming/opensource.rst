Revisions
---------
Revisions should aggregate a list of debug and bugfixes from each commit. You can build a changelog directory directly with this:

    git log HEAD...0.3.9 --pretty="%s
    %b"


Committing
----------
Commits should list the bugfixes and feature changes as a list, like so:

.. code:: bash

    * feature: added my feature 1
    * bugfix: squashed this bug
    * bugfix: squashed this other bug
