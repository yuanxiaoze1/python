import  random
def single_game(pa,pb,scoreslimit):
    scoreA,scoreB=0,0
    while scoreA<scoreslimit and scoreB<scoreslimit:
        if random.random()<pa:
            scoreA+=1
        else:
            scoreB+=1
    if scoreA>scoreB: return 'A'
    else: return 'B'
def get_prob(pa,pb,scoreslimit,n):
    while pa<0 or pa>1:
        pa=float(input("Enter the probability of player A winning a point:(0-1)"))
    while pb+pa !=1:
        pb=float(input("Identify the probability of player B winning a point:(1-pa)"))
    while scoreslimit<0:
        scoreslimit=int(input("Enter the score limit:"))
    while n<0:
        n=int(input("Enter the number of games:"))
    return pa,pb,scoreslimit,n
def play_games(pa,pb,scoreslimit,n):
    winsA,winsB=0,0
    for i in range(n):
        winner=single_game(pa,pb,scoreslimit)
        if winner=='A': winsA+=1
        else: winsB+=1
    print('Player A won',winsA,'and Player B won',winsB)
    print('The probability of Player A winning is',winsA/n)
    print('The probability of Player B winning is',winsB/n)
def main():
    pa,pb,scoreslimit,n=-1,-1,-1,-1
    pa,pb,scoreslimit,n=get_prob(pa,pb,scoreslimit,n)
    play_games(pa,pb,scoreslimit,n)


    
    