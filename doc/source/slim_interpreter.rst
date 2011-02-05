The SLiM interpreter
====================

The SLiM interpreter is a small module, like any other module, that takes a 
string representation in the SLiM language and performs the required *tell* and
*do* actions on the SLiM core to which it is connected. 

SLiM language
-------------

.. highlight:: pascal

The SLiM language has a simple syntax::

  description ::= (slim | do slim)+
  slim ::= '{' symbol+ '}'
  symbol ::= (>)? (id | link) ( : (info | symbol))?
  link ::= '{' (symbol | info)+ '}'
  
A SLiM description is a collection of slim structures and for some
of them *do* is invoked in which case the '>' character marks the entry points.
The ``info`` in the last production rule is used for creating anonymous symbols
and attaching information to them. 

.. highlight:: c

Examples of statements in the SLiM language: ::
   
    {
       // create symbols 
       Razvan
       phone
       
       // create links
       {Razvan phone}
         
       // assign information to symbols
       Razvan: "Razvan Dinu"
       {Razvan phone}: "450-332-4845"
        
       // perform a mapping
       {type show} : function
    }
     
    // do two actions in parallel
    do {
       >{print Razvan}
       >{call {Razvan phone}}
    }
       
    

How it works
------------

The interpreter is registered with a SLiM core as any other module. When a 
description in the SLiM language is given it will start parsing each slim one
by one. When a simple slim is found (without a *do*) then *tell* is invoked
otherwise *do* is invoked. The slim structures parsed by the interpreter will
be referred to as tell-slim or do-slim. The slim structure used in the SLiM core
will be referred to as core-slim.    

Tell mode
~~~~~~~~~

When a tell-slim is passed to the SLiM core, the core-slim will "assimilate" it 
by creating the missing symbols, links and mappings. For example: ::

   {
      {picture327 type jpg}
      {picture327 url "http://something.org/a.jpg"}
      {profile picture} : picture327 
   } 

the ``type``, ``jpg``, ``url``, ``profile`` and ``picture`` symbols will 
probably already exist in the core-slim but ``picture327`` and the anonymous
symbol corresponding to the url information will have to be created. Also, all
the above links and the mapping from the last line will have to be created. 

Do mode
~~~~~~~

On the other hand, when a slim is passed in *do* mode it will only *unify* with 
the slim structure of the SLiM core for the duration of the required actions.
For example: ::

   do {
      some-picture : {profile picture}
      >{show on screen some-picture}
   }
    
By the unification process a new unified-slim will be created from the union of 
the core-slim and the do-slim by taking the symbols  
``profile``, ``picture``,  ``{profile picture}``, ``show``, ``on`` and 
``screen`` only once. The action indicated by the entry point will be performed
on this new slim and after that it will be discarded. 

Obviously, assuming the tell-slim from the previous example is processed right
before this one then ``picture327`` will be displayed on the screen. 

