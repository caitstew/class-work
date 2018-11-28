guestlist = ["eleanor roosevelt", "george washington", "winston churchill"]
print(guestlist[0].title() + ", you are formally invited to my snazzy dinner party.")
print(guestlist[1].title() + ", I would be so thrilled if you could come for my dinner party.")
print("I hope that you, " +guestlist[2].title() + ", can attend my dinner party!")

print("\nUnfortunately, " + guestlist[-1].title() + " can not make it.")
guestlist[-1] = "joan of arc"
print("\n" + guestlist[0].title() + ", I am so hopeful that you can come to my dinner party.")
print("I really hope that you, " + guestlist[1].title() + ", can still come!")
print(guestlist[2].title() + ", I would be estatic to see you at my dinner party!")
print("\n" +guestlist[0].title() + ", " +guestlist[1].title() + ", and " +guestlist[2].title() + ", I have found a bigger table!")
guestlist.insert(0, "gordon ramsay")
guestlist.insert(2, "mary berry")
guestlist.append("jo gaines")
print("\n" + guestlist[0].title() + ", I hope to see you at my dinnr party.")
print(guestlist[1].title() + ", I'm so excited to see you!")
print("I really hope that you, " + guestlist[2].title() + ", can come to my dinner party.")
print(guestlist[3].title() + ", I hope you can come to my dinner party.")
print("My dinner party will be so much better with you, " + guestlist[4].title())
print("I hope to see you at the dinner party, " + guestlist[5].title() + ".")
" "
print("\nUnfortunately, I can now only accomodate two guests.") #this is so rude
popped_guests = guestlist.pop()
" "
print("\nI'm sorry, " + popped_guests.title() + ", but you can no longer come to my party.")
popped_guests = guestlist.pop()
print(popped_guests.title() + ", you are no longer invited to my party.")
popped_guests = guestlist.pop()
print(popped_guests.title() + ", I'm sorry I can't have you come anymore.")
popped_guests =guestlist.pop()
print("You can no longer come, " + popped_guests.title() + ".")
print(guestlist)
print("You are still invited, " + guestlist[1].title() + "!")
print ("You are also still invited, " + guestlist[0].title() + "!")
del guestlist[0]
del guestlist[0]
print(guestlist)