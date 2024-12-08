(chap_small_increments)=
# We make changes in small increments.

**_Note: this section is an MVP. Tests pass, but functionality is incomplete :-) I will soon improve it._**


You make a change. 
- You build before merge. 
- Your build fails.

Now, you need to debug lots and lots of lines to find out what causes the issue.

Alternatively, you make a very small change. 
- You build. 
- You repeat.

If your build fails, you know exactly where to search for the bug.

Even better, you make a very small change. 
- You build. 
- You merge to main. 

You repeat.

This allows everybody to participate in your changes, and you to participate in everybody else changes if they also merge frequently. It’s all about fast feedback, more on this later.

Note, in nearly all cases, large changes can be split into several small changes using the parallel change, branch by abstraction, and other patterns. **Detailed explanation to be added here**
