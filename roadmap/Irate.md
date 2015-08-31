Irate God
========

Scenario: There are no YGO sims. I have every technology available.
-----


My thought process: I would firstly focus on deciding whether I want **manual** or **automatic** duel styles. Manual requires less game setup but requires the players to communicate (like DN does right now), automatic requires more coding and takes away the task of keeping track of everything for the user (like YGOPro does right now). I don't believe those two can really be integrated together, so I would have to decide on either. Below my thoughts on what to implement for each respective duel style.

#### Manual

* The most important implementations are an automatically updated card database as well as a good GUI to improve player communication.
* Matchmaking and rankings (using possibly an ELO system) should be intuitive and competitive, where users with low ELO will never get matched against opponents that would most likely crush them.
* Incentives (such as additional profile customization, borders on your profiles like League of Legends has) can encourage users to play more, but those are not necessarily of the highest priority.
* While duelling, players should always be given the tools to keep track of everything (counters, life points, status increase/decrease, etc.), and communication should always be optimized, possibly providing the players with a VoIP chat, though this is not of the highest priority.
* Priority for me is as following:
	1. Automated CDB
	2. GUI
	3. Player Communication
	4. Tools for players in duel
	5. Matchmaking and ranking, profiles, incentives to play.

#### Automatic

* Players are provided with card rulings and turn sequences by themselves.
* A VoIP chat is not needed as the game progresses by itself, though a normal chat is still used and should still be used frequently to communicate.
* Features here would, again, be: 
	1. An automated CDB
	2. An intuitive GUI (point-and-click as opposed to keyboard controls like "WASD")
	3. Matchmaking and rankings.
	
Essentially, this would be the same as the manual duel style with less direct user interaction where the system takes over the duel and players provide input wherever necessary. To prevent slow play, AFK and such, *players would be given a response window of 2 minutes to perform an action*, after which they would **get kicked by the server**.
A player may not take longer than 3 minutes for their entire turn, which gives them enough time to think about their plays but should prevent slow play. As achieved with an automated CDB, rulings will also be automatically monitored, like the entire game interaction. Profiles and incentives are not of a high concern but could still be implemented for the Quality of Life customization of each player.
