# Exif Tool Notes

1. A simple `exiftool *.docx | grep -c10 Frost` found `2021-12-22.docx`  
2. That was incorrect.  I looked at the first document to see how many lines there were between the `Last Modified` and the name of the document.  There were `24`  
3. The next command I ran was `exiftool *.docx | grep -B42 Frost` and came up with `2021-12-21.docx`  
