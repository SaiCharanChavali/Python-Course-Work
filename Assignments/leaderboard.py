import random
leaderboard=[]

while True:
    print('1. Create a Leaderboard')
    print('2. Highest in the leaderboard')
    print('3. Lowest in the leaderboard')
    print('4. Descending order in leaderboard')
    print('5. Ascending order in the leaderboard')
    print('6. adding into the leaderboard')
    print('7. removing from the leaderboard')
    print('8. Checking the Leaderboard')
    print('9. Add a single player to leaderboard')
    print('10. Top player in leaderboard')
    print('11. Least player in leaderboard')
    print('12. exit')
    choice=int(input("Enter Your Choice: "))
    if choice==1:
        leaderboard=[random.randint(0,500) for i in range(10)]
        print(leaderboard)
        print("Leader Board Created  ")
    elif choice==2:
        print(max(leaderboard))
    elif choice==3:
        print(min(leaderboard))
    elif choice==4:
        print("\nLeaderboard in Descending Order:", sorted(leaderboard, reverse=True))
    elif choice==5:
        print("\nLeaderboard in Ascending Order:", sorted(leaderboard))
    elif choice==6:
        new_players= input("Enter the player numbers to be added to the list: ").split(' ')
        leaderboard.extend(map(int, new_players)) 
        print("Updated Leaderboard:", leaderboard)
    elif choice==7:
        remove_player = int(input("\nEnter the player score to remove: "))
        if remove_player in leaderboard:
            leaderboard.remove(remove_player)
            print( "Removed....Updated Leaderboard:", leaderboard)
        else:
            print("\nPlayer not found in leaderboard.")
    elif choice==8:
        print("The Leaderboard is : ",leaderboard)
    elif choice==9:
        single_player = int(input("\nEnter a single player's score to add: "))
        leaderboard.append(single_player)
        print("Updated Leaderboard:", leaderboard)
    elif choice==10:
        print("\nTop Player Score:", max(leaderboard))
    elif choice==11:
        print("\nLeast Player Score:",min(leaderboard))
    elif choice==12:
        print("Good Bye")
        break
    else:
        print("invalid option")
    
    
    


