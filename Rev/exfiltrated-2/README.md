# Challenge Name:
exfiltrated-2

## Description:
kyk exfiltrated-1, ini chall ngawur krn author lg mls bikin dfir

## Category:
Reverse Engineering

## File:
./exfiltrated-2.pcapng

## Flag:
`NEXUS{exfiltrated_flag_90ae31ff45de}`

## PoC
- the exe read folder content
- split into 1024 byte chunks
- encrypt with RC4 key "helloworld"
- sent using icmp protocol

## Points:
500

## Author:
k.eii
