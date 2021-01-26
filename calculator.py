# to run : streamlit run calcultor.py

import streamlit as st
import numpy as np
from functions import *

st.title("# MOKulator !")
st.write('---')

### --- ACE LORD --- ###
if st.sidebar.checkbox("Development (Construction + Research)"):
    st.markdown("## Ace Lord : Development (Construction + Research)")    
 ### REGULAR SPEEDUPS ###
    st.markdown("### Regular speedup items in your bag")

    reg_total_mins, reg_days, reg_mins = get_bag_min('regular')
    reg_total_points = boosting_points(reg_total_mins)
    write_min_recap('regular', reg_total_mins, reg_days, reg_mins)


 ### RESEARCH SPEEDUPS ###
    st.markdown("### Research speedup items in your bag")

    search_total_mins, search_days, search_mins = get_bag_min('research')
    search_total_points = boosting_points(search_total_mins)
    write_min_recap('research', search_total_mins, search_days, search_mins)


 ### BUILDING SPEEDUPS ### 
    st.markdown("### Building speedup items in your bag")

    build_total_mins, build_days, build_mins = get_bag_min('building')
    build_total_points = boosting_points(build_total_mins)
    write_min_recap('research', build_total_mins, build_days, build_mins)

 ### RECAP ALL SPEEDUPS ###

    total_mins = reg_total_mins + search_total_mins + build_total_mins
    days, mins = day_min_from_total(total_mins)

    st.markdown("-")
    st.write("**TOTAL**")
    st.write("Total speedup minutes in your bag : {}.".format(total_mins))
    st.write("Being {} day{}, {} hour{}, {} min.".format(
        days, 
        's' if days > 1 else '',
        int(mins // 60), 
        's' if (int(mins//60)) >1 else '',
        mins%60))


### SPEEDUP EVENT ###
elif st.sidebar.checkbox("Speedup event") :
    st.markdown("## Speedups event")
    st.write("You've kept all your speedups for this event : **awesome** ! But is it worth spending them all ?")  

    st.write("First, let's have a look in your bag (I promise I won't tell anyone) !")
    
 ### REGULAR SPEEDUPS ###
    st.markdown("### Regular speedup items in your bag")

    reg_total_mins, reg_days, reg_mins = get_bag_min('regular')
    reg_total_points = boosting_points(reg_total_mins)

    write_min_recap('regular', reg_total_mins, reg_days, reg_mins)
    st.write("Potential points you will get *from all your {} speedups* : {}.".format('regular', reg_total_points))

 ### RESEARCH SPEEDUPS ###
    st.markdown("### Research speedup items in your bag")

    search_total_mins, search_days, search_mins = get_bag_min('research')
    search_total_points = boosting_points(search_total_mins)

    write_min_recap('research', search_total_mins, search_days, search_mins)
    st.write("Potential points you will get *from all your {} speedups* : {}.".format('research', search_total_points))

 ### TRAINING SPEEDUPS ###
    st.markdown("### Training speedup items in your bag")

    train_total_mins, train_days, train_mins = get_bag_min('training')
    train_total_points = boosting_points(train_total_mins)

    write_min_recap('research', train_total_mins, train_days, train_mins)
    st.write("Potential points you will get *from all your {} speedups* : {}.".format('training', train_total_points))

 ### BUILDING SPEEDUPS ### 
    st.markdown("### Building speedup items in your bag")

    build_total_mins, build_days, build_mins = get_bag_min('building')
    build_total_points = boosting_points(build_total_mins)

    write_min_recap('research', build_total_mins, build_days, build_mins)
    st.write("Potential points you will get *from all your {} speedups* : {}.".format('building', build_total_points))

 ### RECAP ALL SPEEDUPS ###

    total_mins = reg_total_mins + search_total_mins + train_total_mins + build_total_mins
    days, mins = day_min_from_total(total_mins)
    total_points = boosting_points(total_mins)

    st.markdown("-")
    st.write("**TOTAL**")
    st.write("Total speedup minutes in your bag : {}.".format(total_mins))
    st.write("Being {} day{}, {} hour{}, {} min.".format(
        days, 
        's' if days > 1 else '',
        int(mins // 60), 
        's' if (int(mins//60)) >1 else '',
        mins%60))
    st.write("Total points you will get *if you use all your speedups* : {}.".format(total_points))

    st.write('-')
    st.write("What is your goal?")
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

    st.write("Which would make, including your current poins : {}.".format(total_points))
    if diff_2 > 0 :
        st.write("You would still need {} point{} to get to your objective, equivalent to {} more minute{} of speed-ups.".format(
            diff_2,
            's' if diff_2 > 1 else '',
            (diff_2+14)//15,
            's' if ((diff_2+14)//15) > 1 else ''
        ))

    st.markdown("-")

    st.write("Not enough?")
    st.write("You can also buy 60-min speedups in *Hero Arena Shop* : 1 item for 300 coins,")
    st.write("and from *Trial Shop* : 1 item for 12 coins (max 99 per day).")
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

### HERO FRAG GLORY EVENT ###
elif st.sidebar.checkbox("Hero frags event") :
    st.markdown("## Hero frags")
    st.write("You've been **strong**, you've kept your Arena Surprise Chests, Demon chests, Hero Choice Cards, Oath Runes, Championship Surprise Chest... Good!")
    st.write("Now is the time you were waiting for... Open all your chests, and go to Hero Hall to use your Oath Runes and free Recruits! 🥳")

    hero_actual = st.number_input("How many points did you get ?", 0)

    st.write("And what's left in your bag ?")

    hero_3 = st.number_input("3★ Hero Choice Cards", 0)
    hero_4 = st.number_input("4★ Hero Choice Cards", 0)
    hero_5 = st.number_input("5★ Hero Choice Cards", 0) # 20 000 pts

    st.write("Not enough? ***.")

#### GEAR EVENT ####
elif st.sidebar.checkbox("Gear points") :
    # bag : 
    # lost lands
    # alliance shop
    st.write("Soon!")
    pass

else :
    st.write("Select the event you want with the checkbox. Please remember that if you uncheck an event, all the information you entered will be lost.")

st.write('---')
st.write("Specially made for the Mavdalorian. 😋")
st.write("*This is the way.*")


