.. slim documentation master file, created by
   sphinx-quickstart on Thu Feb 03 18:00:52 2011.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.
   
======================================
Welcome to SLiM project documentation!
======================================

This project is still in its early stages and many things described here will 
probably change in the near future.
	


Contents:

.. toctree::
   :maxdepth: 2
   
   intro
   slim_structure
   slim_core
   slim_interpreter
   symbols
   pattern_matching
   
   
Example that currently works
----------------------------

Here you can find an up-to-date working.

.. highlight:: c

Input: ::

    {
       {picture327 type jpg}
       {picture327 url "http://something.org/a.jpg"}
       {profile picture} : picture327   
    } 
    
    {
       {my name} : "Razvan"
       {Razvan age "25"}
       some-value : "Original" 
    }
    
    do {
        some-value : "Some value"
        >{notify some-value }
    }
    
    do {
        some-value : "Some other value"
        >{notify some-value }
        >{notify "Hello, I'm printing anonymous symbols"}
    }
    
    do{
        >{
            {notify some-value}
            {copy some-value "A new value"}
            {notify some-value}
         }
    }

Output : ::

    notification: ' Some value '
    notification: ' Some other value '
    notification: ' Hello, I'm printing anonymous symbols '
    notification: ' Original '
    notification: ' A new value '

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
