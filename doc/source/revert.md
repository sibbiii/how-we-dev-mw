(chap_revert)=
# If we cannot fix main fast, we revert!

**_Note: this section is an MVP. Tests pass, but functionality is incomplete :-) I will soon improve it._**


Trust me, it will happen. For stupid reasons, main will be broken, and then?
Once having one repo, and having "everything" in this repo so that your code is not affected by things outside that repo fixing main simplifies to rolling back main.
Finding a solution to the issue that caused the breakage may take several hours, or maybe days, but this is fine, as your colleagues are unblocked now.
Just two small issues are remaining: How to check that main is fixed and how to to check it that fast?