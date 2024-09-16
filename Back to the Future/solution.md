Solution for Back to the Future

Here the image.png given doesn't open .

Check the file type using file <filename> command

file image.png
image.png: PNG image data, 1684 x 922, 8-bit/color RGBA, non-interlaced


It is of png type.
There is something wrong. Check the hex codes of this image in hexeditor

As from the specification of PNG file format, the first 8 bytes of any png file in hexadecimal are: “\x89\x50\x4e\x47\xd\xa\x1a\xa”. Comparing that to the 8 highlighted bytes of the file we see that the first 4 bytes are different. So we try to modify those bytes with an hexadecimal editor -https://hexed.it/ 

Save it as newimage.png and open the image , flag is visible

Flag found -> technovate{movie_back_to_future_2047}