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

When a tell-slim is passed to the SLiM core, the core-slim will "load" it 
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

On the other hand, when a slim is passed in *do* mode it will be used in the
context of the core-slim for the duration of the required actions.
For example: ::

   do {
      some-picture : {profile picture}
      >{show on screen some-picture}
   }
   
A do-slim is not loaded as is the case for a tell-slim! (see below)
    
Contextual slim 
###############

What does "*used in the context*" mean?
Given a do-slim, a new **contextual slim** will be created from the union of 
the core-slim and the do-slim in which the core-slim will act as a context. 
That means that whenever a symbol is not found in the do-slim it will be also
searched in the context slim. The same goes for links, mappings and information.
For example, the information for ``{profile picture}`` in the above example 
will be fetched from the context slim (which is the core-slim). 

All the actions indicated by the entry points will be performed on the 
contextual slim and after that it will be discarded. 
Obviously, assuming the tell-slim from the previous example is processed right
before this one then ``picture327`` will be displayed on the screen. 

Updates during actions
######################

All the updates that are performed on the context slim during the execution of
different actions are actually performed on the context-slim. This way their
effect will persist even after discarding the contextual slim. 