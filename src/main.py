'''
Created on Oct 6, 2010

@author: Razvan
'''
from slim.symbolic.waa import SlimCore
from slim.modules.modules import Ping

if __name__ == '__main__':
    print "SLiM python prototype."
    
    waa = SlimCore()
    core = waa.core
    
    # register required modules
    waa.register(Ping())
    
    waa.do("pong");
    waa.do("ping");
    
    waa.core.add("msg", "Hellow there")
    l = waa.core.quick_link(None, [waa.core.symbols["notify"], waa.core.symbols["msg"]])
    waa.do(l.id);
    
    # dump the core
    core.show()
  
