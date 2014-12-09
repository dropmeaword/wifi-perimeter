## Simple wifi-perimeter scanner

- Your client must speak OSC.
- **For OSX only**.

You are supposed to have the airport utility in your path, so you will have to open up a terminal and type in some commands.

Create a symbolic link to the airport utility in your path:

`sudo ln -s /System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport /usr/sbin/airport`

Test that it worked by typing:

`airport --scan --xml`
