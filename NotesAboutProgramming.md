The Elements of Programming Style, by Brian W. Kernighan and P. J. Plauger
===
* **Write clearly -- don't be too clever.**
* Say what you mean, simply and directly.
* Use library functions whenever feasible.
* Avoid too many temporary variables. **[?]**
* Write clearly -- don't sacrifice clarity for efficiency.
* Let the machine do the dirty work.
* **Replace repetitive expressions by calls to common functions.**
* Parenthesize to avoid ambiguity.
* **Choose variable names that won't be confused.**
* Avoid unnecessary branches.
* **If a logical expression is hard to understand, try transforming it.**
* **Choose a data representation that makes the program simple.**
* Write first in easy-to-understand pseudo language; then translate into whatever language you have to use.
* **Modularize. Use procedures and functions.**
* **Avoid gotos completely if you can keep the program readable.**
* **Don't patch bad code -- rewrite it.**
* **Write and test a big program in small pieces.**
* Use recursive procedures for recursively-defined data structures.
* Test input for plausibility and validity.
* Make sure input doesn't violate the limits of the program.
* **Terminate input by end-of-file marker, not by count.**
* Identify bad input; recover if possible.
* **Make input easy to prepare and output self-explanatory.**
* **Use uniform input formats.**
* Make input easy to proofread.
* Use self-identifying input. Allow defaults. Echo both on output.
* Make sure all variables are initialized before use.
* Don't stop at one bug.
* Use debugging compilers.
* Watch out for off-by-one errors.
* Take care to branch the right way on equality.
* Be careful if a loop exits to the same place from the middle and the bottom.
* Make sure your code does "nothing" gracefully.
* Test programs at their boundary values.
* Check some answers by hand.
* 10.0 times 0.1 is hardly ever 1.0.
* 7/8 is zero while 7.0/8.0 is not zero.
* Don't compare floating point numbers solely for equality.
* Make it right before you make it faster. **[!]**
* Make it fail-safe before you make it faster. **[!]**
* Make it clear before you make it faster. **[!]**
* Don't sacrifice clarity for small gains in efficiency. **[!]**
* Let your compiler do the simple optimizations.
* **Don't strain to re-use code; reorganize instead.**
* Make sure special cases are truly special.
* Keep it simple to make it faster. **[!]**
* Don't diddle code to make it faster -- find a better algorithm. **[!]**
* Instrument your programs. Measure before making efficiency changes.
* Make sure comments and code agree.
* Don't just echo the code with comments -- make every comment count.
* **Don't comment bad code -- rewrite it.**
* **Use variable names that mean something.**
* **Use statement labels that mean something.**
* **Format a program to help the reader understand it.**
* Document your data layouts.
* ~~Don't over-comment.~~

The Cathedral and the Bazaar: Musings on Linux and Open Source by an Accidental Revolutionary, by Eric S. Raymond
===
* Every good work of software starts by scratching a developer's personal itch.
* Good programmers know what to write. Great ones know what to rewrite (and reuse).
* Plan to throw one [version] away; you will, anyhow. (Copied from Frederick Brooks' The Mythical Man-Month)
* If you have the right attitude, interesting problems will find you.
* **When you lose interest in a program, your last duty to it is to hand it off to a competent successor.**
* **Treating your users as co-developers is your least-hassle route to rapid code improvement and effective debugging.**
* Release early. Release often. And listen to your customers.
* Given a large enough beta-tester and co-developer base, almost every problem will be characterized quickly and the fix obvious to someone.
* Smart data structures and dumb code works a lot better than the other way around.
* If you treat your beta-testers as if they're your most valuable resource, they will respond by becoming your most valuable resource.
* The next best thing to having good ideas is recognizing good ideas from your users. Sometimes the latter is better.
* Often, the most striking and innovative solutions come from realizing that your concept of the problem was wrong.
* Perfection (in design) is achieved not when there is nothing more to add, but rather when there is nothing more to take away. (Attributed to Antoine de Saint-Exupéry)
* Any tool should be useful in the expected way, but a truly great tool lends itself to uses you never expected.
* When writing gateway software of any kind, take pains to disturb the data stream as little as possible—and never throw away information unless the recipient forces you to!
* When your language is nowhere near Turing-complete, syntactic sugar can be your friend.
* A security system is only as secure as its secret. Beware of pseudo-secrets.
* To solve an interesting problem, start by finding a problem that is interesting to you.
* Provided the development coordinator has a communications medium at least as good as the Internet, and knows how to lead without coercion, many heads are inevitably better than one.
