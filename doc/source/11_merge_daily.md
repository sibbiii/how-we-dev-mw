(chap_merge_daily)=
# We merge (something) to main at least daily.

**_Note: this section is an MVP. Tests pass, but functionality is incomplete :-) I will soon improve it._**


Remember, development happens asynchronously on branches prior to the merge to main. This introduces
- work in progress not being shared with other team members,
- work in progress not being tested together with the code of others
- and work in progress not being releasable.

If many teams do not merge their work-in-progress for extended periods, we introduce high costs once we try to merge to main and fail due to branches conflicting with each other in code and/or behavior. 

Merging too often is also unreasonable but gets cheaper when fast and automated tests are included within a test build that runs automatically before any merge to main.  

The industry best practice we want to follow here is to build in 10 minutes and merge at least *something* daily. There is always something that you can carve out from your current code, e.g., a function, a unit, or an interface change. 

Some of your competitors do so, and developers who have once worked in such a fast feedback environment and environment never want to go back - that should make us think. 
