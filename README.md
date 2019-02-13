# PCN_Project_1
CS6352 Performance of Computer Networks Project 1

In this problem, you will implement an event-driven simulation of a queueing system. In an event-driven simulation,
the system state is updated only when an event (e.g., an arrival or a departure) occurs, rather than being updated at
periodic time intervals. When an event occurs, several steps must be taken to update the system state. The first step is
to update the system time to the time at which the event occurred. The next step is to update any other state parameters,
such as the number of customers in the queue. Finally, new events are generated based on the current event. Once the
system state is updated, the simulation moves on to the next event in chronological order.

Running system: Mac OS

Compiler: Python 2.7.15

For running my code, you need to install numpy and matplotlib libraries for Python.

Install intruction: pip install numpy & mayplotlib
