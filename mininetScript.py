# Author: Mrinal Aich
# Roll No. CS16MTECH11009

"""
Firewall based SDN network
"""
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.node import RemoteController
from mininet.cli import CLI

class SingleSwitchTopo(Topo):
    "Single switch connected to n hosts."
    def build(self, n=2):
        h1 = self.addHost( 'h1' )
        h2 = self.addHost( 'h2' )
        s1 = self.addSwitch( 's1' )
        
        h3 = self.addHost( 'h3' )
        h4 = self.addHost( 'h4' )
        s2 = self.addSwitch( 's2' )
        
        h5 = self.addHost( 'h5' )
        h6 = self.addHost( 'h6' )
        s2 = self.addSwitch( 's3' )

        # Add links
        self.addLink( h1, s1 )
        self.addLink( h2, s1 )
        
        self.addLink( s1, s2 )
        
        self.addLink( s2, h3 )
        self.addLink( s2, h4 )
        
        self.addLink( s2, s3 )

        self.addLink( h5, s3 )
        self.addLink( h6, s3 )

def simpleTest():
    "Create and test a simple network"
    topo = SingleSwitchTopo(n=4)
    net = Mininet(topo, controller=None)
    " Remote POX Controller"
    c = RemoteController('c', '0.0.0.0', 6633)
    net.addController(c)
    net.start()
    print "Dumping host connections"
    dumpNodeConnections(net.hosts)
    CLI(net)
    net.stop()

if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    simpleTest()
