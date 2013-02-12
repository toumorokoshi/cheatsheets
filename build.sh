# build files
./bin/build
# checkout gh-pages
git checkout gh-pages
# sync it
git pull origin gh-pages
# move build up a directory
mv build/* .
# remove build directory
rm -r build/
# add everything
git add .
# do a commit
git commit -am "build $(date)"
# and push it
git push origin gh-pages
# and come back to original branch
git checkout @{-1}



