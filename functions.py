import streamlit as st
from operator import itemgetter

def day_min_from_total(total_mins):
    days = total_mins // (24 * 60)
    mins = total_mins % (24 * 60)

    return days, mins

def total_mins_from_time(days, hours, minutes, seconds):
    total_mins = days * 24 * 60 + hours * 60 + minutes + seconds/60

    return total_mins

def get_bag_min(speedup_type):
    speed_up_5 = st.number_input('5 min {}'.format(speedup_type), 0)
    speed_up_10 = st.number_input('10 min {}'.format(speedup_type), 0)
    speed_up_15 = st.number_input('15 min {}'.format(speedup_type), 0)
    speed_up_30 = st.number_input('30 min {}'.format(speedup_type), 0)
    speed_up_60 = st.number_input('60 min {}'.format(speedup_type), 0)
    speed_up_3h = st.number_input('3 h {}'.format(speedup_type), 0)
    speed_up_8h = st.number_input('8 h {}'.format(speedup_type), 0)
    speed_up_15h = st.number_input('15 h {}'.format(speedup_type), 0)
    speed_up_24h = st.number_input('24 h {}'.format(speedup_type), 0)
    speed_up_3d = st.number_input('3 days {}'.format(speedup_type), 0)
    speed_up_7d = st.number_input('7 days {}'.format(speedup_type), 0)

    total_mins = speed_up_5*5 + speed_up_10*10 + speed_up_15*15 + speed_up_30*30 + speed_up_60*60 + 60*(speed_up_3h*3 + speed_up_8h*8 + speed_up_15h*15 + speed_up_24h*24) + 24*60*(speed_up_3d*3 + speed_up_7d*7)

    days, mins = day_min_from_total(total_mins)

    return total_mins, days, mins

def total_time(min5=0, min10=0, min15=0, min30=0, min60=0, hour3=0, hour8=0, hour15=0, hour24=0, day3=0, day7=0) :
    total_mins = min5*5 + min10*10 + min15*15 + min30*30 + min60*60 + 60*(hour3*3 + hour8*8 + hour15*15 + hour24*24) + 24*60*(day3*3 + day7*7)

    days = total_mins // (24 * 60)
    mins = total_mins % (24 * 60)

    return total_mins, days, mins

def write_min_recap(speed_up_type, total_mins, days, mins) :
    st.write("Minutes from {} speedup minutes in your bag : {}.".format(speed_up_type, total_mins))
    st.write("Being {} day{}, {} hour{}, {} min.".format(
        days, 
        's' if days > 1 else '',
        int(mins // 60), 
        's' if (int(mins//60)) >1 else '',
        mins%60))

def developpement_points(might):
    return might*5

def boosting_points(total_mins):
    return total_mins*15

def gear_points(gear_spin = 0, gear_ess_1 = 0, gear_ess_2 = 0, gear_ess_3 = 0, gear_ess_4 = 0, gear_ess_5 = 0, gear_prom_8 = 0, pts_spin = 1000, pts_ess_1 = 100, pts_ess_2 = 500, pts_ess_3 = 2000, pts_ess_4 = 5000, pts_ess_5 = 20000, pts_prom_8 = 20000):
    
    gears = [gear_spin, gear_ess_1, gear_ess_2, gear_ess_3, gear_ess_4, gear_ess_5, gear_prom_8]
    points = [pts_spin, pts_ess_1, pts_ess_2, pts_ess_3, pts_ess_4, pts_ess_5, pts_prom_8]
    
    total_points = 0
    
    for gear, point in zip(gears, points) :
        total_points += gear*point
        
    return total_points

def sum_dict(list_of_dict):
    new_dict = {}

    for d in list_of_dict:
        for k in d.keys():
            new_dict[k] = new_dict.get(k, 0) + d[k]

    return new_dict

def chest_rss(type_chest, rss_amt, rss_str, amt_current):
    '''
    type_chest = string
    rss_amt = dictionnaire avec qté possible pour food, wood, iron, gold dans le coffre
    rss_str = dictionnaire avec string pour food, wood, iron, gold
    '''

    total_chests = st.number_input(f"{type_chest} in bag", 0)

    if total_chests > 0 :
        
        food_chests = st.slider(f"{type_chest} converted to Food", min_value=0, max_value=total_chests)
        chests_left_1 = total_chests - food_chests

        wood_chests = st.slider(f"{type_chest} converted to Wood", min_value=0, max_value=chests_left_1) if chests_left_1 > 0 else 0
        chests_left_2 = chests_left_1 - wood_chests
        
        
        iron_chests = st.slider(f"{type_chest} converted to Iron", min_value=0, max_value=chests_left_2) if chests_left_2 > 0 else 0
        chests_left_3 = chests_left_2 - iron_chests
        

        gold_chests = st.slider(f"{type_chest} converted to Gold", min_value=0, max_value=chests_left_3) if chests_left_3 > 0 else 0
        chests_left_4 = chests_left_3 - gold_chests
        
        
        st.write(f"Chests left : {chests_left_4}.")

        rss_qty = {
            'food' : food_chests * rss_amt["food"],
            'wood' : wood_chests * rss_amt["wood"],
            'iron' : iron_chests * rss_amt["iron"],
            'gold' : gold_chests * rss_amt["gold"],
        }

        new_current = sum_dict([amt_current, rss_qty])

        st.write(f"*Total from {type_chest}*")
        st.write("{} {:,} - {:,} cumulated.".format(rss_str["food"], rss_qty['food'], new_current['food']))
        st.write("{} {:,} - {:,} cumulated.".format(rss_str["wood"], rss_qty['wood'], new_current['wood']))
        st.write("{} {:,} - {:,} cumulated.".format(rss_str["iron"], rss_qty['iron'], new_current['iron']))
        st.write("{} {:,} - {:,} cumulated.".format(rss_str["gold"], rss_qty['gold'], new_current['gold']))  

        return rss_qty, new_current
    
    else :
        return {}, amt_current

def saurgem_rare_earth_shop(rare_earth_coins, rare_price_essence, rare_max_essence, essence_pts):

    if rare_earth_coins > 0:
        rare_essence = rare_earth_coins // rare_price_essence
        if rare_essence > rare_max_essence :
            rare_essence = rare_max_essence
        rare_essence_pts = rare_essence * essence_pts
        rare_earth_coins = rare_earth_coins - rare_essence * rare_price_essence
    else :
        rare_essence = 0
        rare_essence_pts = 0

    return rare_essence, rare_essence_pts, rare_earth_coins
    
    
