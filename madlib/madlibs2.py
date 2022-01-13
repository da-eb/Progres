from madlibs import *

@madl
def madlib():
    madlibs = f"Today we picked apple from {noun} Orchard. I had no idea there were so many different varieties of apples. I ate apples straight off the tree that tested like {noun}.\
         Then there was a {adj} apple that looked like a {noun2} '.When our bag were full, we went on a free hay ride to '+place+ ' and back. It ended at a hay pile where we got to {verb2}. \
             I can hardly wait to get home and cook with the apples."
    print(madlibs)

if __name__ == "__main__":
    madlib()