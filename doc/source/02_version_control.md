(chap_version_control)=
# We version control everything in one repo

The first thing we need as a software company is a place to store code, documentation, tools, infrastructure-configuration, and other artifacts, for example, test inputs. In an ideal world, we would put all this data in one version control system that stores a single unambitious snapshot of all our data. 

![a snapshot of the entire codebase](img/2/snapshot.png)

Such a snapshot could then be identified by a hash, making modifications to its content impossible. Changes to the codebase will create new hashes for new snapshots, leading to an unambitious state of the entire codebase at any given point in time. How to update the codebase will be discussed in [the next chapter](develop_at_head). For now, let us focus on working with one snapshot. 

Remember the bug from the introduction that we needed to fix. Our life would be much easier if we could get a snapshot of the whole codebase with the bug in it on our local machine. Ideally, this should be the same snapshot the tester used when she discovered the bug. 

First, let me tell you the good news: We use "Git" in our company. Git is not only the de-facto standard source-code version control tool nowadays. Git also allows us to check out an unambitious source-code snapshot from a repository given only a hash. We can trust Git to do so correctly as this is one of its core design principles to prevent malicious modification of open-source code. 

Now, things get tricky. Our code is not stored in one Git repository. We store our code in 100+ repositories for two main reasons. Firstly, we wanted small independent components with clear ownership and separated permissions. We thought to achieve that by having small teams that own their repository end-to-end and release new versions frequently. Secondly, we thought that small repositories are easier to clone, pull, merge, and push. The reality, unfortunately, turned out to be different. Our codebase kept being a hugely convoluted monolith. Dependencies between repositories kept growing everywhere and were by no means well-known. Team silos became bigger and worked against building teams with knowledge across the product. Eventually, we soon used some half-baked in-house tooling to put our 100+ repositories back together into a single workspace with each repository being in a subfolder. This made sharing, standardizing, and modifying code across repositories possible again, but because of tooling issues, by no means enjoyable.

Poly-repos would make sense if we had numerous _independent_ teams with clearly separated responsibilities plus well-defined and stable interfaces. Then, each team could work in isolation in their own "mono-repo". This way of working is common in the open-source world nowadays for good reasons. 

Large enterprises nowadays mostly go the exact opposite approach for all their internal code: _One_ repository per product. In our case, **one Git repository for MotionWise 2.0 and all customer projects based on it**. This obviously by itself does not make the code better, but having all code together eases the large scale refactorings needed to structure and modularize code. 

You may remember that in the past, Git did not work well with large repositories. All that changed since Microsoft updated Git in late 2022. Microsoft invested significant work to make working in a large Git repository an enjoyable experience. After (partially) cloning a large repository, you never need to clone again. Modern Git fetches all new updates to this repository in the background, making long waiting times for _git fetch_ a relic of the past even when the internet connection is slow. Now that all your code is in one repo, you get atomic snapshots of your whole codebase ordered in time. This means you can go backward and forward from any point in time instantly. Using modern Git, there is no single benefit anymore to storing a monolith in multiple Git repositories instead of subfolders of a single Git repository.

Coming back to the bug that we needed to fix. Now that we have all our code in one Git repository, does checking out the correct snapshot give us an environment where we can reproduce the bug? Unfortunately not, as there is more in our environment than just code:

For our daily work, this means:

1. **We store all build inputs in a single Git repository**. This includes code, tests, configuration, and infrastructure.
2. In case we need large binaries in our workspace or for our build, we serve them via Git-LFS, the build-system, or other standard means from Artifactory. Importantly, linking must be done by hash. 
3. **We consume well-separated internal and external dependencies with stable and clearly defined interfaces as packages linked by hash** from Artifactory. For example: Python, Gtest, Python PIP packages, or Conan Packages. Linking external input by version, filename, or unique id, or "latest" is not allowed, as this allows the build inputs to change, making the build potentially non-deterministic. 
4. We must not consume build inputs from systems such as MongoDB, Polarion, or ActiveDirectory for the same reason. If required, a copy (or a link by hash to Artifactory) may be added to Git via pull request.
5. **We use the standardized WSL** provided by our company to make the complete development environment reproducible.

All points above ensure data integrity by creating a Merkle tree starting from a single Git repository. This means that even if we cannot store everything in one repository because of tool breaks, we version control everything we need to recreate a snapshot of our environment in one repository.

Now that we have unambiguous snapshots, we can move on to the next step, that is modifying them.



