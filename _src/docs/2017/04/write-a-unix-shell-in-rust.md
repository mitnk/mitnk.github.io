Write a Shell in Rust
=====================

Rust programming language is getting popular for quite a while. My
first try on Rust is when I wanted to rewrite
[lightsocks](https://github.com/mitnk/lightsocks), a tool similar to
[shadowsocks](https://shadowsocks.org). It's not a smooth experience
because 1) `select()` is not yet natively supported and 2) I felt
Rust programming is too much depends on crates.

Then after using [xonsh](http://xon.sh) for a while, I've become
interested in writting a shell. And I decide to write one in Rust.
One for fun, one for learning Rust. (BTW,
[xonsh](https://github.com/xonsh/xonsh) is a must-try if you love
Python)

![A Cicada Shell](/media/img/2017/04/cicada-shell.jpg)

After several weekends and vacations, the
[cicada](https://github.com/mitnk/cicada) shell was born and ready
for real use.

During the journey, I find writting Rust is quite fun. The cost of
"Zero-cost Abstraction" on programmers are a bit annoying, but I'm
getting used to it. The crates are quite lovely. I treat them as
the std libraries in Python. They work very well with `cargo` tool.
The Rust comunity is very good and gave me a lot of helps along the way.

[1] image via https://www.pinterest.com/pin/554435404110738142/
