
# Math-Practice

The vision for this app is that educators and students are going to be able to create problems that generate themselves automatically.

In essence, it works similar to a site like IXL and KhanAcademy, except with a few changes. 

Firstly, users are able to add their own problems. Some coding experience is required at the moment, but it may not be far fetched that a block-based method might be possible. In addition, no coding experience that is too hard should be requied.

## Structure

There is a heirarchy of problems invovled.

```
* Courses 
    - Topics
        > Problems
``` 

To make these easier for students to navigate, topics are divided into units, in the format `X.Y`

Topics are given a UID, to differentiate them since there may be common courses with the same name (algebra II, calc BC, stats)

The data structure is likely not a dictionary structure, and isn't at the moment, but that is may change. 

For example, a math course might have the following structure

```
* AP Calculus AB
    - Basic limits (1.1)
        > Determining Limits from Graphs
        > Determining Limits from Tables
    - Discontinuities (1.2)
        > Identifying Discontinuities
        > Discontinuties through Equations
    
    - Power Rule (2.1)
        > Power Rule
    - Quotient Rule (2.2)
        > Quotient Rule
    - Chain Rule (2.3)
        > Chain Rule
        > Chain Rule with Trig Functions
```

Users are able to choose between which topics they would like to practice, but within topics, the problems are randomized. 

(As an aside, if you are a math student, pleasse don't use the above syllabus rashly... its just an example)

Users are stored seperately. Each user gets a list of the courses that they own (by UID). 

Learning is a bit more complicated. For each course a user "joins", all topics are added into the user data.

Each topic is given a few user-specific variables: datetime of the last session, number of problems done in the last session, accuracy within the last session.

If the accuracy within the last session is below some cutoff after some number of problems (cutoff, cutoff_problems), then the user is encouraged to repeat the problems after an interval.

## Problems

Problems are broken into three parts
  * Question
  * Answer (the value of the answer)
  * Solution (how to find the answer)
  * +some metadata

There should be an output `data` object from the problem code that returns:
```
{
    "question": str,
    "answer": str, int or array,
    "solution": str    
}
```

