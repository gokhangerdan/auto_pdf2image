# auto_pdf2image
Automatically finds pdf files from given path and save images in same directories.
### Dependencies:
```
pip3 install -r requirements.txt
```
### Usage:
```
python3 convert.py <PATH>
```
Example directory tree:
```
-docs
  |
   --type1
     |
      ---doc1.pdf
      ---doc2.pdf
      ---doc3.pdf
   --type2
     |
      ---doc4.pdf
      ---doc5.pdf
   --type3
     |
      ---doc6.pdf
```
Result directory tree:
```
-docs
  |
   --type1
     |
      ---doc1.pdf
      ---doc1.jpg
      ---doc2.pdf
      ---doc2.jpg
      ---doc3.pdf
      ---doc3.jpg
   --type2
     |
      ---doc4.pdf
      ---doc4.jpg
      ---doc5.pdf
      ---doc5.jpg
   --type3
     |
      ---doc6.pdf
      ---doc6.jpg
```
