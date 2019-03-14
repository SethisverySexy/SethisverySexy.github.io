import random     
import time


    
def gameOver():     
      print "Game OVER!!! Too Bad!"     
      retry = raw_input("\n\nWant to try again? (yes or no)\n\n").lower()     
      if retry == "yes":     
         game()     
      else:     
         quit()     
    
def game():   
    
   gold = 50     
   character_hp = 125     
   weapon_damage = 15     
   monster_damage = 25     
   monster_payout = 80     
      
   weapons = ["fists"]     
      
   MONSTERS = {     
      "goblin":55,     
      "zombie":80,     
      "wolf":105,     
      "dragon":150   
  }     
      
   name = raw_input("\nWhat is your name young padiwan?\n\n").title()     
      
   while name == "":     
      name = raw_input("\nWhat is your name young padiwan?\n\n").title()     
      
   print "\nWelcome", name, "Enjoy, Your Adventure!\n"     
      
   while character_hp > 0:     
      
      WEAPONS_STORE = {     
       "sword":140,     
       "axe":120,       
       "club":75,       
       "bat":45     
      }     
      
      store = raw_input("\nDo you want to buy weapons? (yes or no)\n\n").lower()     
      
      if store == "yes":     
         print "\nWEAPON\t\tCOST\n"     
      
         for items in WEAPONS_STORE:       
            print items, "\t\t", WEAPONS_STORE[items], "\n"     
      
         print "\nYou have", gold, "gold\n\n"     
         weapon_purchase = raw_input("Which weapon would you like to buy?\n\n").lower()     
      
         while weapon_purchase not in WEAPONS_STORE or weapon_purchase in weapons:     
            weapon_purchase = raw_input("Which weapon would you like to buy?\n\n").lower()     
      
         if weapon_purchase in WEAPONS_STORE and weapon_purchase not in weapons:     
      
            if gold >= WEAPONS_STORE[weapon_purchase]:     
               print "you bought a(n)", weapon_purchase, "\n"     
               gold -= WEAPONS_STORE[weapon_purchase]     
               weapons.append(weapon_purchase)     
               print "\nyou have", gold, "gold\n"     
               print "\nWeapons(s) you own\n"     
               for items in weapons:     
                  print items       
      
            elif gold <= WEAPONS_STORE[weapon_purchase]:     
               print "not enough gold"     
      
      elif store == "no":     
      
         print "\nTime to get off your La-Z-Boy Sofa and go kill a monster!\n"    
         print "\nMONSTERS\tHEALTH\t\n"     
         for monster in MONSTERS:     
            print monster, "\t\t", MONSTERS[monster], "\n"     
      
         monchoice = raw_input("Which tseries fan do you want to brutally defeat?\n\n").lower()     
      
         if monchoice in MONSTERS:     
    
            print "\n Good Luck! End that thing!", monchoice, "From the bois"     
                
         else:     
    
            print "That brute is not in this town!"     
    
            while monchoice in MONSTERS:     
    
              monchoice = raw_input("Which tseries fan do you want to brutally defeat?\n\n").title()     
                      
         print "\nWEAPONS YOU OWN\n"     
    
         for weapon in weapons:     
    
            print weapon, "\n"     
    
            weapuse = raw_input("What weapon will you choose?\n\n").lower()     
    
         if weapuse in weapons:     
    
            print "\nI Like It!", name, "You are using the", weapuse, "against the", monchoice     
    
         if weapuse == "fists" or weapuse == "bat":   
            gold
    
         elif weapuse == "club" or weapuse == "axe": 
            gold 
  
         while character_hp > 0 and MONSTERS[monchoice] > 0:   
            rand = random.randint(5, 20)   
            pdmg = weapon_damage + rand   
            mdmg = monster_damage   
            print monchoice, "has", MONSTERS[monchoice], "health left\n\n"   
            time.sleep(1.5)   
            print "The", monchoice, "attacked YOU by", mdmg   
            character_hp -= mdmg   
            if character_hp <= 0:   
                gameOver()   
    
            print name,", your health is now", character_hp   
            time.sleep(1.5)   
    
            print "\nYou attacked the", monchoice, "with the", weapuse, "for", pdmg, "damage!"   
            MONSTERS[monchoice] -= pdmg   
            time.sleep(1.5)   
    
            while character_hp > 0 and MONSTERS[monchoice] > 0:     
              rand = random.randint(3, 7)     
              pdmg = weapon_damage + rand     
              mdmg = monster_damage     
    
              print monchoice, "has", MONSTERS[monchoice], "health left\n\n"     
              time.sleep(1.5)     
              print "The", monchoice, "attacked YOU by", mdmg     
              character_hp -= mdmg     
              if character_hp <=0:     
                  gameOver()     
    
              print name,", your health is currently", character_hp     
              time.sleep(1.5)     
    
              print "\nYou attacked the", monchoice, "with the", weapuse, "for", pdmg, "damage!"     
              MONSTERS[monchoice] -= pdmg     
              time.sleep(1.5)     
         else:   
    
             print name, "\nYou don't have that, balls", weapuse, "!"     
    
             while weapuse not in weapons:     
    
               weapuse = raw_input("\nWhat wepaon will you use\n\n").lower()     
    
             print "\nI Like It!, name, You are using the", weapuse, "against the", monchoice         
game()
