# Roadmap

In the following documentation, I would like to remark wanted features, as well features I will work on implementing int he future as well. It should be noted that my main platform is mac OS X with access to a Linux server and an occassional Windows XP VM.

## General
- A news blog with some status updates on a frontpage tells people that the project is alive.

## Community
- Having a forum/place for people to talk at is a key in -every- good game. If users cant communicate, you can not improve.
- Users need to be able to talk with the devs. If the devs are __up in heaven and gone by far__, they'll be unhappy and believe that they are unheared, ignored, not relevant to the game.
- People get sad and want to talk about their issues. **Take a good look at them!** A drama-loaded community (= `drama-house`) destroys many good things and prohibits evolution and improvement. Here is what I have learned while owning a community myself:
    * There needs to be a handful of person that are non-biased, moderative and direct. They need to tell the drama-causing people (= `drama whore`/`attention whore`) to move the drama away from the public and put it into a different room or private messages.
    * **Keep the first-room-to-be-seen as clean as possible**. If someone runs into a room full of arguring, they'll likely grab their feet and ran off!
    * There should be a volunteer that can take care and talk to people if they are feeling unhappy. They need that. Plus, if they feel valued by the staff, itll make them very, very loyal. Not to mention that they'll recommend the place as being "helpful and awesome".
    * I sometimes hear, that people call my site as their "online home". If people say that about your place...you did it totally right.
    * Let users have a word in staff voting or staff administration. At least ask them for opinions.
- Polls can be quite a helpful thing.

## Staff
- Members should have a rough understanding of code.
- The staff should know, what the other members are capable of.
- Try to share tasks. Some people are better at things than other. Together is better.

## Technical / Code
### YGOPro
- Re-implement the YGOPro GUI and make it cross-platform.
- Make building YGOPro easier and faster. (Mainly changing the build tool and mechanism.)
- Allow card images to be dynamically downloaded.
- Allow clients to share unknown cards. I.e.: The option "Allow custom cards" was enabled, then client A might not have this card, whilst client B does. So client B sends the information plus image over so the game can continue flawlessly.
- Investigate into the C++ based network protocol and try to implement it as a library so a nodejs module can be made out of it.
- Allow for card sleeves to be exchanged.
- Allow keyboard/gamepad controls.
- Support native fullscreen on all platforms.

### YGOPro Launcher
- Implement public database to let the community share content, such as sleeves, field images and other graphics. Do __not__ allow audio material to be shared to not run into copyright flaws.
- Have either an installation bundle or a pre-launcher program that obtains missing resources - native client, node-webkit, etc. This actually could easily be implemented in C++ via FLTK.
- Allow uploading of replays.
- Enable a bug report feature. Bugs simply will exist.
- Allow user avatars (Though the forum might do that already).

### YGOPro Server
- Implement a RESTful API to let other developers integrate a server into their site. Imagine a small community whose main page should show the current amount of active duels.
- API to query for updates.
- Server administration client to monitor states and alike.
- Make the server itself headless - no node-webkit.

### General
- Abandon binary data from the Git repository. A user would otherwise download more junk (= files for other platforms) than they need.
- To create a development environment, offer a script to fetch needed/required resources. Can be simply done using custom NPM scripts.
