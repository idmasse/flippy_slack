## SLACK BOT POWERED BY OPENAI
This bot posts a message generated by ChatGPT to a slack channel every six hours.

### GOAL
Find a way to ensure that a computer on a local network is powered on and its operations are functional. Due to certain circumstances, I wasn't able to forward a port on my local network to expose it to the internet, so I designed this bot to act as a de-facto ping. If I don't get a slack notification from the bot every six hours, I'll know to check that the computer is still running. 

### PROCESS
To make this more interesting (as opposed to just posting the same message over and over), I decided to make the bot prompt ChatGPT to post to the Slack channel. This has been through several iterations, first I had it create a dark-humored haiku, then asked it to tell jokes, after that it was posting horroscopes, and now it's posting a word of the day. 

For this iteration, I at first simply asked it to just post a word of the day, but it kept repeating the same words over and over. To get some variety, I implemented a solution for it to choose a word based on a randomized letter selection.

### IMPLEMENTATION
The bot is scheduled to run every 21600 seconds (six hours) via a plist. 