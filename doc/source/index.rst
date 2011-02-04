.. slim documentation master file, created by
   sphinx-quickstart on Thu Feb 03 18:00:52 2011.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.
   
======================================
Welcome to SLiM project documentation!
======================================

This project is still in its early stages and many things described here will 
probably change in the near future. Quick overview.

The Core
--------

SLiM core is a component that is intended to be embedded in an agent 
architecture. It provides a clear API through which other modules, which are 
part of the agent architecture, can connect.

The main objective of SLiM core is *flexible collaboration between modules of an 
agent*. Hopefully, it will help us build more open agents in the sense that 
modules can be added, removed and interact in new ways over time.

It has three main functions: *symbolic data store*, *know-how* base and 
*rules base*.
 
 
The Modules
-----------

Modules have to be registered with the SLiM core in order to be able to use it
and expose their capabilities to other modules. Here is a detailed description 
of the registration process.

There is one default module called lang providing a language that can be used 
to manipulate the core. This language can be used through the SLiM interpreter 
or from any other code through the Do API.

.. image:: images/waa-quick.png
	:width: 300
	


Contents:

.. toctree::
   :maxdepth: 2
   
   intro
   tutorial

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

