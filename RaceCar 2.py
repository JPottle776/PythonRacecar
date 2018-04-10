#########################
#
# RaceCar.py
#
# Author: Jamin Pottle Partner: Eugene
# Date: April 5, 2018
#
#########################

# imports
from random import *
import operator
import time

startRace = input("Welcome to the Indy 500!! To start type race, to leave type exit. ")
print("=====================================================")

def race():
    lapNum = 1
    lap = 0
    lapLength = 1
    
 #   inputLaps = input("Enter how many laps you would like to race. ")
    numLaps = 500
    numberOfLaps = 501
    
    racecar1Aver = {}
    racecar2Aver = {}
    racecar3Aver = {}
    racecar4Aver = {}
    racecar5Aver = {}
    racecar6Aver = {}
    racecar7Aver = {}
    racecar8Aver = {}
    racecar9Aver = {}
    racecar10Aver = {}
    racecar11Aver = {}
    racecar12Aver = {}
    racecar13Aver = {}
    racecar14Aver = {}
    racecar15Aver = {}
    racecar16Aver = {}
    racecar17Aver = {}
    racecar18Aver = {}
    racecar19Aver = {}
    racecar20Aver = {}
    racecar26Aver = {}
    allCarAver = {}

    totalTime1 = {}
    totalTime2 = {}
    totalTime3 = {}
    totalTime4 = {}
    totalTime5 = {}
    totalTime6 = {}
    totalTime7 = {}
    totalTime8 = {}
    totalTime9 = {}
    totalTime10 = {}
    totalTime11 = {}
    totalTime12 = {}
    totalTime13 = {}
    totalTime14 = {}
    totalTime15 = {}
    totalTime16 = {}
    totalTime17 = {}
    totalTime18 = {}
    totalTime19 = {}
    totalTime20 = {}
    totalTime26 = {}
    
    while(lapNum < numberOfLaps):
        
        
        while(lap < 1):
            #racers
            racecar1 = {"name":"Matt Kenseth", "sponser":"Dollar General", "num":"#01", "speed": randint(1,200)}
            racecar2 = {"name":"Kyle Busch", "sponser":"Skittles", "num":"#02", "speed": randint(1,200)}
            racecar3 = {"name":"Tim Flock", "sponser":"Ford", "num":"#03", "speed": randint(1,200)}
            racecar4 = {"name":"Mark Martin", "sponser":"Car Quest", "num":"#04", "speed": randint(1,200)}
            racecar5 = {"name":"Bill Elliott", "sponser":"Dodge", "num":"#05", "speed": randint(1,200)}
            racecar6 = {"name":"Buck Baker", "sponser":"Swift", "num":"#06", "speed": randint(1,200)}
            racecar7 = {"name":"Herb Thomas", "sponser":"Knight", "num":"#07", "speed": randint(1,200)}
            racecar8 = {"name":"Tony Stewart", "sponser":"Mobil 1", "num":"#08", "speed": randint(1,200)}
            racecar9 = {"name":"Junior Johnson", "sponser":"Pepsi", "num":"#09", "speed": randint(1,200)}
            racecar10 = {"name":"Ned Jarrett", "sponser":"Freightliner", "num":"#10", "speed": randint(1,200)}
            racecar11 = {"name":"Lee Petty", "sponser":"San Jaun Motors", "num":"#11", "speed": randint(1,200)}
            racecar12 = {"name":"Rusty Wallace", "sponser":"M&M", "num":"#12", "speed": randint(1,200)}
            racecar13 = {"name":"Dale Earnhardt", "sponser":"Circle K", "num":"#13", "speed": randint(1,200)}
            racecar14 = {"name":"Jimmie Johnson", "sponser":"Quick Trip", "num":"#14", "speed": randint(1,200)}
            racecar15 = {"name":"Cale Yarborough", "sponser":"7-Eleven", "num":"#15", "speed": randint(1,200)}
            racecar16 = {"name":"Darrell Waltrip", "sponser":"Tide", "num":"#16", "speed": randint(1,200)}
            racecar17 = {"name":"Bobby Allison", "sponser":"GoodYear", "num":"#17", "speed": randint(1,200)}
            racecar18 = {"name":"Jeff Gordon", "sponser":"AARP", "num":"#18", "speed": randint(1,200)}
            racecar19 = {"name":"David Pearson", "sponser":"Home Depot", "num":"#19", "speed": randint(1,200)}
            racecar20 = {"name":"Richard Petty", "sponser":"STP", "num":"#20", "speed": randint(1,200)}
            racecar26 = {"name":"Ricky Bobby", "sponser":"Wonder", "num":"#26", "speed": randint(1,200)}
            '''
            print("Lap:",lapNum)
            '''
            #print name and speed
            racecar1Time = 1 / racecar1["speed"] * 60 * 60
            racecar2Time = 1 / racecar2["speed"] * 60 * 60
            racecar3Time = 1 / racecar3["speed"] * 60 * 60
            racecar4Time = 1 / racecar4["speed"] * 60 * 60
            racecar5Time = 1 / racecar5["speed"] * 60 * 60
            racecar6Time = 1 / racecar6["speed"] * 60 * 60
            racecar7Time = 1 / racecar7["speed"] * 60 * 60
            racecar8Time = 1 / racecar8["speed"] * 60 * 60
            racecar9Time = 1 / racecar9["speed"] * 60 * 60
            racecar10Time = 1 / racecar10["speed"] * 60 * 60
            racecar11Time = 1 / racecar11["speed"] * 60 * 60
            racecar12Time = 1 / racecar12["speed"] * 60 * 60
            racecar13Time = 1 / racecar13["speed"] * 60 * 60
            racecar14Time = 1 / racecar14["speed"] * 60 * 60
            racecar15Time = 1 / racecar15["speed"] * 60 * 60
            racecar16Time = 1 / racecar16["speed"] * 60 * 60
            racecar17Time = 1 / racecar17["speed"] * 60 * 60
            racecar18Time = 1 / racecar18["speed"] * 60 * 60
            racecar19Time = 1 / racecar19["speed"] * 60 * 60
            racecar20Time = 1 / racecar20["speed"] * 60 * 60
            racecar26Time = 1 / racecar26["speed"] * 60 * 60
            
            '''
            print(racecar1["name"],"|", "speed:",racecar1["speed"],"mph","|", "time:", round(racecar1Time, 2),"sec")
            print(racecar2["name"],"|", "speed:",racecar2["speed"],"mph","|", "time:", round(racecar2Time, 2),"sec")
            print(racecar3["name"],"|", "speed:",racecar3["speed"],"mph","|", "time:", round(racecar3Time, 2),"sec")
            print(racecar4["name"],"|", "speed:",racecar4["speed"],"mph","|", "time:", round(racecar4Time, 2),"sec")
            print(racecar5["name"],"|", "speed:",racecar5["speed"],"mph","|", "time:", round(racecar5Time, 2),"sec")
            print(racecar6["name"],"|", "speed:",racecar6["speed"],"mph","|", "time:", round(racecar6Time, 2),"sec")
            print(racecar7["name"],"|", "speed:",racecar7["speed"],"mph","|", "time:", round(racecar7Time, 2),"sec")
            print(racecar8["name"],"|", "speed:",racecar8["speed"],"mph","|", "time:", round(racecar8Time, 2),"sec")
            print(racecar9["name"],"|", "speed:",racecar9["speed"],"mph","|", "time:", round(racecar9Time, 2),"sec")
            print(racecar10["name"],"|", "speed:",racecar10["speed"],"mph","|", "time:", round(racecar10Time, 2),"sec")
            print(racecar11["name"],"|", "speed:",racecar11["speed"],"mph","|", "time:", round(racecar11Time, 2),"sec")
            print(racecar12["name"],"|", "speed:",racecar12["speed"],"mph","|", "time:", round(racecar12Time, 2),"sec")
            print(racecar13["name"],"|", "speed:",racecar13["speed"],"mph","|", "time:", round(racecar13Time, 2),"sec")
            print(racecar14["name"],"|", "speed:",racecar14["speed"],"mph","|", "time:", round(racecar14Time, 2),"sec")
            print(racecar15["name"],"|", "speed:",racecar15["speed"],"mph","|", "time:", round(racecar15Time, 2),"sec")
            print(racecar16["name"],"|", "speed:",racecar16["speed"],"mph","|", "time:", round(racecar16Time, 2),"sec")
            print(racecar17["name"],"|", "speed:",racecar17["speed"],"mph","|", "time:", round(racecar17Time, 2),"sec")
            print(racecar18["name"],"|", "speed:",racecar18["speed"],"mph","|", "time:", round(racecar18Time, 2),"sec")
            print(racecar19["name"],"|", "speed:",racecar19["speed"],"mph","|", "time:", round(racecar19Time, 2),"sec")
            print(racecar20["name"],"|", "speed:",racecar20["speed"],"mph","|", "time:", round(racecar20Time, 2),"sec")
            print(racecar26["name"],"|", "speed:",racecar26["speed"],"mph","|", "time:", round(racecar26Time, 2),"sec")
            '''
            #push to car averages
            i = lapNum
            racecar1Aver[str(i)] = racecar1["speed"]
            racecar2Aver[str(i)] = racecar2["speed"]
            racecar3Aver[str(i)] = racecar3["speed"]
            racecar4Aver[str(i)] = racecar4["speed"]
            racecar5Aver[str(i)] = racecar5["speed"]
            racecar6Aver[str(i)] = racecar6["speed"]
            racecar7Aver[str(i)] = racecar7["speed"]
            racecar8Aver[str(i)] = racecar8["speed"]
            racecar9Aver[str(i)] = racecar9["speed"]
            racecar10Aver[str(i)] = racecar10["speed"]
            racecar11Aver[str(i)] = racecar11["speed"]
            racecar12Aver[str(i)] = racecar12["speed"]
            racecar13Aver[str(i)] = racecar13["speed"]
            racecar14Aver[str(i)] = racecar14["speed"]
            racecar15Aver[str(i)] = racecar15["speed"]
            racecar16Aver[str(i)] = racecar16["speed"]
            racecar17Aver[str(i)] = racecar17["speed"]
            racecar18Aver[str(i)] = racecar18["speed"]
            racecar19Aver[str(i)] = racecar19["speed"]
            racecar20Aver[str(i)] = racecar20["speed"]
            racecar26Aver[str(i)] = racecar26["speed"]

            #pushes time per lap into another varibale
            totalTime1[str(i)] = round(racecar1Time, 2)
            totalTime2[str(i)] = round(racecar2Time, 2)
            totalTime3[str(i)] = round(racecar3Time, 2)
            totalTime4[str(i)] = round(racecar4Time, 2)
            totalTime5[str(i)] = round(racecar5Time, 2)
            totalTime6[str(i)] = round(racecar6Time, 2)
            totalTime7[str(i)] = round(racecar7Time, 2)
            totalTime8[str(i)] = round(racecar8Time, 2)
            totalTime9[str(i)] = round(racecar9Time, 2)
            totalTime10[str(i)] = round(racecar10Time, 2)
            totalTime11[str(i)] = round(racecar11Time, 2)
            totalTime12[str(i)] = round(racecar12Time, 2)
            totalTime13[str(i)] = round(racecar13Time, 2)
            totalTime14[str(i)] = round(racecar14Time, 2)
            totalTime15[str(i)] = round(racecar15Time, 2)
            totalTime16[str(i)] = round(racecar16Time, 2)
            totalTime17[str(i)] = round(racecar17Time, 2)
            totalTime18[str(i)] = round(racecar18Time, 2)
            totalTime19[str(i)] = round(racecar19Time, 2)
            totalTime20[str(i)] = round(racecar20Time, 2)
            totalTime26[str(i)] = round(racecar26Time, 2)
            
            
            
            #print("=====================================================")
            lap += 1
        lapNum += 1
        lap = 0
        if(lapNum == numberOfLaps):
            print("=====================================================")
            print("Results of race")
            print("")
            print(numLaps,"Laps")
            if(numLaps == 1):
                print(numLaps,"Lap")
            print("")

            #Gets the sum and averages the speed for each racer
            Aver1 = sum(racecar1Aver.values()) / numLaps
            Aver2 = sum(racecar2Aver.values()) / numLaps
            Aver3 = sum(racecar3Aver.values()) / numLaps
            Aver4 = sum(racecar4Aver.values()) / numLaps
            Aver5 = sum(racecar5Aver.values()) / numLaps
            Aver6 = sum(racecar6Aver.values()) / numLaps
            Aver7 = sum(racecar7Aver.values()) / numLaps
            Aver8 = sum(racecar8Aver.values()) / numLaps
            Aver9 = sum(racecar9Aver.values()) / numLaps
            Aver10 = sum(racecar10Aver.values()) / numLaps
            Aver11 = sum(racecar11Aver.values()) / numLaps
            Aver12 = sum(racecar12Aver.values()) / numLaps
            Aver13 = sum(racecar11Aver.values()) / numLaps
            Aver14 = sum(racecar14Aver.values()) / numLaps
            Aver15 = sum(racecar15Aver.values()) / numLaps
            Aver16 = sum(racecar16Aver.values()) / numLaps
            Aver17 = sum(racecar17Aver.values()) / numLaps
            Aver18 = sum(racecar18Aver.values()) / numLaps
            Aver19 = sum(racecar19Aver.values()) / numLaps
            Aver20 = sum(racecar20Aver.values()) / numLaps
            Aver26 = sum(racecar26Aver.values()) / numLaps
            allCarAver = {float(Aver1), float(Aver2), float(Aver3), float(Aver4), float(Aver5), float(Aver6), float(Aver7), float(Aver8), float(Aver9), float(Aver10), float(Aver11), float(Aver12), float(Aver13), float(Aver14), float(Aver15), float(Aver16), float(Aver17), float(Aver18), float(Aver19), float(Aver20), float(Aver26)}
            sortCarPlace = {}

            raceTime1 = round(round(sum(totalTime1.values()), 2) / 60 / 60, 2)
            raceTime2 = round(round(sum(totalTime2.values()), 2) / 60 / 60, 2)
            raceTime3 = round(round(sum(totalTime3.values()), 2) / 60 / 60, 2)
            raceTime4 = round(round(sum(totalTime4.values()), 2) / 60 / 60, 2)
            raceTime5 = round(round(sum(totalTime5.values()), 2) / 60 / 60, 2)
            raceTime6 = round(round(sum(totalTime6.values()), 2) / 60 / 60, 2)
            raceTime7 = round(round(sum(totalTime7.values()), 2) / 60 / 60, 2)
            raceTime8 = round(round(sum(totalTime8.values()), 2) / 60 / 60, 2)
            raceTime9 = round(round(sum(totalTime9.values()), 2) / 60 / 60, 2)
            raceTime10 = round(round(sum(totalTime10.values()), 2) / 60 / 60, 2)
            raceTime11 = round(round(sum(totalTime11.values()), 2) / 60 / 60, 2)
            raceTime12 = round(round(sum(totalTime12.values()), 2) / 60 / 60, 2)
            raceTime13 = round(round(sum(totalTime13.values()), 2) / 60 / 60, 2)
            raceTime14 = round(round(sum(totalTime14.values()), 2) / 60 / 60, 2)
            raceTime15 = round(round(sum(totalTime15.values()), 2) / 60 / 60, 2)
            raceTime16 = round(round(sum(totalTime16.values()), 2) / 60 / 60, 2)
            raceTime17 = round(round(sum(totalTime17.values()), 2) / 60 / 60, 2)
            raceTime18 = round(round(sum(totalTime18.values()), 2) / 60 / 60, 2)
            raceTime19 = round(round(sum(totalTime19.values()), 2) / 60 / 60, 2)
            raceTime20 = round(round(sum(totalTime20.values()), 2) / 60 / 60, 2)
            raceTime26 = round(round(sum(totalTime26.values()), 2) / 60 / 60, 2)

            racecar1[5] = round(round(sum(totalTime1.values()), 2) / 60 / 60, 2)
            racecar2[5] = round(round(sum(totalTime2.values()), 2) / 60 / 60, 2)
            racecar3[5] = round(round(sum(totalTime3.values()), 2) / 60 / 60, 2)
            racecar4[5] = round(round(sum(totalTime4.values()), 2) / 60 / 60, 2)
            racecar5[5] = round(round(sum(totalTime5.values()), 2) / 60 / 60, 2)
            racecar6[5] = round(round(sum(totalTime6.values()), 2) / 60 / 60, 2)
            racecar7[5] = round(round(sum(totalTime7.values()), 2) / 60 / 60, 2)
            racecar8[5] = round(round(sum(totalTime8.values()), 2) / 60 / 60, 2)
            racecar9[5] = round(round(sum(totalTime9.values()), 2) / 60 / 60, 2)
            racecar10[5] = round(round(sum(totalTime10.values()), 2) / 60 / 60, 2)
            racecar11[5] = round(round(sum(totalTime11.values()), 2) / 60 / 60, 2)
            racecar12[5] = round(round(sum(totalTime12.values()), 2) / 60 / 60, 2)
            racecar13[5] = round(round(sum(totalTime13.values()), 2) / 60 / 60, 2)
            racecar14[5] = round(round(sum(totalTime14.values()), 2) / 60 / 60, 2)
            racecar15[5] = round(round(sum(totalTime15.values()), 2) / 60 / 60, 2)
            racecar16[5] = round(round(sum(totalTime16.values()), 2) / 60 / 60, 2)
            racecar17[5] = round(round(sum(totalTime17.values()), 2) / 60 / 60, 2)
            racecar18[5] = round(round(sum(totalTime18.values()), 2) / 60 / 60, 2)
            racecar19[5] = round(round(sum(totalTime19.values()), 2) / 60 / 60, 2)
            racecar20[5] = round(round(sum(totalTime20.values()), 2) / 60 / 60, 2)
            racecar26[5] = round(round(sum(totalTime26.values()), 2) / 60 / 60, 2)
            
            #Prints each racers lap average in mph and the total time it took to race
            print(racecar1["name"],"lap average:",Aver1,"mph","|", raceTime1,"hours")
            print(racecar2["name"],"lap average:",Aver2,"mph","|", raceTime2,"hours")
            print(racecar3["name"],"lap average:",Aver3,"mph","|", raceTime3,"hours")
            print(racecar4["name"],"lap average:",Aver4,"mph","|", raceTime4,"hours")
            print(racecar5["name"],"lap average:",Aver5,"mph","|", raceTime5,"hours")
            print(racecar6["name"],"lap average:",Aver6,"mph","|", raceTime6,"hours")
            print(racecar7["name"],"lap average:",Aver7,"mph","|", raceTime7,"hours")
            print(racecar8["name"],"lap average:",Aver8,"mph","|", raceTime8,"hours")
            print(racecar9["name"],"lap average:",Aver9,"mph","|", raceTime9,"hours")
            print(racecar10["name"],"lap average:",Aver10,"mph","|", raceTime10,"hours")
            print(racecar11["name"],"lap average:",Aver11,"mph","|", raceTime11,"hours")
            print(racecar12["name"],"lap average:",Aver12,"mph","|", raceTime12,"hours")
            print(racecar13["name"],"lap average:",Aver13,"mph","|", raceTime13,"hours")
            print(racecar14["name"],"lap average:",Aver14,"mph","|", raceTime14,"hours")
            print(racecar15["name"],"lap average:",Aver15,"mph","|", raceTime15,"hours")
            print(racecar16["name"],"lap average:",Aver16,"mph","|", raceTime16,"hours")
            print(racecar17["name"],"lap average:",Aver17,"mph","|", raceTime17,"hours")
            print(racecar18["name"],"lap average:",Aver18,"mph","|", raceTime18,"hours")
            print(racecar19["name"],"lap average:",Aver19,"mph","|", raceTime19,"hours")
            print(racecar20["name"],"lap average:",Aver20,"mph","|", raceTime20,"hours")
            print(racecar26["name"],"lap average:",Aver26,"mph","|", raceTime26,"hours")
            allTimeTotals = [float(raceTime1), float(raceTime2), float(raceTime3), float(raceTime4), float(raceTime5), float(raceTime6), float(raceTime7), float(raceTime8), float(raceTime9), float(raceTime10), float(raceTime11), float(raceTime12), float(raceTime13), float(raceTime14), float(raceTime15), float(raceTime16), float(raceTime17), float(raceTime18), float(raceTime19), float(raceTime20)]
 #           print(sorted(racecar26Aver.values()))
 #           sortCarPlace = sorted(allCarAver)
            #print(sortCarPlace)
            print("=====================================================")
            print("=====================================================")
            sortAllTimeTotals = sorted(allTimeTotals)
#            print(sortAllTimeTotals)
            if(sortAllTimeTotals[0] == racecar1[5]):
                print("The winner is:",racecar1["num"],racecar1["name"],"|","sponser:",racecar1["sponser"],"|","Time:",racecar1[5],"hours","|","Average speed:",Aver1,"mph")
            if(sortAllTimeTotals[0] == racecar2[5]):
                print("The winner is:",racecar2["num"],racecar2["name"],"|","sponser:",racecar2["sponser"],"|","Time:",racecar2[5],"hours","|","Average speed:",Aver2,"mph")
            if(sortAllTimeTotals[0] == racecar3[5]):
                print("The winner is:",racecar3["num"],racecar3["name"],"|","sponser:",racecar3["sponser"],"|","Time:",racecar3[5],"hours","|","Average speed:",Aver3,"mph")
            if(sortAllTimeTotals[0] == racecar4[5]):
                print("The winner is:",racecar4["num"],racecar4["name"],"|","sponser:",racecar4["sponser"],"|","Time:",racecar4[5],"hours","|","Average speed:",Aver4,"mph")
            if(sortAllTimeTotals[0] == racecar5[5]):
                print("The winner is:",racecar5["num"],racecar5["name"],"|","sponser:",racecar5["sponser"],"|","Time:",racecar5[5],"hours","|","Average speed:",Aver5,"mph")
            if(sortAllTimeTotals[0] == racecar6[5]):
                print("The winner is:",racecar6["num"],racecar6["name"],"|","sponser:",racecar6["sponser"],"|","Time:",racecar6[5],"hours","|","Average speed:",Aver6,"mph")
            if(sortAllTimeTotals[0] == racecar7[5]):
                print("The winner is:",racecar7["num"],racecar7["name"],"|","sponser:",racecar7["sponser"],"|","Time:",racecar7[5],"hours","|","Average speed:",Aver7,"mph")
            if(sortAllTimeTotals[0] == racecar8[5]):
                print("The winner is:",racecar8["num"],racecar8["name"],"|","sponser:",racecar8["sponser"],"|","Time:",racecar8[5],"hours","|","Average speed:",Aver8,"mph")
            if(sortAllTimeTotals[0] == racecar9[5]):
                print("The winner is:",racecar9["num"],racecar9["name"],"|","sponser:",racecar9["sponser"],"|","Time:",racecar9[5],"hours","|","Average speed:",Aver9,"mph")
            if(sortAllTimeTotals[0] == racecar10[5]):
                print("The winner is:",racecar10["num"],racecar10["name"],"|","sponser:",racecar10["sponser"],"|","Time:",racecar10[5],"hours","|","Average speed:",Aver10,"mph")
            if(sortAllTimeTotals[0] == racecar11[5]):
                print("The winner is:",racecar11["num"],racecar11["name"],"|","sponser:",racecar11["sponser"],"|","Time:",racecar11[5],"hours","|","Average speed:",Aver11,"mph")
            if(sortAllTimeTotals[0] == racecar12[5]):
                print("The winner is:",racecar12["num"],racecar12["name"],"|","sponser:",racecar12["sponser"],"|","Time:",racecar12[5],"hours","|","Average speed:",Aver12,"mph")
            if(sortAllTimeTotals[0] == racecar13[5]):
                print("The winner is:",racecar13["num"],racecar13["name"],"|","sponser:",racecar13["sponser"],"|","Time:",racecar13[5],"hours","|","Average speed:",Aver13,"mph")
            if(sortAllTimeTotals[0] == racecar14[5]):
                print("The winner is:",racecar14["num"],racecar14["name"],"|","sponser:",racecar14["sponser"],"|","Time:",racecar14[5],"hours","|","Average speed:",Aver14,"mph")
            if(sortAllTimeTotals[0] == racecar15[5]):
                print("The winner is:",racecar15["num"],racecar15["name"],"|","sponser:",racecar15["sponser"],"|","Time:",racecar15[5],"hours","|","Average speed:",Aver15,"mph")
            if(sortAllTimeTotals[0] == racecar16[5]):
                print("The winner is:",racecar16["num"],racecar16["name"],"|","sponser:",racecar16["sponser"],"|","Time:",racecar16[5],"hours","|","Average speed:",Aver16,"mph")
            if(sortAllTimeTotals[0] == racecar17[5]):
                print("The winner is:",racecar17["num"],racecar17["name"],"|","sponser:",racecar17["sponser"],"|","Time:",racecar17[5],"hours","|","Average speed:",Aver17,"mph")
            if(sortAllTimeTotals[0] == racecar18[5]):
                print("The winner is:",racecar18["num"],racecar18["name"],"|","sponser:",racecar18["sponser"],"|","Time:",racecar18[5],"hours","|","Average speed:",Aver18,"mph")
            if(sortAllTimeTotals[0] == racecar19[5]):
                print("The winner is:",racecar19["num"],racecar19["name"],"|","sponser:",racecar19["sponser"],"|","Time:",racecar19[5],"hours","|","Average speed:",Aver19,"mph")
            if(sortAllTimeTotals[0] == racecar20[5]):
                print("The winner is:",racecar20["num"],racecar20["name"],"|","sponser:",racecar20["sponser"],"|","Time:",racecar20[5],"hours","|","Average speed:",Aver20,"mph")
            if(sortAllTimeTotals[0] == racecar26[5]):
                print("The winner is:",racecar26["num"],racecar26["name"],"|","sponser:",racecar26["sponser"],"|","Time:",racecar26[5],"hours","|","Average speed:",Aver26,"mph")
    
        
    
if(startRace == "race"):
    race()
    
