How do I convert between Unix and Windows text files?

The format of Windows and Unix text files differs slightly. In Windows, lines end with both the line feed and carriage return ASCII characters, but Unix uses only a line feed. As a consequence, some Windows applications will not show the line breaks in Unix-format files. Likewise, Unix programs may display the carriage returns in Windows text files with Ctrl-m ( ^M ) characters at the end of each line.

There are many ways to solve this problem. This document provides instructions for using FTP, screen capture, unix2dos and dos2unix, tr, awk, Perl, and vi to do the conversion. To use these utilities, the files you are converting must be on a Unix computer.

Note: In the instructions below, replace unixfile.txt with the name of your Unix file, and replace winfile.txt with the Windows filename..

FTP
When using an FTP program to move a text file between Unix and Windows, be sure the file is transferred in ASCII format, so the document is transformed into a text format appropriate for the host. Some FTP programs, especially graphical applications (e.g., Hummingbird FTP), do this automatically. If you are using command line FTP, before you begin the transfer, enter:

  ascii
Note: You need to use a client that supports secure FTP to transfer files to and from Indiana University's central systems. For more, see At IU, what SSH/SFTP clients are supported and where can I get them?

dos2unix and unix2dos
The utilities dos2unix and unix2dos are available for converting files from the Unix command line.

To convert a Windows file to a Unix file, enter:

  dos2unix winfile.txt unixfile.txt
To convert a Unix file to Windows, enter:

  unix2dos unixfile.txt winfile.txt
tr
You can use tr to remove all carriage returns and Ctrl-z ( ^Z ) characters from a Windows file:

  tr -d '\15\32' < winfile.txt > unixfile.txt
However, you cannot use tr to convert a document from Unix format to Windows.

awk
To use awk to convert a Windows file to Unix, enter:

  awk '{ sub("\r$", ""); print }' winfile.txt > unixfile.txt
To convert a Unix file to Windows, enter:

  awk 'sub("$", "\r")' unixfile.txt > winfile.txt
Older versions of awk do not include the sub function. In such cases, use the same command, but replace awk with gawk or nawk.

Perl
To convert a Windows text file to a Unix text file using Perl, enter:

  perl -p -e 's/\r$//' < winfile.txt > unixfile.txt
To convert from a Unix text file to a Windows text file, enter:

  perl -p -e 's/\n/\r\n/' < unixfile.txt > winfile.txt
You must use single quotation marks in either command line. This prevents your shell from trying to evaluate anything inside.

vi
In vi, you can remove carriage return ( ^M ) characters with the following command:

  :1,$s/^M//g

Note: To input the ^M character, press Ctrl-v , and then press Enter or return.

In vim, use :set ff=unix to convert to Unix; use :set ff=dos to convert to Windows.