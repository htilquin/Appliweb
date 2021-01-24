# to run : streamlit run calcultor.py

import streamlit as st
import numpy as np

st.title("# MOK Calculator !")

@st.cache
def boosting_time(min5=0, min10=0, min15=0, min30=0, min60=0, hour3=0, hour8=0, hour15=0, hour24=0, day3=0, day7=0):
    
    total_mins = min5*5 + min10*10 + min15*15 + min30*30 + min60*60 + 60*(hour3*3 + hour8*8 + hour15*15 + hour24*24) + 24*60*(day3*3 + day7*7)
    # print("Total minutes : ", total_mins)
    days = total_mins // (24 * 60)
    mins = total_mins % (24 * 60)
    
    # print("Total : {} days, {} hours, {} min.".format(days, int(mins // 60), mins%60))
    # print("Total points : {}".format(total_mins*15))
    total_points = total_mins*15

    return total_mins, days, mins, total_points

# Regular / Research / Training / Building

st.write("Select the event you want with the checkbox. Please remember that if you uncheck an event, all the information you entered will be lost.")

if st.checkbox("Speedup event") :

    st.write("You've kept all your speedups for this event : **awesome** ! But is it worth spending them all ?")  

    st.write("First, let's have a look in your bag (I promise I won't tell anyone) !")
    st.markdown("### Regular speedup items in your bag")

    reg_5 = st.number_input('5 min regular', 0)
    reg_10 = st.number_input('10 min regular', 0)
    reg_15 = st.number_input('15 min regular', 0)
    reg_30 = st.number_input('30 min regular', 0)
    reg_60 = st.number_input('60 min regular', 0)
    reg_3h = st.number_input('3 h regular', 0)
    reg_8h = st.number_input('8 h regular', 0)
    reg_15h = st.number_input('15 h regular', 0)
    reg_24h = st.number_input('24 h regular', 0)
    reg_3d = st.number_input('3 days regular', 0)
    reg_7d = st.number_input('7 days regular', 0)

    st.write()

    st.markdown("### Research speedup items in your bag")

    search_5 = st.number_input('5 min research', 0)
    search_10 = st.number_input('10 min research', 0)
    search_15 = st.number_input('15 min research', 0)
    search_30 = st.number_input('30 min research', 0)
    search_60 = st.number_input('60 min research', 0)
    search_3h = st.number_input('3 h research', 0)
    search_8h = st.number_input('8 h research', 0)
    search_15h = st.number_input('15 h research', 0)
    search_24h = st.number_input('24 h research', 0)
    search_3d = st.number_input('3 days research', 0)
    search_7d = st.number_input('7 days research', 0)

    st.markdown("### Training speedup items in your bag")

    train_5 = st.number_input('5 min train', 0)
    train_10 = st.number_input('10 min train', 0)
    train_15 = st.number_input('15 min train', 0)
    train_30 = st.number_input('30 min train', 0)
    train_60 = st.number_input('60 min train', 0)
    train_3h = st.number_input('3 h train', 0)
    train_8h = st.number_input('8 h train', 0)
    train_15h = st.number_input('15 h train', 0)
    train_24h = st.number_input('24 h train', 0)
    train_3d = st.number_input('3 days train', 0)
    train_7d = st.number_input('7 days train', 0)

    st.markdown("### Building speedup items in your bag")

    build_5 = st.number_input('5 min building', 0)
    build_10 = st.number_input('10 min building', 0)
    build_15 = st.number_input('15 min building', 0)
    build_30 = st.number_input('30 min building', 0)
    build_60 = st.number_input('60 min building', 0)
    build_3h = st.number_input('3 h building', 0)
    build_8h = st.number_input('8 h building', 0)
    build_15h = st.number_input('15 h building', 0)
    build_24h = st.number_input('24 h building', 0)
    build_3d = st.number_input('3 days building', 0)
    build_7d = st.number_input('7 days building', 0)


    min5 = reg_5 + search_5 + train_5 + build_5
    min10 = reg_10 + search_10 + train_10 + build_10
    min15 = reg_15 + search_15 + train_15 + build_15
    min30 = reg_30 + search_30 + train_30 + build_30
    min60 = reg_60 + search_60 + train_60 + build_60
    hour3 = reg_3h + search_3h + train_3h + build_3h
    hour8 = reg_8h + search_8h + train_8h + build_8h
    hour15 = reg_15h + search_15h + train_15h + build_15h
    hour24 = reg_24h + search_24h + train_24h + build_24h
    day3 = reg_3d + search_3d + train_3d + build_3d
    day7 = reg_7d + search_7d + train_7d + build_7d

    total_mins, days, mins, total_points = boosting_time(min5, min10, min15, min30, min60, hour3, hour8, hour15, hour24, day3, day7)

    st.markdown("-")
    st.write("Total speedup minutes in your bag : {}.".format(total_mins))
    st.write("Being {} day{}, {} hour{}, {} min.".format(
        days, 
        's' if days > 1 else '',
        int(mins // 60), 
        's' if (int(mins//60)) >1 else '',
        mins%60))
    st.markdown("-")
    st.write("Total points you will get *if you use all your speedups* : {}.".format(total_mins*15))

    st.write("What are you aiming to achieve ?")
    objective = st.number_input('Objective of points', 0)
    current_points = st.number_input('Current points', 0)
    diff = objective - current_points
    if diff > 0 :
        st.write("You are {} point{} away from your objective, being {} minute{} of speedups.".format(
            diff, 
            's' if diff > 1 else '',
            (diff+14)//15,
            's' if ((diff+14)//15) > 1 else ''))
    else :
        st.write("Seems like you have already fulfilled your objective ;)")

    total_points = total_mins*15 + current_points
    diff_2 = objective - total_points

    st.write("Which would make, including your current poins : {}".format(total_points))
    if diff_2 > 0 :
        st.write("You would still need {} point{} to get to your objective, equivalent to {} more minute{} of speed-ups.".format(
            diff_2,
            's' if diff_2 > 1 else '',
            (diff_2+14)//15,
            's' if ((diff_2+14)//15) > 1 else ''
        ))
    st.write()

    st.markdown("-")

    st.write("Not enough? You can also buy 60-min speedups in *Hero Arena Shop* : 1 item for 300 coins, and from *Trial Shop* : 1 item for 12 coins, max 99.")
    arena_coins = st.number_input('Hero Arena Coins in bag', 0)
    st.write("Potential points from Arena Shop speedups : {}, buying {} speedup{}.".format(
        (arena_coins//300)*60*15, 
        arena_coins//300,
        's' if (arena_coins//300)>1 else ''))
    
    trial_coins = st.number_input('Trial Tower Coins', 0)
    trial_speedups = trial_coins // 12
    if trial_speedups > 99 :
        trial_speedups = 99
    st.write("Potential points from Trial Tower Coins speedups : {}, buying {} speedup{}.".format(
        trial_speedups*60*15, 
        trial_speedups,
        's' if trial_speedups>1 else ''))

    st.write("")

st.write("*Specially made for Mavikiwi* 😋")


