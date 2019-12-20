#Introduction

This is a choose your own adventure python program about the classic tale of the three little pigs. 
I am doing this to practice the basics of python which I have just learned. 

 #Game overview 
 
 Three little pigs lived in their houses made of wood, brick and straw. The wolf came by and wanted to blow thier houses down 
 The wolf needed more power to successfully blow down the houses that were made of stronger materials. 
 
 The strength of the materials were , in order of strength 
 Straw --> Wood--> Brick 
 
 The player is the wolf and has to select the strength with which he tries to blow down the house
 if he selects a strong enough value, he will get a message "You have blown the [] house down!" otherwise he will get another message 
 "Sorry you need to blow harder to knock this house down!"
 
 
 #Game logic 
 
 The player enters the game 
 The program asks him to enter his name 
 The name is stored as a variable and will be shown as part of subsequent messages 
 The game returns a message "Hello [yourname]!"
 
 The game displays the story of hte three little pigs 
 "Welcome [yourname]. In this game, there are three little pigs. The youngest pig, Rupert, has a house made of straw.
  The middle pig, Oscar, has a house made of wood. The oldest pig, Wilbur, has a house made of brick. 
  You are the wolf. For some inexplicable reason, you want to blow all their houses down.
  You will need to choose how hard you want to blow down these houses. 
  The sturdier houses will need you to blow harder. 
  Once you have blown down all three houses, the game will end .
  
  Good luck!"
  
  The game asks the player to select which pigs house he wants to blow down
  "[yourname], please select which pigs house you want to blow down 
  (a) Rupert (Straw)
  (b) Oscar (Wood) 
  (c) Wilbur (Brick) 
  
  Remember, the stronger the house, the harder you need to blow! "
  
  the player makes a choice 
  
  The game asks the player to select the strength he wnats to blow the house down with (between 0 -100) 
  to successfully blow down a house, he needs to select 
  Straw house >=20
  Wood house >= 50
  Brick house >= 70
  
  If he is successful, the game displays a message 
  "You have blown the [] house down!" otherwise he will get another message 
 "Sorry you need to blow harder to knock this house down! Please try again!"
 
 Once he successfully blows down all the houses, the game ends with this message 
 "[yourname] you have blown all houses down! Congratulations! "
  