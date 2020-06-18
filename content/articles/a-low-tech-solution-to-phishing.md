Title: User Training: A Low-Tech Solution to Phishing
Slug: a-low-tech-solution-to-phishing
Date: 2017-09-08
Tags: phishing, security

> This article was originally posted to the Strongarm blog in 2017 and has been reposted here on my personal site. Many of the links and resources are broken, but the content is still valid.

<img src="/images/phishing.png" class="img-thumbnail" alt="Phishing Logo">

Early in my career, I was an active naysayer against “security awareness training.” The idea that we could train every employee in the company to actively identify phishing emails and never fall victim didn’t just seem improbable; I thought it was impossible.

Why? Well, the attacker only needs one person to fall victim and click that suspicious link or open that sketchy word document, and they gain access to our network. Meanwhile, we, as security defenders, need to be perfect! We can’t make any mistakes... and neither can our employees!

It didn’t seem realistic to me.

Instead of investing in education and training, I wanted to build technical solutions to security problems. I thought investing resources in technically enforcing security policy would take the human error out of the equation.

Fortunately, I wasn’t in charge. At my previous workplaces, we invested heavily in security training and user education over the years, in spite of my point of view. We trained employees to identify phishing emails and other threats and report them to our internal security team. Sure enough, the emails and reports flowed in.

And I realized I was wrong. The results of employee education and training were overwhelmingly strong. On more than one occasion, an employee-reported email led to the detection and prevention of a targeted attack. That same attack had bypassed all of our email filtering solutions and intrusion detection systems, which included capabilities to “detonate” and inspect URLs and file attachments. The humans beat the machines handily.

In addition, we used trends in reporting to help understand who (human resources, finance, engineering, etc) was being targeted and when. With this information, we were able to improve our security training and phishing prevention.

This experience taught me that there is deep value in treating your users as your front-line defense. You should, of course, have technology that can facilitate the detection and remediation of any threats that make it through your human and machine barriers, but there is no substitute for strong user education, and especially for training your users to spot and report suspicious emails.

# Getting Started with User training

Okay, so all that sounds good in theory. But getting started with security awareness training is often the hardest part. We suggest leveraging free training materials, including our [own short guide to spotting phishing emails](https://strongarm.io/blog/tips-to-spot-phishing/). In addition, the Government of Canada has compiled [free security training resources](https://www.getcybersafe.gc.ca/index-eng.aspx) including a [three-minute video](https://www.youtube.com/watch?v=9TRR6lHviQc) to introduce the skills needed to thwart phishing.

Part of this training includes instructing your employees to forward suspicious emails to your IT and security team. We suggest creating an email distribution list, security@<your-company-domain> specifically for this purpose.

# Analyzing Employee-Reported Emails

Once you are in a place where employees are forwarding suspicious emails to your IT and security team, you need to work on a process to analyze them and provide feedback to the employees.

The analysis process can be very complicated, but again, starting with a simple approach is best. Check our guide for [spotting phishing emails](https://strongarm.io/blog/tips-to-spot-phishing/), and pay attention to unexpected email senders and mismatched links. If you have a dedicated analysis environment where you can safely visit the suspicious URLs, do so; the intent of the email often reveals itself in the form of [credential theft](https://strongarm.io/blog/docusign-phishes/) or other attack.

Once you have determined if the email is indeed malicious, it’s time to respond to the employee who reported it. Thank them and provide them with enough information to reinforce the value of their diligence.

# Taking Training and Education to the Next Level

Lastly, you need a strategy to prevent your employees, specifically those “happy clickers” inside your company who will click on just about anything, from falling victim to threats. You can do this by blocking access to bad domains used in suspicious emails. This can often be done in your firewalls and web proxies, but the best way to do it is via your DNS. If you are a Strongarm customer, we have you covered.

Over time, you will start to see trends in both the type and intent of suspicious emails being sent to your business, as well as your employees’ increasing ability to spot and report them. This information helps inform where and how to improve security. For example, if you are often targeted with credential theft attacks, it may be worthwhile to invest in improving password strategies and implementing [password management solutions](https://strongarm.io/blog/password-best-practices/).

Alternatively, if you find only a certain team, like those pesky folks in sales, are routinely falling victim to phishing, it may be worth creating some training specifically for them.

# How Strongarm Can Help

When you sign up for a [Strongarm account](https://app.strongarm.io/accounts/signup/) and protect your business, our team is here to help proactively block any malicious domains found. This way, if in spite of user training and education, any of your employees fall victim to a phish or other scam, there will be no damage to your business. The user will simply be presented with a Strongarm block page, which includes on-demand security education to help make sure they don’t click on a bad link again.
