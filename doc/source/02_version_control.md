# We version control everything in one repo

Poly-repos make sense if we had multiple teams with
clearly separated responsibilities plus well-defined and stable interfaces. 
Then each team could work in their own “mono-repo”.
This is the common way of working in the open source world nowadays.

As a matter of fact, we are one team, with one hugely convoluted codebase,
no well-defined interfaces, unstable interfaces, and shared responsibilities. 
Consequently, we only need one Git repo repo for Motionwise 2.0
and all customer projects based on it.

- **Store all build inputs in a single Git repository**.
  This includes code, tests, configuration, infrastructure, …
- Serve large binaries via Git-LFS from Artifactory
- **Consume well separated internal and external dependencies 
  with stable and clearly defined interfaces as packages 
  linked by a hash** off the full content from Artifactory. 
  For example: Python, Gtest, or PIP packages.
  Linking external input by version, filename, or id is not allowed, 
  as this allows the build inputs to change, 
  therefore making the build non-reproducible.
- Consuming build input from systems such as MongoDB, 
  Polarion or ActiveDirectory is forbidden for the same reason.

Note: in contrast to Camel, a single repo allows for ordered atomic commits 
with standard of the shelf tooling. Further benefits are
the ability to do fast workspace updates (fetch takes only some seconds),
background prefetch, mirroring, rollbacks,
usage of standard tooling to build a pull request and much more.
Plus, we need to train, document, and maintain one home-grown tool less.

Working with one repo is easy: Use ```scalar checkout path_of_repo```
to get all you need. Continue to work with standard git commands (git fetch, pull, ...).
Notably, we can arrange a training for you and your colleges on this topic, see here.
