# -*- coding: utf-8 -*-
"""
Date: 2023/11/21
Author: @1chooo(Hugo ChunHo Lin)
E-mail: hugo970217@gmail.com
Course: AP4063
Midterm: Question 2
Version: v0.1.0
"""

def decode(message):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    reversed_alphabet = alphabet[::-1]  # Reversed alphabet
    
    decoded_message = ''
    
    for char in message:
        if char == ' ':
            decoded_message += ' '  # Preserve spaces
        else:
            index = reversed_alphabet.index(char)
            decoded_message += alphabet[index]
    
    return decoded_message

decode("sr")    #"hi"

decode("svool") #"hello"

decode("r slkv mlylwb wvxlwvh gsrh nvhhztv")    #"i hope nobody decodes this message"

decode("qzezxirkg rh z srts ovevo wbmznrx fmgbkvw zmw rmgvikivgvw kiltiznnrmt ozmtfztv rg szh yvvm hgzmwziwravw rm gsv vxnzxirkg ozmtfztv hkvxrurxzgrlm zolmthrwv sgno zmw xhh rg rh lmv lu gsv gsivv vhhvmgrzo gvxsmloltrvh lu dliow drwv dvy xlmgvmg kilwfxgrlm gsv nzqlirgb lu dvyhrgvh vnkolb rg zmw rg rh hfkkligvw yb zoo nlwvim dvy yildhvih drgslfg koftrmh")   #"javacript is a high level dynamic untyped and interpreted programming language it has been standardized in the ecmacript language specification alongside html and css it is one of the three essential technologies of world wide web content production the majority of websites employ it and it is supported by all modern web browsers without plugins"

decode("gsv vrtsgs hbnkslmb dzh qvzm hryvorfh urmzo nzqli xlnklhrgrlmzo kilqvxg lxxfkbrmt srn rmgvinrggvmgob")  #"the eighth symphony was jean sibelius final major compositional project occupying him intermittently"

decode("husbands ask repeated resolved but laughter debating")  #"sfhyzmwh zhp ivkvzgvw ivhloevw yfg ozftsgvi wvyzgrmt"

decode("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")   #"zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"

decode(" ") #" "

decode("")  #""

decode("thelastrandomsentence") #"gsvozhgizmwlnhvmgvmxv"