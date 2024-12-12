package utils

import "net"

func AddrToIP(addr net.Addr) net.IP {
	x, ok := addr.(*net.TCPAddr)
	if !ok {
		return net.IPv4zero
	}
	return x.IP
}
