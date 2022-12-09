# Firewall based SDN Network

Staring with Firewall based SDN

## Introduction

In SDN Networks, the network intelligence is logically centralized in software-based controllers (the control plane), and network devices become simple packet forwarding devices (the data plane) that can be programmed via an open interface (OpenFlow).

## Firewall

SDN could be used to replace expensive Layer 4-7 firewalls, load-balancers, and IPS/IDS with cost-effective high-performance switches with a logically centralized controller.
In this project, I have implemented Layer 2, 3 & 4 firewall by proactive policies and managed to block several applications like specific link, host-to-host connectivity and destination process.

## Architecture

There are one each POX Controller and OVS-Switch alongwith 4 Hosts forming an SDN Network.

---

---

## Prerequisites

Your system should install mininet and pox packages.

## Installing

There are two scripts namely, mininetScript.py and poxController_firewall.py which will run the mininet based ovsSwitch and POX Controller respectively.

- Running the POX Controller
- Go to the pox directory installed in your setup and execute

  ```
  ./pox.py log.level --INFO poxController_firewall
  ```

- Running the Mininet and OVS-Switch
- Execute the python script
  ```
  python mininetScript.py
  ```

## Running the Tests

## perform some tests using `ping` and `pingall` command.
