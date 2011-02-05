'''
Created on Oct 6, 2010

@author: Razvan
'''
from slim.symbolic.waa import SlimCore
from slim.modules.modules import Ping

if __name__ == '__main__':
    print "SLiM python prototype."
    
    waa = SlimCore()
    core = waa.slim
    
    # register required modules
    waa.register(Ping())
    
    waa.do("pong");
    waa.do("ping");
    
    waa.slim.add("msg", "Hellow there")
    l = waa.slim.quick_link(None, [waa.slim.symbols["notify"], waa.slim.symbols["msg"]])
    waa.do(l.id);
    
    # dump the core
    core.show()
  
