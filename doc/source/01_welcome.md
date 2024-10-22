# Welcome to software engineering

Writing new code is easy. 
We all learned that already at the university, 
at our previous job, or by ourselves. 
We all feel confident writing new code.
We press run, and no surprise, the new code works on our machine. 
Therefore, we think we need to follow no procedures when coding.

The next step is “a bit” harder. 
We need to integrate our new code.
Integrating means merging our new code with
the new code our 300+ colleagues write simultaneously
into the millions of lines of working code already in our codebase. 
Usually, we work on huge features.
Therefore, integration occurs in most cases just before the release when we are already in a hurry.
Still, we can do it. 
We work extra-long shifts. 
We find shortcuts such as skipping testing or writing documentation.
To speed up quality checks, we trick the system. 
Short-term thinking cannot be good for our company in the long term, can it?
We feel incredibly uncomfortable, but managers told us we need to deliver. 
Lately, this happens so often that while waiting for our endless builds, 
we browse other companies’ job offers. 
Fortunately, there are so many cool things about our company that we power through.

So far, so good, but wait!
The next day, we receive a call that the piece of code we had carefully designed 
broke something else at some place far away in the codebase.
Really? How could we anticipate that code conflict in a codebase of 30+ million lines?
We have just heard of this part of the codebase for the first time. 

We surrender to our fate. 
We start the debugger: bug-fixing time!
If only we could reproduce the bug locally…

## ``Your life does not need to be painful!''

We are not the first ones to fail. 
Programmers before us have made the same mistakes again and again. 
We who love to code underestimate the unforgiving power 
of exponentially growing complexity.
If not managed well, this complexity can quickly outgrow 
the brain capacity of the smartest among us, given scale and time.
No need to be embarrassed; we are all human.

There is a profound difference between coding and software engineering.
As Titus Winters, former C++ libraries lead of Google, once said:
“Software engineering is programming integrated over time and scale.” 

Sure, we all want to master time and scale, but how? 
There no one-fits-all recipe to software engineering. 
The best-practice target-picture for open-source projects with sporadic contributors 
(the kind of environment you might be most familiar with) is different to the
target picture of large enterprise setups with hundreds of full-time employees. 
The often-cited target picture of companies such as Netflix 
that need to scale their independent microservices into gigantic dimensions 
is different to companies working on embedded hardware. 
We do not need to be like Netflix with their microservices or Google with their
gigantic monorepo and custom tooling. 

For MotionWise, we are 300+ full-time developers. 
We trust each other.
Our 30+ million lines codebase is monolithic and full of legacy.
That being said, there is a well-established industry best practice 
for this setup that has proven to scale and stand the test of time:
**Continuous development at the head of a single repository**.

_to be continued ..._