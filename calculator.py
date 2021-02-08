# to run : streamlit run calcultor.py

import streamlit as st
import numpy as np
from functions import *
import pandas as pd

st.title("# MOKulator !")
st.markdown("### 🚧 Site under construction ! 🧱⛏️")
st.write('---')

### -- ACE LORD -- ##
calendar = "📅 Calendar..."
ace_monday = "♔ Gathering"
ace_tuesday = "♔ Development"
# ace_wednesday = "Consume Stamina and AP"
# ace_thurday = "Finish troops"
ace_friday = "♔ Ultimate might" # Blacksmith might, essence, blessing
ace_week_end = "♔ Ultimate Trial" #  Improve building and research might, train troops

### -- Other week -- ###
week2_monday = "♚ Hero Update"
week2_tuesday_dev = "♚ New Development"
week2_tuesday_bless = "♚ Stone of Blessing"
# week2_wednesday = "Obtain Equipment and Blessing stones items"
week2_thursday = "♚ Sauroi Power"
# week2_friday = "Obtain gems and Blessing stone items"
# week2_week_end = "Consume diamonds"

### -- Hell events -- ###



event = st.sidebar.radio(
    "Choose your event !",
    (calendar, ace_monday, ace_tuesday, ace_friday, ace_week_end,
    week2_monday, week2_tuesday_dev, week2_tuesday_bless, week2_thursday))

if event == calendar :

    st.write("**⤎⤛**")
    st.write("**⤎⤛** &nbsp &nbsp &nbsp Select the event you want in the menu")
    st.write("**⤎⤛**")
    st.write(" ")
    st.write("*Please remember that when you change your selection, all the information you entered will be lost.*")

    st.write("---")
    st.markdown('## Calendar')

    st.markdown('### ♔ *Ace Lord Week* ♔')
    st.write("**Monday**: Gathering.")
    st.write("**Tuesday**: Development - Finish Construction + Research.")
    st.write("**Wednesday**: Consume Stamina and AP.")
    st.write("**Thursday**: Finish troops.")
    st.write("**Friday**: Ultimate Might - Improve Blacksmith might, get essences, get blessing stones.")
    st.write("**Week-end**: Ultimate Trial - Finish Constructions + Research + Troops.")

    st.markdown('### ♚ *Other Week* ♚')
    st.write("**Monday**: Hero Update - Get hero fragments.")
    st.write("**Tuesday**: New Development - Get Mark of glory, use speedups &nbsp &nbsp &nbsp / &nbsp &nbsp &nbsp Stone of Blessing")
    st.write("**Wednesday**: Obtain Equipment items.")
    st.write("**Thursday**: Sauroi Power - Get Runestones, get Saurgem Material.")
    st.write("**Friday**: Obtain gems and Blessing stone items.")
    st.write("**Week-end**: Consume diamonds.")

### --- ACE LORD --- ###
if event == ace_monday : # Gathering
    st.markdown("## ♔ Ace Lord - Gathering ♔")
    st.write('Event on Monday of Ace Lord week.')
    st.write("-")
    st.write("**How to earn points**")
    st.write("- 2 pts every 20 Food / 20 Wood / 4 Iron / 1 Gold gathered.")
    st.write("- 1 pt every 10 Rare Earth Ore gathered.")
    st.write("-")
    st.write("**Points rewards phases**")
    st.write("Phase 1 - Pts : 18,000")
    st.write("Phase 2 - Pts : 36,000")
    st.write("Phase 3 - Pts : 72,000")
    st.write("Phase 4 - Pts : 144,000")
    st.write("Phase 5 - Pts : 360,000")
    st.write("Phase 6 - Pts : 720,000")
    st.write("-")
    st.write("**Points for each resource spot**")

    st.write("Level 7 &nbsp&nbsp - &nbsp&nbsp 40,000 points.") # 400k food
    st.write("Level 6 &nbsp&nbsp - &nbsp&nbsp 28,000 points.") # 280 k food
    st.write("Level 5 &nbsp&nbsp - &nbsp&nbsp 20,000 points.") # 200k food
    st.write("Level 4 &nbsp&nbsp - &nbsp&nbsp 13,500 points.") # 135k food
    st.write("Level 3 &nbsp&nbsp - &nbsp&nbsp &nbsp 8,000 points.") # 80k food
    st.write("Level 2 &nbsp&nbsp - &nbsp&nbsp &nbsp 4,000 points.") # 40k food
    st.write("Level 1 &nbsp&nbsp - &nbsp&nbsp &nbsp 2,000 points.") # 20k food

    st.write("-")
    st.write('**Same level spots grant the same points... But what can your troops gather the quickest ?**')

    st.write("If you're VIP 10, apply your \"Gathering\" talent tree before looking at your numbers ;)" )

    ## Boost Info
    st.write("&nbsp")
    st.write("First, let's see your **Lord Boost Info** ! 🏰")
    st.write("*If you are using a gathering speedup bonus, it is already included in these stats by the game.*")
    rss_b = st.number_input("Resource Gathering Speed", min_value=0.0, step=0.1)
    food_b = st.number_input("Food Gathering Speed", min_value=0.0, step=0.1)
    wood_b = st.number_input("Wood Gathering Speed", min_value=0.0, step=0.1)
    iron_b = st.number_input("Iron Gathering Speed", min_value=0.0, step=0.1)
    gold_b = st.number_input("Gold Gathering Speed", min_value=0.0, step=0.1)

    ## Gathering Speed-up
    # st.write("&nbsp")
    # st.write("♔ Are you using a **Gathering Speedup** ?")
    # st.markdown("###### You really should...")
    # st.write("")
    # gathering_speed_up = st.number_input("Value of your speedup bonus", 0, step=5)

    ## Basic gathering speeds
    food_gs = 43200
    wood_gs = 43200
    iron_gs = 8640
    gold_gs = 2160

    ## Calculation :p
    total_speed_food = int(food_gs * (rss_b + food_b + 20)/100)
    total_speed_wood = int(wood_gs * (rss_b + wood_b + 20)/100)
    total_speed_iron = int(iron_gs * (rss_b + iron_b + 20)/100)
    total_speed_gold = int(gold_gs * (rss_b + gold_b + 20)/100)

    time_food = 400000 / (food_gs + total_speed_food) * 60
    time_wood = 400000 / (wood_gs + total_speed_wood) * 60
    time_iron = 80000 / (iron_gs + total_speed_iron) * 60
    time_gold = 20000 / (gold_gs + total_speed_gold) * 60


    st.write("-")

    st.write("**Gathering speeds & Time needed to empty a level 7 Resource Spot**")
    d = {'Resource' : ['Food', 'Wood', 'Iron', 'Gold'], 
    "Basic speed / h" : [food_gs, wood_gs, iron_gs, gold_gs],
    "Bonus speed / h" : [total_speed_food, total_speed_wood, total_speed_iron, total_speed_gold],
    "Empty Lvl 7 in" : [
        "{} min".format(round(time_food)), 
        "{} min".format(round(time_wood)), 
        "{} min".format(round(time_iron)), 
        "{} min".format(round(time_gold))
        ],
    "Equivalent to..." : [
    "{} h {} min".format(round(time_food//60), round(time_food % 60)),
    "{} h {} min".format(round(time_wood//60), round(time_wood % 60)),
    "{} h {} min".format(round(time_iron//60), round(time_iron % 60)),
    "{} h {} min".format(round(time_gold//60), round(time_gold % 60))
    ]}

    df = pd.DataFrame(d)
    st.table(df)


    # st.write("Food :&nbsp {} / h +&nbsp {} / h.".format(food_gs, total_speed_food))
    # st.write("Wood : {} / h +&nbsp {} / h.".format(wood_gs, total_speed_wood))
    # st.write("Iron :&nbsp&nbsp&nbsp&nbsp&nbsp {} / h +&nbsp {} / h.".format(iron_gs, total_speed_iron))
    # st.write("Gold :&nbsp&nbsp&nbsp&nbsp {} / h +&nbsp&nbsp {} / h.".format(gold_gs, total_speed_gold))
    # st.write("-")
    
    # st.write("**Time needed to empty a level 7 Resource Spot**")
    # st.write("Food :&nbsp {} min ⟶ {} h {} min.".format(round(time_food), round(time_food//60), round(time_food % 60)))
    # st.write("Wood : {} min ⟶ {} h {} min.".format(round(time_wood), round(time_wood//60), round(time_wood % 60)))
    # st.write("Iron :&nbsp&nbsp&nbsp {} min ⟶ {} h {} min.".format(round(time_iron), round(time_iron//60), round(time_iron % 60)))
    # st.write("Gold :&nbsp&nbsp {} min ⟶ {} h {} min.".format(round(time_gold), round(time_gold//60), round(time_gold % 60)))

    st.write("-")

    dict_time = {'Food' : time_food,
       'Wood' : time_wood, 
       'Iron' : time_iron,
       'Gold' : time_gold}

    st.write("You should gather **{}** for points optimization !".format(min(dict_time, key=dict_time.get)))

    st.write("-")
    st.write("⚠️ Don't forget to apply your \"Gathering\" talent tree before sending your troops gather !")

if event == ace_tuesday : # Development (Construction + Research)
    st.markdown("## ♔ Ace Lord - Development ♔")
    st.write('Event on Tuesday of Ace Lord week.')
    st.write("-")
    st.write("**How to earn points**")
    st.write("- Improve Building Might by 1 - 5 pts")
    st.write("- Improve Tech Might by 1 - 5 pts")
    st.write("-")
    st.write("**Points rewards phases**")
    st.write("Phase 1 - Pts : 54,000")
    st.write("Phase 2 - Pts : 108,000")
    st.write("Phase 3 - Pts : 216,000")
    st.write("Phase 4 - Pts : 432,000")
    st.write("Phase 5 - Pts : 1,080,000")
    st.write("Phase 6 - Pts : 2,160,000")
    st.write("-")
    st.write('♔ Before starting to build, think about your boosts !')
    
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

if event == ace_friday :  # "Ultimate might" # Blacksmith might, essence, blessing
    st.markdown("## Ace Lord - Ultimate might (Blacksmith)")
    st.write("Gear, Gem, Saurgem, Warsigil might, essences, blessing stones")
    st.write('Event on Friday of Ace Lord week.')

if event == ace_week_end : # Improve building and research might, train troops
    st.markdown("## Ace Lord - Ultimate Trial (Buildings, Research, Troops)")
    st.write('**Event on the week-end of Ace Lord week.**')

### SPEEDUP EVENT ###
elif event == week2_tuesday_dev : # Speedups event
    st.markdown("## New Development")
    st.markdown("### Use speedups, get Mark of glory.")
    st.write("Use 1 min of speedup = 15 pts")
    st.write("Get 1 Mark of Glory = 350 pts")
    st.write("Minimum of points to receive rank rewards : 900,000.")

    st.write("---")

    st.write("You've kept all your speedups for this event : **awesome** ! But is it worth spending them *at all* ?")  
    st.write("First, let's have a look in your bag (I promise I won't tell anyone) !")
    
 ### REGULAR SPEEDUPS ###
    st.markdown("### Regular speedup items in your bag")

    reg_total_mins, reg_days, reg_mins = get_bag_min('regular')
    reg_total_points = boosting_points(reg_total_mins)

    write_min_recap('regular', reg_total_mins, reg_days, reg_mins)
    st.write("Potential points you would get *from all your {} speedups* : {}.".format('regular', reg_total_points))

 ### RESEARCH SPEEDUPS ###
    st.markdown("### Research speedup items in your bag")

    search_total_mins, search_days, search_mins = get_bag_min('research')
    search_total_points = boosting_points(search_total_mins)

    write_min_recap('research', search_total_mins, search_days, search_mins)
    st.write("Potential points you would get *from all your {} speedups* : {}.".format('research', search_total_points))

 ### TRAINING SPEEDUPS ###
    st.markdown("### Training speedup items in your bag")

    train_total_mins, train_days, train_mins = get_bag_min('training')
    train_total_points = boosting_points(train_total_mins)

    write_min_recap('research', train_total_mins, train_days, train_mins)
    st.write("Potential points you would get *from all your {} speedups* : {}.".format('training', train_total_points))

 ### BUILDING SPEEDUPS ### 
    st.markdown("### Building speedup items in your bag")

    build_total_mins, build_days, build_mins = get_bag_min('building')
    build_total_points = boosting_points(build_total_mins)

    write_min_recap('research', build_total_mins, build_days, build_mins)
    st.write("Potential points you would get *from all your {} speedups* : {}.".format('building', build_total_points))

 ### RECAP ALL SPEEDUPS ###

    total_mins = reg_total_mins + search_total_mins + train_total_mins + build_total_mins
    days, mins = day_min_from_total(total_mins)
    total_points = boosting_points(total_mins)

    st.markdown("-")
    st.markdown("### Using everything from your bag...")

    st.write("Total **speedup minutes** in your bag : {}.".format(total_mins))
    st.write("Being {} day{}, {} hour{}, {} min.".format(
        days, 
        's' if days > 1 else '',
        int(mins // 60), 
        's' if (int(mins//60)) >1 else '',
        mins%60))
    st.write("Total points you would get *if you use all your speedups* : {}.".format(total_points))

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
    if total_points < 900000 :
        st.write("**I'm afraid that's not enough to get rank rewards (minimum is *900,000 pts*).**")
    if diff_2 > 0 :
        st.write("You would still need {} point{} to get to your objective, equivalent to {} more minute{} of speed-ups.".format(
            diff_2,
            's' if diff_2 > 1 else '',
            (diff_2+14)//15,
            's' if ((diff_2+14)//15) > 1 else ''
        ))

    st.write("-")

    st.markdown("### Not enough?")
    st.write("You can also buy **60-min speedups** in *Hero Arena Shop* : 1 item for 300 coins,")
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

    trial_points = trial_speedups*60*15

    st.write("Potential points from Trial Shop speedups : {}, buying {} speedup{}.".format(
        trial_points, 
        trial_speedups,
        's' if trial_speedups>1 else ''))

    st.write("-")
    st.write("You can buy **Mark of Glory** items in the Rare Earth Shop")
    rare_earth_coins = st.number_input("Rare Earth items owned :", 0)
    mark_of_glory = rare_earth_coins // 5000
    mark_of_glory_points = mark_of_glory * 350

    st.write("Potential points from Rare Earth Mark of Glory : {}, buying {} items.".format(mark_of_glory_points, mark_of_glory))

    st.write("")
    new_total = total_points + (arena_coins//300)*60*15 + trial_points + mark_of_glory_points
    st.write("New total : {} points.".format(new_total))

    if new_total < 900000 :
        st.write("**I'm afraid that's not enough to get rank rewards (minimum is *900,000 pts*).**")
    if objective - new_total > 0 :
        st.write("You would still be {} point{} away from your objective ({} points).".format(
            diff_2,
            's' if diff_2 > 1 else '',
            objective
        ))

### STONE OF BLESSING ###
elif event == week2_tuesday_bless :
    st.markdown("## Stone of Blessing")
    #st.markdown("### Get Stone of Blessing")
    st.write("Get 1 Stone of Blessing = 1000 pts")
    st.write("Minimum of points to receive rank rewards : 500,000.")

    diamonds = st.number_input("How many diamonds do you have ?",0)

    stones = diamonds // 100
    stone_pts = stones * 1000

    st.write("Potential points : {}, buying {} stones.".format(stone_pts, stones))

elif event == week2_thursday :
    st.markdown("## Sauroi Power")
    #st.markdown("### Get Stone of Blessing")
    st.write("Get 100 Runestones = 40 pts")
    st.write("Other points for Saurgem material.")
    st.write("Minimum of points to receive rank rewards : 1,500,000.")
    pass


### HERO FRAG EVENT ###
elif event == week2_monday : # Hero frags event
    st.markdown("## Hero Upgrade")
    st.write("You've been **strong**, you've kept your Arena Surprise Chests, Demon chests, Hero Choice Cards, Oath Runes, Championship Surprise Chest... Good!")
    st.write("Now is the time you were waiting for... **Open all your chests**, and go to Hero Hall to use your Oath Runes and free Recruits! 🥳")

    hero_actual = st.number_input("How many points did you get ?", 0)
    st.write("What is your goal?")
    objective = st.number_input('Objective of points', 0)

    st.write("And what's left in your bag ?")

    hero_2 = st.number_input("2★ Hero Choice Cards", 0) # 500 pts
    hero_3 = st.number_input("3★ Hero Choice Cards", 0) # 2 000 pts
    hero_4 = st.number_input("4★ Hero Choice Cards", 0) # 8 000 pts
    hero_5 = st.number_input("5★ Hero Choice Cards", 0) # 20 000 pts

    sum_cards = hero_2 + hero_3 + hero_4 + hero_5
    sum_points = hero_2 * 500 + hero_3 * 2000 + hero_4 * 8000 + hero_5 * 20000

    st.write("**TOTAL**")
    st.write("You will get {} points using your {} cards.".format(sum_points, sum_cards))
    st.write("Including previous points: {}.".format(hero_actual+sum_points))

    diff = objective - (hero_actual+sum_points)
    if diff > 0 :
        st.write("You are {} point{} away from your objective.".format(
            diff, 
            's' if diff > 1 else ''))
    else :
        st.write("Seems like you have already fulfilled your objective ;)")

    st.write('-')

    st.write("Not Enough ?")
    st.write("You can get more frags :")

    st.write("- Hero Arena Shop : 3★ frags, 4★ frags or 4★ Hero Choice Card;")
    st.write("- Legion Showdown Shop : 4★ Hero Choice Card,  5★ Hero Choice Card;")
    st.write("- Trial shop : 4★ frags;")
    st.write("- Rare Earth Fields : 5★ frags.")
    st.write("")

    trial_coins = st.number_input('Trial Tower Coins', 0)
    hart_frags = trial_coins // 50
    if hart_frags > 10 :
        hart_frags = 10
    trial_tower_points = hart_frags*8000
    st.write("Potential points from Trial Shop - Hart Frags : {}, buying {} frags.".format(trial_tower_points, hart_frags))

    rare_earth = st.number_input("Rare Earth material", 0)
    ryska_frags = rare_earth // 350000
    rare_earth_points = ryska_frags * 20000
    st.write("Potential points from Rare Earth Fields - Ryska frags : {}, buying {} frags.".format(rare_earth_points, ryska_frags))


#### GEAR EVENT ####
#elif st.sidebar.checkbox("Gear points") :
    # bag : 
    # lost lands
    # alliance shop
#    st.write("Soon!")
#    pass

st.write('---')
st.write("Specially made for the Mavdalorian. 🥰")
st.write("*This is the way.*")


