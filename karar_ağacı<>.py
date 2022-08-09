print("decision tree game:\n keep an electronic device in mind:")
reply = input("is it electronic? [Y/N]")
if reply == 'Y' or reply == 'y':
    reply1 = input("is it portable? [Y/N]")
    if reply1 == 'Y' or reply1 == 'y':
        reply2 = input("can it be mounted? [Y/N]")
        if reply2 == 'Y' or reply2 == 'y':
            print("OK hour")
            reply3 = input("is it used to talk? [Y/N]")
            if reply3 == 'Y' or reply2 == 'y':
                print("OK telephone")
            else:
                reply4 = input("does it run an application? [Y/N]")
                if reply4 == 'Y' or reply4 == 'y':
                    print("OK tablet")
                else:
                    cvp5 = input("video çeker mi? [E/H]")
                    if reply5 == 'Y' or reply5 == 'y':
                        print("OK camera")
                    else:
                        reply6 = input("do you listen to music? [Y/N]")
                        if reply6 == 'Y' or reply6 == 'y':
                            print("OK radio")
                        else:
                            print("I don't know")

                        reply8 = input("do you watch the movie? [Y/N]")
                        if reply8 == 'Y' or reply8 == 'y':
                            print("OK tv")
                        else:
                            reply9 = input("white goods? [Y/N]")
                            if reply9 == 'Y' or reply9 == 'y':
                                replyX = input("does something wash? [Y/N]")
                                if replyX == 'Y' or replyX == 'y':
                                    replyXX = input("does it do laundry? [Y/N]")
                                    if replyXX == 'Y' or replyXX == 'y':
                                        print("OK washing machine")
                                    else:
                                        print("OK dishwasher")

                                    print("OK refrigerator")
                                else:
                                    print("you don't know")
