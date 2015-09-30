===============================
defaultsob
===============================

.. image:: https://img.shields.io/travis/honewatson/defaults.svg
        :target: https://travis-ci.org/honewatson/defaults

.. image:: https://img.shields.io/pypi/v/defaults.svg
        :target: https://pypi.python.org/pypi/defaults


A simple package to create data structures with defaults and strict limitations of attributes/properties.

* Free software: ISC license
* Documentation: https://defaults.readthedocs.org.

Features
--------

.. code-block:: python
   class User(Defaults):
       __slots__ = [
          "name",
          "description",
          "an_attribte_with_no_default"
      ]
      """
      usef will use the 'name' attribute
      if the description attribute is not
      set at the time of object creation
      """      
      description = usef('name')
   
   user = User(name='Billy')
   """
   .to_dict_clean method returns a
   dictionary of attributes with values
   """
   print(user.to_dict_clean())
   {
      "name": "Billy",
      "description": "Billy"
   }
   
   user.description = "Something Else"
   user.an_attribute_with_no_default = "Another"
   print(user.to_dict_clean())
   {
      "name": "Billy",
      "description": "Something Else"
      "an_attribute_with_no_default": "Another"
   }

    
   user2 = User(name="Billy", description="The Kid")
   print(user2.to_dict_clean())
   {
      "name": "Billy",
      "description": "The Kid"
   }



