**Update (2011-11-18):**
Ubuntu机器上也出现了一个与此类似的问题，解决方案是执行下面命令后再重装PIL库

    sudo apt-get install libjpeg-dev libpng-dev zlib1g-dev liblcms1-dev python-dev

**Update (2012-12-22):**

There is no `/usr/share/libtool/config.sub` and `/usr/share/libtool/config.guess` in my Mac OS 10.8  
But we can get them from <http://www.gnu.org/software/libtool/news.html>.

And if PIL still doesn't work. install `brew install libjpeg` and `brew link jpeg`.

Change PIL setup.py like `/usr/local/Cellar/jpeg/8d`, then built PIL with `python setup.py build_ext -i`


Old Article
---------

做项目的时候遇到在Admin Sites下面上传jpg图片报错的问题：
Upload a valid image. The file you uploaded was either not an image or a corrupted.

Google了下，发现<a href="http://djangodays.com/2008/09/03/django-imagefield-validation-error-caused-by-incorrect-pil-installation-on-mac/">这是Mac下PIL没有被正确安装的原因</a>

解决方案是先装Apple XCodeTools
再装jpg图片的一个库：<a href="http://sourceforge.net/projects/libjpeg/files/">libjpeg</a>

    cp /usr/share/libtool/config.sub .
    cp /usr/share/libtool/config.guess .
    ./configure –enable-shared
    make
    sudo mkdir -p /usr/local/include
    sudo mkdir -p /usr/local/bin
    sudo mkdir -p /usr/local/lib
    sudo mkdir -p /usr/local/man/man1
    sudo make install

然后重装PIL就ok了

    # in setup.py
    JPEG_ROOT = "/usr/local/include"
    ZLIB_ROOT = "/usr/local/include"
    # rebuild and install
    python setup.py build_ext -i
    # 这一步测试通过才行！
    python selftest.py
    sudo python setup.py install


详细信息请参照Django Days的文章：<a href="http://djangodays.com/2008/09/03/django-imagefield-validation-error-caused-by-incorrect-pil-installation-on-mac/">Django ImageField validation error caused by incorrect PIL installation on MAC</a>