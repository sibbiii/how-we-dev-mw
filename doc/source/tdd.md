(chap_tdd)=
# We Test, Code, Test, Code, Test, Code, ...

**_Note: this section is an MVP. Tests pass, but functionality is incomplete :-) I will soon improve it._**


Write self-testing code (= code + tests). Thereby it does not matter if you write test first or code first, doesn’t it?

Anyway, the important thing is the no longer than 3 minute feedback cycle between writing tests and code. 
Sure, working like this requires the habits of all of us to be changed, but its worth it. 
Just imagine you update some external dependency (e.g. pymongo, requests) from one version to a new major or minor one. 
How do you know your code will still behave as required. 
With hundreds of dependencies, and lots of CVEs, and several updates a week, manual testing is not a saleable option here.

Testing is not about finding bugs, it is about thinking.

*To be continued ...*
