# Meet SCPI
Parsing Homework Assignment for ENGN1931Z

The first class of physical devices that we will interface with in this course will be scientific instrumentation, for example, of the kind that you may have encountered in other engineering labs. These include instruments branded Agilent, HP, Fluke, Keithley, Keysight, Tektronix, etc.

Thankfully, many of these instruments share a common programmatic protocol called SCPI - Standard Commands for Programmable Instruments (pronounced "skippy"). SCPI is a protocol that includes both a list of common commands as well as a set of general rules for creating new commands. The current SCPI - 1999 protocol is defined in a 4 volume, 819 page specification that you can find at [this link from the Interchangeable Virtual Instruments Foundation](http://www.ivifoundation.org/docs/scpi-99.pdf).

In this assignment, we will follow the advice from the helpful engineers at Keysight (formerly Agilent) in their ["Making it easier to learn SCPI" guide](https://www.keysight.com/main/redirector.jspx?action=ref&lc=eng&cc=US&nfr=&ckey=1707043&cname=EDITORIAL). Specifically, in this assignment, you will apply your knowledge of Python and Regular Expressions to programmatically find all the state query commands for the Agilent/Keysight E3631A Power Supply. You will then pass these queries as a properly formatted string to a virtual instrument (online via HTTP Get commands) in order to discover the current state of this instrument.

Your Python code should:

1. Use the pdfminer library to extract the text from the [PDF manual for the E3631A](http://literature.cdn.keysight.com/litweb/pdf/E3631-90002.pdf). It may take ~15 mins to run on a Raspberry Pi.

2. Use the re library to find all unique long-form state queries (ignoring any optional command elements/nodes as described [here](http://www.keysight.com/upload/cmc_upload/All/FollowtheSCPILearningProcessandUsingtheTool.pdf?&cc=US&lc=eng)).

3. Pass these queries as an appropriately formatted string (with terminators) to a web-based virtual instrument using the requests library.

Before you start this assignment, please remember to install pdfminer. **The easiest way to install PDFMiner.six on Pi using the pip3 package management system: `pip3 install pdfminer.six` / on computer with Anaconda `conda install -c conda-forge pdfminer.six`

`hw_parsing.py` is a template code for the assignment. **Please review the comments at the top of that file.**
`pdfminerToText.py` contains a helpful convert() function for extracting text using the pdfminer library adapted from [Tim Arnold's artcile on "Manipulating PDFs with Python"](https://www.binpress.com/tutorial/manipulating-pdfs-with-python/167). 
`submit.py` is the script that will submit your code to the autograder.

Please note you are welcome to try this assignment as many times as you would like. (There is no penalty for failed attempts, because I wanted to encourage you to practice, test, and debug.) **However, please make sure to obey the class collaboration policy --- do not share your code with others; please write and debug on your own!**
