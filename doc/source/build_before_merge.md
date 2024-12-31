(chap_build_before_merge)=
# If we cannot fix main in 10min: revert!

**_Note: this section is an MVP. Tests pass, but functionality is incomplete :-) I will soon improve it._**


The purpose of a build is to transform software into binaries. This includes not only compilation and linking, but also running generators, static code analysis, unit testing, component testing, integration testing, flashing and testing in hardware, and so on.
In short, **a build includes all steps to generate and ship a release package plus ensuring that the release package is of sufficient quality** to be released.

Now the idea:
- if we write code + tests (same programmer, same repo)
- if we build prior merging to main,
- if our build passes only if our codebase is of releasable quality,
- if we merge to main only if the build passes,

then

- Main will always be of sufficient quality to be released
- Main will always be of sufficient quality for our colleagues to checkout
- Main will include more and more tests over time that make testing much better in the future.

By doing so, you will spend most of your day writing and "building" code; thus, any investment in “better” builds (faster, reproducible, easy-to-understand results, easy usage, …) will pay off many times over.

We want one automated build with only two possible outcomes: pass or fail.
In case we repeat the build, the outcome must be identical.
In case somebody else triggers the build on her/his machine from the same source commit,  the output must be identical.
In other words, there must be no difference regarding who starts the build or whether the build is started locally or by a CI system (other than that, the CI system takes some extra steps to store results, etc.).
