class EntertainmentIndustry(object):

    def music(self, a, b, c, d, album = 1500):
        sold = a  / album
        print('Albums sold: ', sold)
        strmrev = a * .005
        strmcut = strmrev * .25
        labelstrm = strmrev - strmcut
        print('Streams Revenue: ', labelstrm)
        radiocut = b * .25
        labelradio = b - radiocut
        print('Radio Revenue: ', labelradio)
        evntscut = c * .25
        labelevnts = c - evntscut
        print('Events Revenue: ', labelevnts)
        tourcut = d * .25
        labeltour = d - tourcut
        print('Tour Revenue: ', labeltour)
        totalrev = labelstrm + labelradio + labelevnts + labeltour
        print('Total Revenue for Year: ', totalrev)
        return totalrev

    def nfl(self, a, b, c, d, e, x, y, z):
        lgrevenue = 255000000
        teamrev = b + c + d + e + lgrevenue
        teamexp = x + y + z
        salarycap = teamrev - teamexp
        playeravg = salarycap / 55
        if a == 17:
            print('Player Salary: ', playeravg)
            return playeravg
        else:
            gameday = playeravg / 17
            raised = gameday * a
            print('Current Earnings: ', raised)
            return raised

    def nba(self, a, b, c, d, e, x, y, z):
        lgrevenue = 267000000
        teamrev = b + c + d + e + lgrevenue
        teamexp = x + y + z
        salarycap = teamrev - teamexp
        playeravg = salarycap / 15
        overallavg = playeravg + e
        print('Player Total Revenue: ', overallavg)
        return overallavg

class RealTime(object):

    def music(self, a, b, c, d, album = 1500):
        sold = a  / album
        print('Albums sold: ', sold)
        strmrev = a * .005
        strmcut = strmrev * .25
        labelstrm = strmrev - strmcut
        print('Streams Revenue: ', labelstrm)
        radiocut = b * .25
        labelradio = b - radiocut
        print('Radio Revenue: ', labelradio)
        evntscut = c * .25
        labelevnts = c - evntscut
        print('Events Revenue: ', labelevnts)
        tourcut = d * .25
        labeltour = d - tourcut
        print('Tour Revenue: ', labeltour)
        totalrev = labelstrm + labelradio + labelevnts + labeltour

        return totalrev

    def nfl(self, a, b, c, d, e, x, y, z):
        lgrevenue = 255000000
        teamrev = b + c + d + e + lgrevenue
        teamexp = x + y + z
        salarycap = teamrev - teamexp
        playeravg = salarycap / 55
        if a == 17:
            print('Player Salary: ', playeravg)
            return playeravg
        else:
            gameday = playeravg / 17
            raised = gameday * a
            print('Current Earnings: ', raised)
            return raised

    def nba(self, a, b, c, d, e, x, y, z):
        lgrevenue = 267000000
        teamrev = b + c + d + e + lgrevenue
        teamexp = x + y + z
        salarycap = teamrev - teamexp
        playeravg = salarycap / 15
        overallavg = playeravg + e
        print('Player Total Revenue: ', overallavg)
        return overallavg

if __name__ == '__main__':
    desired = EntertainmentIndustry()
    actual = RealTime()

    profession = (input("What is your entertaiment career? "))

    if profession == 'Music':
        streams = int(input("What is your goal amount of streams? "))
        radio = int(input("What is your goal amount of radio play? " ))
        events = int(input("What is your goal amount of money for events(awards, talk shows, short performances, etc.? "))
        tours = int(input("What is your goal amount of money for tours? " ))
        print("Expected Earnings and Salary")
        desired.music(streams, radio, events, tours)
        expected = desired.music(streams, radio, events, tours)
        curstreams = int(input("What are your current streams today? "))
        curradio = int(input("What are your current radio plays? "))
        curevents = int(input("How much have you generated from events performed? "))
        curtour = int(input("How much have you generated from trips on tour so far? "))
        print("Real-Time(Up-to_Date) Earnings and Salary")
        actual.music(curstreams, curradio, curevents, curtour)
        reality = actual.music(curstreams, curradio, curevents, curtour)
        comparison = expected - reality
        print("Difference between Expcted & Real-Time Earnings and Salary: ", comparison)
    elif profession == 'NFL':
        games = int(input("What is your goal amount of games? " ))
        tickets = float(input("What is your team's ticket sales? "))
        events = float(input("How much money raised from events at your team's stadium? " ))
        merch = float(input("How much money raised from merchandise sales? "))
        sponsors = int(input("How much money raised from sponsors? "))
        stadium = int(input("Stadium maintenance cost: "))
        marketing = int(input("Team marketing/promotion cost: "))
        franchise = int(input("Team's franchise fee: "))
        print("Expected Player Salary")
        desired.nfl(games, tickets, events, merch, sponsors, stadium, marketing, franchise)
        expected = desired.nfl(games, tickets, events, merch, sponsors, stadium, marketing, franchise)
        curgames = int(input("What is the current amount of games you've played in the season? "))
        print("Real-Time (Up-to-Date) Player Earnings")
        actual.nfl(curgames, tickets, events, merch, sponsors, stadium, marketing, franchise)
        reality = actual.nfl(curgames, tickets, events, merch, sponsors, stadium, marketing, franchise)
        comparison = expected - reality
        print("Difference between Expcted & Real-Time Earnings and Salary: ", comparison)
    elif profession == 'NBA':
        tickets = float(input("What is your team's ticket sales? "))
        events = float(input("How much money raised from events at your team's stadium? " ))
        merch = float(input("How much money raised from merchandise sales? "))
        sponsors = int(input("How much money raised from sponsors? "))
        endorsements = int(input("What is your goal amount of endorsement sales? "))
        arena = int(input("Arena maintenance cost: "))
        marketing = int(input("Team marketing/promotion cost: "))
        franchise = int(input("Team's franchise fee: "))
        print("Expected Player Salary")
        desired.nba(tickets, events, merch, sponsors, endorsements, arena, marketing, franchise)
        expected = desired.nba(tickets, events, merch, sponsors, endorsements, arena, marketing, franchise)
        curendorsements = int(input("What are your current endorsements? "))
        print("Real-Time (Up-to-Date) Player Earnings")
        actual.nba(tickets, events, merch, sponsors, curendorsements, arena, marketing, franchise)
        reality = actual.nba(tickets, events, merch, sponsors, curendorsements, arena, marketing, franchise)
        comparison = expected - reality
        print("Difference between Expcted & Real-Time Earnings and Salary: ", comparison)
    else:
        print("Career not found.")
