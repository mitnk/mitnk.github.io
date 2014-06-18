强大的CKEditor在[这里](http://ckeditor.com/).

近期项目里的CKEitor出问题了，花时间研究了下，结果把以前我反对使用WYSWYG的编辑器的想法给推翻了。之前不想用是因为不会用

项目的需求是这样的：
将一些静态页面的主要内容的HTML代码保存在数据库里，前台用时从这里将对应条目取出来render到页面上。这样客户就可以随时通过django后台使用CKEitor对其内容进行修改。

后来出现问题，客户对一个页面做修改之后，这个页面的样式就彻底乱掉了。我认为肯定是CKEitor给加了额外的代码引起的。后来证明并不是如此。问题的原因是代码在被CKEditor碰之前就有问题。

CKEditor只做两件事：

1. 对有问题的代码尝试修改
2. 格式化格式乱的代码

比如会把以下代码

    a

    b

修改为

    :::html
    <p>
        a b</p>

会把以下代码

    :::html
    <ul><li>ab</li><li>
    cd</li> 
    <li>ef</li></ul>

修改成这样：

    :::html
    <ul>
        <li>
            ab</li>
        <li>
            cd</li>
        <li>
            ef</li>
    </ul>

有两点不好

1. 代码里用的是tab字符，应该用空格才好
2. 像p li这样的元素在开标签后面不应该回车才好

今天才知道这些CKEitor都是可以调整的
使用CKEditor时加入以下代码就可以了

    :::javascript
    <script type="text/javascript">
    CKEDITOR.on( 'instanceReady', function( ev ) {
      ev.editor.dataProcessor.writer.setRules( 'p',
         {
            indent : false,
            breakBeforeOpen : true,
            breakAfterOpen : false,
            breakBeforeClose : false,
            breakAfterClose : false
         });
      ev.editor.dataProcessor.writer.setRules( 'li',
         {
            indent : false,
            breakBeforeOpen : true,
            breakAfterOpen : false,
            breakBeforeClose : false,
            breakAfterClose : false
         });
      ev.editor.dataProcessor.writer.indentationChars = '  ';
      ev.editor.dataProcessor.writer.lineBreakChars = '\n';
    });
    </script>

现在CKEditor会将以下代码

    :::html
    a

    b

    <p>ppp</p><p>pppppd</p>
    <ul><li>
        abc</li>
      <li>
        def</li><li>
        g</li></ul>

    <li>abcde</li>

修改为这样：

    :::html
    <p>a b</p>
    <p>ppp</p>
    <p>pppppd</p>
    <ul>
      <li>abc</li>
      <li>def</li>
      <li>g</li>
    </ul>
    <ul>
      <li>abcde</li>
    </ul>

是不是顺眼多了？嘿嘿

用CKEditor做了个简单的页面，当作[HTML代码的格式化工具](/webapps/ckeditor/)用
大家可以到这个页面试试CKEditor的格式化功能

1. 先点Source按钮
2. 粘贴点乱的HTML代码进去
3. 然后连点Source按钮两次，就可以看效果了

