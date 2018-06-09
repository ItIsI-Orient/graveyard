
.. _faq:

********************************
QNEA (Questions Not Even Asked)
********************************

What is it?
===========

DraciDoupe.cz is a collaboration place for pen-and-paper RPG creativists, designed to host a single (dated) RPG system, Draci Doupe, from a single country, Czech Republic. Back in early 00's, it also served as a social network for (not only teen) fantasy fans.

In peak of its popularity, it enjoyed thousands of visitors per day (huge number back then). The popularity declined as both technology, the RPG system and the concept of community sites become dated (being consumed by Facebook and likes). It still treasures hundreds of articles and a lot of capture creativity.

Hence, it still attracts few hundred of visitors every day.

Why work on it?
================

Because I want to keep it available, something to be discovered for both nostalgics and new player generation, if only for nostalgia reasons. That is unsustainable in current state, mainly for security reasons. 

Also, I am just grateful. This site shaped my life like nothing else.

Why not fix the product in the process?
=======================================

That was an idea of RPGPlanet, planned successor to DraciDoupe.cz. It, however, entered development hell, coupled with changing landscape of how sites are consumed. It was also never truly accepted by community, hence dying before bing born. 

Thus, I decided to instead fix the current state. 

Why reimplementation instead of fix?
====================================

Because it has been born in a different time and is very hard to fix incrementally. 

Smartphone was not a thing, PDA barely was. Broadband was only available at universities, dial-up connection was a way to connect to internet. PHP just changed its name and came out as PHP 3. CSS was in version 1 and impossible to get working accross browsers consistently; tables were used to do page layouts. Netscape was something to be tested. Mozilla Suite was gaining traction, Firebird (later called Firefox) hasn't been born yet. Internet Explorer 5 was ruling it.

DDCZ has been kicked out by its hosting provider for consuming more than 1 GB of outbound traffic *per month*, moving on to be hosted on bare metal. The database was huge for its time, counting data in *hundreds of megabytes*. That's why UTF has been considered wasteful at the time and not adopted everywhere. 

JavaScript (called JScript in IE) was in its infancy, both DOM and language inconsistent accross browsers (without any façade library; jQuary hasn't been born yet), painfully slow and with security holes, as well as cookies. *The whole site has been designed to work with both JavaScript AND cookies to be turned off*. 

PHP, the implementation language of choice (not many other options, although ASP 3 implementation has been attempted) hasn't supported `register_globals` feature flag and it has been *on*. This created a huge problem for the future since it can't be turned on in "modern" PHPs. This renders the whole codebase unworkable and tricky to refactor.

At last, but not at least, the whole site has been architected, designed and implemented by three 16 year olds who learned programming on this. 

All of those contribute to architectural decisions that are very hard to reverse, and clean-slate rewrite is better option. 

You don't have time to do this
==============================

I don't and I don't want this to be another RPGPlanet. Which is why this is going to be implemented in stages, fist one being very easy yet still useful. 

What will stay?
===============

Most of the things from user perspective. The goal is to preserve, not to rework. Some changes will be done in the name of usability, though.

* Public site still usable without cookies
* Privacy still considered important
* Original URLs. Redirects will be in place
* Site being Czech to the bones (and routes)
* Skins. They are terrible, make the site much harder to develop, makes maintenance costly and doesn't bring almost any value. I love them
* Filters, some of them. They are beautifully terrible in the same way skins are
* User registration approval. It's elitists, awful, unfriendly and it makes the site the way it is
* Focus on user privacy. All data is pseudonymous. No personal information collected

What will change?
=================

* Either cookies or local storage (TBD) will be required for skins and for log in. Those days, it's *more* safe than URL parameter, trust me. It also means it is safer to have longer session length than terrible 15 minutes
* Public site still working without either, though
* SEO, those articles deserve it. Current site is *very* unfriendly to search engines
* Security, on multiple levels
* Moudra Sova, the over-the-decade, manually-patched version of Phorum is going to either go away, or be sandboxed. It doesn't see almost any activity anyway
* Source now open (as opposed to old version)
* Filters, some of them. In a lot of places they don't really make sense; I want to keep them, but if they'd complicate implementation too much, they are (at least temporarily) gone
