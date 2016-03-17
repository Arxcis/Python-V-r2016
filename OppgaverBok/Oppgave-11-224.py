

this = ["I", "am", "legend"]
that = ["I", "am", "legend"]

""" Lists has the property that they do not occupy the same
  place in memory, even if they are identical. 
    You have to explicity specify this = that to 
   make that happen. When you do this = that, this and that become
    aliases of each other. If you change one of them, you change both. 
     Because they now point at the same object in memory. 
  """
print("Test 1: {0}".format(this is that))

"""
   The following operation makes "this" forget the object it is pointing to,
    and starts to point at the same object that "that" is pointing to. 
"""
this = that
print("Test 2: {0}".format(this is that))


