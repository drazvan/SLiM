Introduction to SLiM
====================

The SLiM model is based on three main concepts:

- **Symbol**. a symbol is an abstract thing with a unique identity, represented by the id property.
- **Link**. a link is a symbol that groups together, in a specific order, multiple symbols.
- **Mapping**. A mapping is a function that associates each symbol with one other symbol.


Also, every symbol has an associated piece of **information**. It can have any type (python prototype: a reference to an object).

The whole set of symbols and links form a generalized hypergraph structure and it will be further referred to as *symbolic hypergraph* or simply hypergraph. Together with a mapping they form a structure which we call simply a *slim*.

   


