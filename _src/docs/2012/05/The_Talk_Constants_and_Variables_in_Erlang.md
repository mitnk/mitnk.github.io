<a>mitnk</a>:    Hi, I'm new to Erlang. Can anybody show me how to define a global like variable in Erlang? I wrote like this, http://codepad.org/kSMIyRyc But it got compile Errors.

<a>Erlang</a>:    Python code- 18 lines - codepad (0.02s)

<a>dottedmag</a>:    mitnk: you don't

<a>dottedmag</a>:    mitnk: there are no variables in Erlang, just constants. If you need a constant, just declare arg-less function.

<a>DeadZen</a>:    there are variables in erlang.

<a>dottedmag</a>:    DeadZen: if you count ETS as variables.

<a>DeadZen</a>:    no im counting immutable variables as variables

<a>dottedmag</a>:    They aren't _var_iables, they don't vary, right?

<a>DeadZen</a>:    and there are mutable variables beyond just ets..

<a>DeadZen</a>:    yes they do vary

<a>DeadZen</a>:    they don't mutate.

<a>mitnk</a>:    How to define and constant? I'm going to look at arg-less

<a>dottedmag</a>:    mitnk: my_age/0

<a>DeadZen</a>:    variables have different values. thats why they're called variables.. not because a single variables value varies

<a>DeadZen</a>:    thats why they're called immutable variables not immutable constants

<a>mitnk</a>:    dottedmag: It was in my code.

<a>dottedmag</a>:    mitnk: that's the arg-less function.

<a>dottedmag</a>:    DeadZen: "immutable variables" is oxymoron

<a>DeadZen</a>:    not really... immutable variables and immutable flags are long standing terms

<a>mitnk</a>:    dottedmag: Then what you mean by saying "If you need a constant, just declare arg-less function."

<a>dottedmag</a>:    mitnk: my_age/0 is constant. So you have already declared it.

<a>DeadZen</a>:    but thats not a variable my_age is a function

<a>DeadZen</a>:    i thought the question was global variables

<a>mitnk</a>:    Ok, thx. Yeah, I meant constant rather than global varmy mistake.

<a>DeadZen</a>:    in erlang the question becomes global to what?

<a>DeadZen</a>:    global to that process? that node? that cluster?

<a>dottedmag</a>:    mitnk: There's another way to do it: http://www.erlang.org/doc/reference_manual/macros.html

<a>Erlang</a>:    Erlang -- The Preprocessor (0.86s)

<a>DeadZen</a>:    mitnk: -define(MY_AGE, 18). after -export

<a>dottedmag</a>:    mitnk: see the 8.2

<a>DeadZen</a>:    mitnk: then reference ?MY_AGE in bar()

<a>mitnk</a>:    DeadZen: Well, I am writing a simple Sequential program. Maybe I asked a bad question.

<a>DeadZen</a>:    mitnk: I don't believe in bad questions, even asking the wrong question is useful indication

<a>DeadZen</a>:    mitnk: the subsequent question is always... now what are you trying to do?

<a>mitnk</a>:    DeadZen: "-define(MY_AGE, 18)" seems just what I am looking for

<a>DeadZen</a>:    dottedmag: also i still assert 1 allowed mutation constitutes a variable.

<a>DeadZen</a>:    dottedmag: albeit with limited assignment variability?;p

<a>dottedmag</a>:    There is no mutation or assignment -- just coming to scope with defined value.

<a>DeadZen</a>:    well thats really what erlang is saying.. once a variable is set, its no longer safe to change it

<a>DeadZen</a>:    the value can vary, but not be reassigned

<a>dottedmag</a>:    Different instances of the same, ahem, variable may exist with different values in different scopes, but the every particular example is immutable and does not vary.

<a>dottedmag</a>:    But that's just the terminology.

<a>dottedmag</a>:    So let's agree we describe the same situation using different terms.

<a>DeadZen</a>:    thats interesting you consider it not setting a variable but brining a non variable to scope

<a>DeadZen</a>:    dottedmag: its 6am, i haven't slept, semantic death is imminent

<a>DeadZen</a>:    

<a>dottedmag</a>:    good night

<a>DeadZen</a>:    nah its funny, i had the same thought but arrived at the opposite conclusion

<a>DeadZen</a>:    A=1. simple a variable A set to 1.. B = A. a variable B set to the variable A.. the values could be anything.. ergo. they're variables

<a>mitnk</a>:    DeadZen: Bye, thx!

<a>DeadZen</a>:    mitnk: you're welcome, keep at it

<a>mitnk</a>:    dottedmag: I knew variable in Erlang is different. But in book "Programming Erlang", Joe call them variables

<a>DeadZen</a>:    if it makes you feel better, we can call them predictable variables

<a>mitnk</a>:    Okey

<a>DeadZen</a>:    lol

<a>ttmrichter</a>:    mitnk: They *are* variables.

<a>ttmrichter</a>:    In the *mathematical* sense of the term.

<a>ttmrichter</a>:    If you think about it, the statement "x = x + 1" is ludicrous.

<a>ttmrichter</a>:    It cannot be possible in anything except the most neurotic of number systems (a number system which has one value and is a ring).

<a>ttmrichter</a>:    had a massive shock on first contact with BASIC back in the day when seeing "A = A + 1".

<a>ttmrichter</a>:    It just didn't make any damned sense.

<a>Erlang</a>:    does not compute

<a>mitnk</a>:    Thank you, ttmrichter. That's can be right, but my question (concern) here is not this. Thanks all!

<a>ski_</a>:    mitnk : your pasted code works fine, if you lift the call to my_age/0 out of the condition

<a>ski_</a>:    ponders using a parameterized module for this ..

<a>mitnk</a>:    ski_: Yes, I tried that. But I don't want create an extra variable; -define is just the case

<a>ttmrichter</a>:    ski_: Parameterized modules are evil.

<a>ski_</a>:    ttmrichter : i'm not convinced

<a>ski_</a>:    mitnk : *nod*, then go with that

<a>DeadZen</a>:   draws horns on parameterized modules

<a>DeadZen</a>:   adds a picture of rush limbaugh

<a>DeadZen</a>:   ski_: k... how bout now?

<a>Licenser</a>:   heh

<a>Licenser</a>:   ski_ there is a very good explemation why somewhere on the interwerbs let ne dig it out

<a>Licenser</a>:   http://ferd.ca/you-will-regret-this.html

<a>Erlang</a>:   ferd.ca -> YOU WILL REGRET THIS (0.22s)

<a>Licenser</a>:   that one, realy worth looking at, not only opend it my eyes but ti made me laugh a lot

<a>nox</a>:   when was released -callback attributes?

<a>nox</a>:   were*

<a>ski_</a>:   DeadZen : all lies !

<a>ski_</a>:   (though i suppose horns is a biblical symbol for power ..)

<a>DeadZen</a>:   nox: r15 i think

<a>DeadZen</a>:   ski_: WITCH!

<a>nox</a>:  DeadZen: thanks

Copy right by <a>mitnk</a>, <a>dottedmag</a>, <a>DeadZen</a>, <a>ttmrichter</a>,  <a>ski_</a>, <a>Licenser</a>, and <a>nox</a> @ <a href="irc://irc.freenode.net/erlang">Erlang IRC</a> :P