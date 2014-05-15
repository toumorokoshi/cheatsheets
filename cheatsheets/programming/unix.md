Unix Tips and Tricks
====================

tips, tricks, and useful command for unix
-----------------------------------------

### sed commands

* $ sed -i s/SEARCH_PATTERN/REPLACE_PATTERN/g FILE_NAME: replace SEARCH_PATTERN with REPLACE_PATTERN is FILE_NAME
* $ git ls-files | xargs cat | wc -l : count number of lines in a git repository.
* $ sed ./ -type f s/X/Y/g {} \; : sed for all files in directory (recursive)
* $ perl -pi -e 's/[[:^ascii:]]//g' filename : ascii-ify a file
* Create a jenkins jobs
* $ curl -X POST -d @tgapp.testapi.jenkins.xml http://devcompile.zillow.local/createItem?name=egg.tgapp.testapi &> out.html -H "Content-Type:text/xml"
