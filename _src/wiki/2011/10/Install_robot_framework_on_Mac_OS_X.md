Download robot framework source package from here:
http://code.google.com/p/robotframework/downloads/list
like robotframework-2.6.1.tar.gz

Un-tar it and install it with
sudo python setup.py install

Link pybot into bin directory
sudo ln -s /System/Library/Frameworks/Python.framework/Versions/2.6/bin/pybot /usr/local/bin/pybot

You can try command now:
pybot --version

Look up key works from here:
http://robotframework-seleniumlibrary.googlecode.com/hg/doc/SeleniumLibrary.html?r=2.8

Download robotframework-seleniumlibrary from here:
http://code.google.com/p/robotframework-seleniumlibrary/downloads/list
like 	robotframework-seleniumlibrary-2.8.tar.gz

Un-tar it and install it with
sudo python setup.py install

Write Cases

==============

*** Settings ***
Library    Selenium Library    30
Test setup    Start Selenium Server
Test teardown    Stop Selenium Server

*** Testcases ***
TestCseSearchBoxDefaultValue    [Documentation]    Search box default value
  Open Browser    http://mitnk.com/commands/    firefox
  Textfield Value Should Be    cse-input    Search
  Close Browser

TestCseSearchBoxBlur    [Documentation]    Search box blur event
  Open Browser    http://mitnk.com/commands/    firefox
  Input Text    cse-input    abc
  Simulate    cse-input    blur
  Textfield Value Should Be    cse-input    abc
  Input Text    cse-input    \
  Simulate    cse-input    blur
  Textfield Value Should Be    cse-input    Search
  Close Browser

TestCseSearchBoxFocus    [Documentation]    Search box focus event
  Open Browser    http://mitnk.com/commands/    firefox
  Textfield Value Should Be    cse-input    Search
  Simulate    cse-input    focus
  Textfield Value Should Be    cse-input    \
  Input Text    cse-input    abc
  Simulate    cse-input    blur
  Simulate    cse-input    focus
  Textfield Value Should Be    cse-input    abc
  Close Browser
