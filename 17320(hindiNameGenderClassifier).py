# Taking input from user

name = input("Enter the hindi name: \n")

# Checking for last vowels

n = len(name)

if name[n-1] in ('a', 'e', 'i', 'o', 'u'):
    print(name," is a woman")
else:
    print(name," might be a man, onto the next step:")
# Moving on to next classifier, sonorants
# last 3 chars of the name

    nameSONO = name[::-1]

    array1 = []
    for i in range(0,3):
        array1.append(nameSONO[i])
# reversing the sonorant string
# converting the list into a string
    sono = ''.join(array1)
    sonorant = sono[::-1]
    print("The sonorant is ", sonorant)

# comparing the sonorant

    if sono in ("mha", "nha", "lha", "vha", "rha"):
        print(name," is a woman")
    else: 
        print(name," might be a man, onto the next step:")
# checking open syllables
        if sonorant in ("be", "go", "hi","aja","avi", "kha", "eha","ali","eet"):
# The above list can be increased depending upon the corpus of hindi words
            print(name," is a woman")
        else:
            print(name," is most probably a man")

''' The decision parameters for this program was referenced from
 https://medium.com/simpl-under-the-hood/classifying-gender-based-on-indian-names-in-82f34ce47f6d
 using their finding for hindi first names corpus. Decision tree can also be made based on the if
 statements in the above program. Its not completely accurate for men names.
 '''
# https://github.com/skylanskylion/IndianFirstName_classifier link the program and screenshots
