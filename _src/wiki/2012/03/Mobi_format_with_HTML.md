Amazon .mobi and .azw File Format v.s. .epub File Format – What’s the Difference? – Part 1
http://www.helenhanson.com/?p=892

Mobipocket Custom Tags

    <mbp:pagebreak/>
    Description:

        forces a page break

    Attributes:

        Attribute 	Value 	Description
        crossable 	yes,no 	If set to "no", the flow content is not crossable using next and previous page navigation.   (requires version 4.8)



    <mbp:nu>
    Description:

        forces non underline font



    <mbp:section>
    Description:

        defines a book section

    Attributes:

        Attribute 	Value 	Description
        crossable 	yes, no 	if set to yes, the page next/previous are only allowed with this section.
        bgcolor 	hexa color code 	set the background color for the entire section



    <mbp:frameset>
    Description:

        defines a new frameset, which can contain slave frame tags.

    Attributes:

        Attribute 	Value 	Description
        crossable 	yes,no 	If set to "no", the main flow content inside this frameset is not crossable using next and previous page navigation.
        name 		used to identify the frameset when a javascript function has to be executed inside a particular frameset.   (requires version 4.8)
                



    <mbp:slave-frame>
    Description:

        defines a new slave frame.

    Attributes:

        Attribute 	Value 	Description
        display 	top, bottom, left, right 	indicates the positionning of the slave frame relative to the current frameset
        breadth 	a positiver integer, in em or px units , auto 	indicates the height (in case display="top" or "bottom") or width (display="left" or "right") of the slave frame. The "auto" value is valid only for display="top" or "bottom"
        device 	pc, pda, all 	pda : frame displays only in the Mobipocket Reader on PDA devices pc : frame displays only in the Mobipocket Reader for PC all : frame displays both on PC and PDA devices
        src 	a Url to an .htm file 	a url to the slave frame html file, in the case the mbp:slave-frame has to be auto-close
        topmargin 	a positiver integer, in em or px units 	the top margin (only in case where src is not set and the slave content is embedded inside the mbp:slave-frame tag
        bottommargin 	a positiver integer, in em or px units 	same
        leftmargin 	a positiver integer, in em or px units 	same
        rightmargin 	a positiver integer, in em or px units 	same



    <idx:entry>
    Description:

        defines a new entry entry

    Attributes:

        Attribute 	Value 	Description
        name 	String 	Name of the index
        id 	String 	identifies this entry when related to an external sub-entry (idx:ext-subentry).   (requires version 4.8)



    <idx:orth>
    Description:

        Marks the text that will appear in the index search box for that entry. Note: the label of the entry is limited to 127 characters in the index search view. If longer than 127 characters, the full text will be visible in the flow of the book but only the first 127 characters will be used in the index search.

    Attributes:

        Attribute 	Value 	Description
        value 	String 	include text for the label in the entry that you do not want to display in the OEB flow
        style 	bold, italic, underline inactive, numbered 	Values can be combined in a comma-separated list. This attribute specifies how a keyword will be displayed in the index search mode of the reader. numbered: if several entries have the same keyword, numbers will be displayed along those entries to distinguish them in the index search mode of the reader. The style "numbered" requires version 4.8 of the reader.
        indent 	1 	If set, the entry will be displayed indented in the index search. Also, the part of text of the entry that is the same as the text of the first non-indented preceding (in alphabetical order) entry will not be displayed.
                
        format 	String 	Marks the format to apply to the text that will appear in index search box for this entry. To have more information about the format string see "Creating complex content > Indexes and Dictionaries > What is the format string?"   (requires version 5)



    <idx:key>
    Description:

        Enables to search for an entry in the index by an alternative key. You can specify one or more alternative keys. Use the type attribute to distinguish between key searches

    Attributes:

        Attribute 	Value 	Description
        name 	String 	define the type of the alternative key
        key 	String 	Use the key attribute to include text for the alternative key that you do not want to display in the OEB flow
        scriptable 	yes 	If set to yes, this key will be accessible from the main index   (requires version 5)



    <idx:short>
    Description:

        used in dictionaries to mark the scope of the text that will be displayed in the popup window when selecting the word entry within any ebook



    <idx:gramgrp/>
    Description:

        used in dictionaries to indicate the list of inflections attached to a grammatical group. 

    Attributes:

        Attribute 	Value 	Description
        value 	String 	marks the grammatical group that will appear in the inflection disambiguation tooltip   (requires version 4.8)
        infl 	String 	list of the inflected forms attached to the grammatical group defined in "value".



    <idx:subentry>   requires version 4.8
    Description:

        defines a new subentry. The subentry is part of the entry. The data in the subentry can be easily accessed by clicking on some links present in the frameset. 

    Attributes:

        Attribute 	Value 	Description
        name 	String 	name of the subentry



    <idx:string>   requires version 4.8
    Description:

        defines a column that contains String data in the entry table 

    Attributes:

        Attribute 	Value 	Description
        name 	String 	name of the column
        value 	String 	value of the current entry in the column "name"



    <idx:ext-subentry>   requires version 4.8
    Description:

        Defines a new external subentry. The external subentry is not part of the entry, but it is used in the same way as a subentry. The only difference is that the data in the external subentry can be displayed in a frameset different from the main entry's one. 

    Attributes:

        Attribute 	Value 	Description
        name 	String 	name of the subentry
        id 	String 	the id of the main entry to which this external subentry is related



    <loghost/>
    Description:

        used to set the url where to upload logging information

    Attributes:

        Attribute 	Value 	Description
        url 	URL 	
        prefix 		
        encoding 		



http://www.mobipocket.com/dev/article.asp?BaseFolder=prcgen&File=tagref_mobi.xml