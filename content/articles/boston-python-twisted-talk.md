Title: Boston Python - Twisted Concepts & Patterns
Slug: boston-python-twisted-talk
Date: 2015-08-28
Tags: python, twisted

[Patrick Cloke](http://patrick.cloke.us/) and I recently gave a talk at
[Boston Python](http://www.meetup.com/bostonpython/) meetup
about the [Twisted Networking Framework](https://twistedmatrix.com/).
It was an introductory to intermediate level talk based on our experiences
using Twisted at [Percipient Networks](http://strongarm.io).

The slides and example code are available on
[GitHub](https://github.com/percipient/talks). There is a
[rendered PDF](https://github.com/percipient/talks/blob/master/boston_python_08_27_2015/boston_python_08_27_2015.pdf)
for convenience. The talk covered:

1. What is asynchronous programming?
1. What is Twisted?
1. When/why to use Twisted?
1. What is the event loop (`reactor`)?
1. What are `Deferreds` and how do you use them?
1. What are protocols, protocol factories, and transports?

Additionally, there was a "bonus" section on using Twisted to build systems
and services. We used an example of a simple chat server with an admin
dashboard to demonstrate integrating Twisted in the larger Python ecosystem.

Thank you to everyone who attended, the sponsors for the night, and the
organizers of [Boston Python](http://www.meetup.com/bostonpython/).
An additional thank you goes out to Patrick for co-presenting and my very
supportive wife for attending.
