import itertools as it
import time
from itertools import combinations
import re

Mia = 1610612748
Mem = 1610612763
Gsw = 1610612744
Jaz = 1610612762
Pho = 1610612756
Bos = 1610612738
Den = 1610612743
Mil = 1610612749
Min = 1610612750
Chi = 1610612741
Phi = 1610612755
Atl = 1610612737
Por = 1610612757
Nop = 1610612740
Okc = 1610612760
Sas = 1610612759
Lal = 1610612747
Dal = 1610612742
Bkn = 1610612751
Cle = 1610612739
Cha = 1610612766
Sac = 1610612758
Ind = 1610612754
Orl = 1610612753
Lac = 1610612746
Nyk = 1610612752
Tor = 1610612761
Det = 1610612765
Hou = 1610612745
Was = 1610612764

atl_p = [1629027, 203991, 1626153]
bos_p = [1628369, 1629057, 201143]
bkn_p = [201142, 201935, 202681, 1628971]
cha_p = [1630163, 1628970, 1626179]
chi_p = [201942, 203897, 202696]
cle_p = [1629636, 1628386, 201567]
dal_p = [1629029, 1628973, 1627827]
den_p = [203999, 1628420, 203932]
det_p = [1630180, 203924, 203482]
gsw_p = [201939, 1627780, 203490]
hou_p = [1626174, 1630231, 1630578]
ind_p = [1627734, 1627763, 1626167]
lac_p = [1628392, 201587, 202331]
lal_p = [2544, 203076, 1628370]
mem_p = [1629630, 1630217, 203500]
mia_p = [202710, 1628389, 200768]
mil_p = [203507, 201950, 203114]
min_p = [1626157, 1630162, 201976]
nop_p = [202685, 1627742, 203468]
nyk_p = [1629011, 202692, 203944]
okc_p = [1628983, 203488, 1629676]
orl_p = [1628976, 1628964, 1629021]
phi_p = [203954, 1630178, 202699]
pho_p = [101108, 1626164, 1628969]
por_p = [203994, 203081, 203468]
sac_p = [1630169, 203084, 1628368]
sas_p = [1627749, 1627751, 1628401]
tor_p = [1627783, 1627832, 1630567]
jaz_p = [203497, 1628378, 201144]
was_p = [1626149, 1629655, 1628398]


#bkn_p
player_ids = [atl_p, bos_p, bkn_p, cha_p, chi_p, cle_p, dal_p, den_p, det_p, gsw_p, hou_p, ind_p, lac_p, lal_p, mem_p, mia_p, mil_p, min_p, nop_p, nyk_p, okc_p, orl_p, phi_p, pho_p, por_p, sac_p, sas_p, tor_p, jaz_p, was_p]
#Bkn
# I may have deleted it by accident, but double check that you have Hou in your array
# all the things have to line up for this to work :)
teams = [Atl, Bos, Bkn, Cha, Chi, Cle, Dal, Den, Det, Gsw, Hou, Ind, Lac, Lal, Mem, Mia, Mil, Min, Nop, Nyk, Okc, Orl, Phi, Pho, Por, Sac, Sas, Tor, Jaz, Was]

url_start = "https://www.pbpstats.com/wowy/nba?0Exactly2OffFloor={}&1Exactly2PlayedInGame={}&TeamId={}&Season=2021-22&SeasonType=Regular%20Season&Type=Player&Table=Scoring&StatType=Totals"

# initialize empty array variable
play_combo = []
# get all possible player combinations - basically [[1,2], [2,3], [1,3]]
for play in player_ids:
    play_combo.append(list(combinations(play, 2)))
# just prints info to see what we're getting from play_combo
print(list(play_combo), len(play_combo), len(teams), len(player_ids))


def get_All_Combos(players, teams, t_counter=0, p_counter=0):
    """ first checks to see if our t_counter is greater than or equal to the length of
        the 'teams' array.  If it is, then it stops the recursion and returns all of
        the information we have gathered from the stack.
        
        Otherwise:
        gets the teamID (I called it teamName and just never changed it) using the
        t_counter which is defaulted at 0, but gets +1 every time we recurse 
        (call get_All_Combos again).  same is true for p_counter
        we loop through the players parameter (which is play_combo array) and since each 
        item in play_combo is an array too, we have to use p_counter to make sure that
        we loop through the items so they line up with which team we are on with
        t_counter.
        
        Finally, each time we loop, we generate a new url.
        I'll leave the rest to you :) good luck!
        """
    if (t_counter >= len(teams)):
        return
    else:
        teamName = f"{teams[t_counter]}"
        for p in players[p_counter]:
            combo = f"{p[0]},{p[1]}"
            url = url_start.format(combo, combo, teamName)
            print(teamName, combo, p_counter)
            print(url)
        p_counter += 1
        t_counter += 1
        get_All_Combos(players, teams, t_counter, p_counter)

get_All_Combos(play_combo, teams)