隔了好久没更新部落格了, 各种琐事呀. 这篇关于短链接的这篇文章已经在手机memo里呆了很长一段时间了. 在上班路上修正了一些单词bug, 就这样发布吧

With the bursting of twitter like social networks, which allow only short messages. An service called url-shorten became known to most people.

    http://tinyurl.com/7ut9aho
    http://is.gd/DBoG18

Instead of using a public url-shorten service, some website built their own url-shorten service.

    http://t.co/et0lGlHF

Now how to built a service like that?

It's actually pretty simple. A table with the single url attribute with an extra the auto-incrise id attribute will be satisfied.

<table border="1">
    <tr><th>id</th> <th>original URL</th> </tr>
    <tr> <td>1</td><td>http://xxxx.com/very_very_long.html</td> </tr>
    <tr> <td>2</td><td>http://xxxx.com/very_very_long.html</td> </tr>
    <tr><td>...</td><td>...</td></tr>
    <tr> <td>22</td><td>http://xxxx.com/very_very_long.html</td> </tr>
    <tr><td>...</td><td>...</td></tr>
    <tr> <td>5000</td><td>http://xxxx.com/very_very_long.html</td> </tr>
</table>


Now the shorten part. The key point is the conversion: base-10 to base-62 and base-62 to base-10

<table border="1">
    <tr><th>id</th> <th>Shorten URL</th></tr>
    <tr><td>1</td>     <td>http://local.com/1</td></tr>
    <tr><td>2</td>     <td>http://local.com/2</td></tr>
    <tr><td>10</td>   <td>http://local.com/A</td></tr>
    <tr><td>3000</td> <td>http://local.com/mO</td></tr>
    <tr><td>1334212</td> <td>http://local.com/5b5Y</td></tr>
</table>


When a query with a shorten-string comes, we just convert it to the ocd id to lookup the item in the table and 301 redirect to that url.

The convert algorithm is simple, people already implemented it every where, you don't need to implement it again.

This gist is a pretty good one: <https://gist.github.com/778542>

And even [django provide an base-36 version](https://docs.djangoproject.com/en/dev/ref/utils/#django.utils.http.base36_to_int) only including numbers and lowercase letters.
