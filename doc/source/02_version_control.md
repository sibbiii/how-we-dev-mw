(chap_version_control)=
# We version control everything in one repo

Poly-repos would make sense if we had multiple teams with clearly separated responsibilities plus well-defined and stable interfaces. 
Then each team could work in their own "mono-repo". This is the common way of working in the open-source world nowadays.

For MotionWise, our codebase is a hugely convoluted monolith. Dependencies between parts of the code are everywhere and not well-known. Feature owners are responsible to integrate their features into all projects. Consequently, we are one large team that nees only one Git repository for MotionWise 2.0 and all customer projects based on it. Working with one repo is easy: Type _scalar checkout path_of_repo_ on the command line to get all you need. Continue to work with standard git commands (git fetch, pull, commit, ...).

In contrast to Camel, a single repo allows for ordered atomic commits with standard of the shelf tooling. Further benefits are the ability to do fast workspace updates (fetch takes only some seconds), background prefetch, mirroring, rollbacks, usage of standard tooling to build a pull request and much more. Plus, we need to train, document, and maintain one home-grown tool less.

For our daily work this means:
1. **We store all build inputs in a single Git repository**. This includes code, tests, configuration, and infrastructure.
2. We serve large binaries via Git-LFS from Artifactory
3. **We consume well separated internal and external dependencies with stable and clearly defined interfaces as packages linked by a hash** from Artifactory. For example: Python, Gtest, or Python PIP packages. Linking external input by version, filename, or id is not allowed, as this allows the build inputs to change, therefore making the build potentially non-deterministic. 
4. We must not consume build inputs from systems such as MongoDB, Polarion or ActiveDirectory for the same reason. If required, a copy (or a link by hash) may be added to Git with an automated pull request.



