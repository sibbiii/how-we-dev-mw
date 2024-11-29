# How we (want to) develop MotionWise

![Welcome](img/home.jpg)

Welcome to the high-level guideline we (want to) follow to develop MotionWise continuously at the head of a single repository.

```{only} epub
This e-book is work in progress. We did not include internal or confidential information on purpose. Feel free to read it also as webpage [here](https://documentation.tttech-auto.com/cx_mw/).  
```
```{only} not epub
This guideline is work in progress. We did not include internal or confidential information on purpose. Feel free to read it in .epub format [here](https://4sdv-my.sharepoint.com/:u:/g/personal/sebastian_caban_tttech-auto_com/ERv-ctp4miFFlFC-qiJlfUIBB22qLsr6ZifdikOGiqrPCA?e=wRUSba). 
```

Trainings will be held at all sites, see [here](https://4sdv.sharepoint.com/sites/TTTechAuto-LearningManagementSystem/SitePages/how_we_develop_motionwise.aspx).

## Table of contents

```{eval-rst}
.. toctree::
   :maxdepth: 1

   Welcome to software engineering<01_welcome.md>
   We version control everything in one repo<02_version_control.md>
   We continuously develop at the head of main.<03_develop_at_head.md>
   We agree as a team to never break main.<04_never_break_main.md>
   If we cannot fix main in 10min: revert!<05_revert.md>
   We build before merge.<06_build_before_merge.md>
   We make changes in small increments.<07_small_increments.md>
   We automate the one build.<08_automate_the_one_build.md>
   We have a vast amount of high-quality tests.<09_tests.md>
   We Test, Code, Test, Code, Test, Code, ...<10_tdd.md>
   We merge to main daily.<11_merge_daily.md>
   We have a "fast" build.<12_fast_build.md>
   We use a build system.<13_build_system.md>
   We decouple the codebase.<14_decouple.md>
   We spend time to educate ourselves.<15_educate.md>
   To win, we invest in architecture.<16_architecture.md>
```

## Who are we

[TTTech Auto](https://www.tttech-auto.com/) is a leading platform product and service provider focusing on system, safety and security for the software-defined vehicle. "[MotionWise](https://www.tttech-auto.com/software-products/motionwise-safety-middleware)" is our next-generation safety middleware solution to provide a safe and deterministic execution environment for mixed-criticality software applications. With our headquarters in Vienna and subsidiaries in Spain, Germany, Serbia, and Croatia, we are always searching for excellent engineering potential. Feel free to apply in case you are looking for one of the most incredible places to work on safety-critical embedded software.

## Disclaimer

The content of this guideline is heavily based on input from the public domain that I have collected over the past years. I hereby declare that, except where not appropriately referenced, nothing in this guideline is my own work. Please excuse me for not remembering all the input and ideas I have collected from various books, conference presentations, YouTube videos, and blogs. All started with [a incredibly inspiring talk from Jakob Ehn](https://www.youtube.com/watch?v=hL1OZfgoZGk&t=105s) on "real developers" commiting to main. Lots of inspiration from [Martin Fowler](https://martinfowler.com/articles/branching-patterns.html), [Dave Farley](https://www.youtube.com/@ContinuousDelivery), and countless others later, we from TTTech want to give back to the community our interpretation of modern embedded-software development. Feel free to [contact me](mailto:sebastian.caban@tttech-auto.com) for new inspiration, concerns, and whatever is on your mind. Feel also free to share this guideline as it is. I hope we can inspire you as others inspired us.
