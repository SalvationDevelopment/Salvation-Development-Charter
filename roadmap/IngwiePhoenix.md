# Roadmap

In the following documentation, I would like to remark wanted features, as well features I will work on implementing int he future as well. It should be noted that my main platform is mac OS X with access to a Linux server and an occassional Windows XP VM.


## YGOPro
- Re-implement the YGOPro GUI and make it cross-platform.
- Make building YGOPro easier and faster. (Mainly changing the build tool and mechanism.)
- Allow card images to be dynamically downloaded.
- Allow clients to share unknown cards. I.e.: The option "Allow custom cards" was enabled, then client A might not have this card, whilst client B does. So client B sends the information plus image over so the game can continue flawlessly.
- Investigate into the C++ based network protocol and try to implement it as a library so a nodejs module can be made out of it.
- Allow for card sleeves to be exchanged.
- Allow keyboard/gamepad controls.
- Support native fullscreen on all platforms.

## YGOPro Launcher
- Implement public database to let the community share content, such as sleeves, field images and other graphics. Do __not__ allow audio material to be shared to not run into copyright flaws.
- Have either an installation bundle or a pre-launcher program that obtains missing resources - native client, node-webkit, etc. This actually could easily be implemented in C++ via FLTK.
- Allow uploading of replays.
- Enable a bug report feature. Bugs simply will exist.
- Allow user avatars (Though the forum might do that already).

## YGOPro Server
- Implement a RESTful API to let other developers integrate a server into their site. Imagine a small community whose main page should show the current amount of active duels.
- API to query for updates.
- Server administration client to monitor states and alike.
- Make the server itself headless - no node-webkit.

## General
- Abandon binary data from the Git repository. A user would otherwise download more junk (= files for other platforms) than they need.
- To create a development environment, offer a script to fetch needed/required resources. Can be simply done using custom NPM scripts.



I will update this document from here to then to add other roadmap points that other friends of mine mention or that i come up with.
