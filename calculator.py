# to run : streamlit run calcultor.py

import streamlit as st
import numpy as np
from functions import *
import pandas as pd

st.title("# MOKulator !")
st.markdown("### 🚧 Site under construction ! 🧱 ⛏️")
st.write('---')

### -- ACE LORD -- ##
calendar = "📅 Calendar..."
ace_monday = "♔ Gathering"
ace_tuesday = "♔ Development"
# ace_wednesday = "Consume Stamina and AP"
ace_thurday = "♔ Master Trainer"
warsigil = "♚ Warsigil Upgrade"
ace_friday = "♔ Ultimate might" # Blacksmith might, essence, blessing
ace_week_end = "♔ Ultimate Trial" #  Improve building and research might, train troops

### -- Other week -- ###
week2_monday = "♚ Hero Update"
week2_tuesday_dev = "♚ New Development"
week2_tuesday_bless = "♚ Stone of Blessing"
# week2_wednesday = "Obtain Equipment and Blessing stones items"
week2_thursday = "♚ Sauroi Power"
week2_friday = "♚ Gem Upgrade"
# week2_week_end = "Consume diamonds"

### -- Hell events -- ###

time_calculator = "⏳ Time Converter"
might_speed = "🔎 Might + Speedups pts"
rss_calc = "🌰 Resources Calculator"


event = st.sidebar.radio(
    "Choose your event !",
    (calendar, ace_monday, ace_tuesday, warsigil, ace_thurday, ace_friday, ace_week_end,
    week2_monday, week2_tuesday_dev, week2_tuesday_bless, week2_thursday, week2_friday,
    time_calculator, might_speed, rss_calc))

if event == calendar :

    st.write("**⤎⤛**")
    st.write("**⤎⤛** &nbsp &nbsp &nbsp Select the event you want in the menu")
    st.write("**⤎⤛**")
    st.write(" ")
    st.write("*Please remember that when you change your selection, all the information you entered will be lost.*")

    st.write("---")
    st.markdown('# Calendar')

    st.markdown('## ♔ Ace Lord Week ♔')
    st.markdown("### Monday")
    st.write("✨ 1/6 - Gathering")
    st.write("+ Lucky Draw - day 1")
    st.write("+ Demon Incursion")

    st.markdown("### Tuesday")
    st.write("✨ 2/6 - Development - Finish Construction + Research")
    st.write("+ Lucky Draw - day 2")

    st.markdown("### Wednesday")
    st.write("✨ 3/6 - Hunt Monsters - Consume Stamina and AP")
    st.write("+ Lucky Draw - day 3")

    st.markdown("### Thursday")
    st.write("✨ 4-/6 Master Trainer - Finish Troops") 
    st.write("🎊 Warsigil Upgrade")
    st.write("+ Hell events")
    st.write("+ Element Trial I - Purple + Yellow Heroes")
    st.write("+ Demon Incursion")

    st.markdown("### Friday")
    st.write("✨ 5/6 - Ultimate Might - Improve Blacksmith might, get essences, get blessing stones")
    st.write("+ Hell events")
    st.write("+ Element Trial III - Green + Blue + Purple Heroes")
    st.write("+ Battle of Saurnesia")

    st.markdown("### Week-end")
    st.write("✨ 6/6 - Ultimate Trial - Finish Constructions + Research + Troops")
    st.write("+ Boneyard")
    st.write("+ Hell events")
    st.write("+ Element Trial IV - All colors")
    st.write("+ Hunter Tactic")
    st.write("+ Military Expedition")

    st.write("-")

    st.markdown('## ♚ Other Week ♚')
    st.markdown("### Monday")
    st.write("🎊 Hero Update - Get Hero Fragments")
    st.write("+ Personal Activity")
    st.write("+ Element Trial I - Blue + Yellow Heroes")
    st.write("+ Challenger's Path - day 1")

    st.markdown("### Tuesday###")
    st.write("🎊 New Development - Get Mark of glory, use speedups")
    st.write("🎊 Stone of Blessing")
    st.write("+ Gather Supplies")
    st.write("+ Challenger's Path - day 2")
    st.write("+ Monster Hunt")

    st.write("### Wednesday")
    st.write("Joy 777 - day 1")
    st.write("🎊 Gear Upgrade - Get Gear Material")
    st.write("Challenger's Path")
    st.write("Elemental Trial II - Green + Purple + Red Heroes")

    st.write("### Thursday")
    st.write("Joy 777 - day 2")
    st.write("🎊 Sauroi Power - Get Runestones, get Saurgem Material")
    st.write("Monster Hunt")
    st.write("Hell events")
    st.write("Army expension")
    st.write("Element Trial I - Blue + Yellow Heroes")

    st.write("### Friday")
    st.write("🎊 Gem Upgrade - Get Gem Material")
    st.write("Battle of Saurnesia")
    st.write("Joy 777 - day 3")
    st.write("Elemental Trial IV - Green + Yellow Heroes")

    st.write("### Week-end")
    st.write("🎊 Consume diamonds")
    st.write("Valiant Conquest")

    st.write('---')
    st.write("🎊 Events where you can get Summon Stone II.")
    st.write("✨ Ace Lord : week-long event where you can get Summon Stone I.")

### --- ACE LORD --- ###
if event == ace_monday : # Gathering
    st.markdown("## ♔ Ace Lord - Gathering ♔")
    st.write('**Event on Monday of Ace Lord week.**')
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
    st.write('**Event on Tuesday of Ace Lord week.**')
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
    st.markdown("## ♔ Ace Lord - Ultimate might ♔")
    st.write('**Event on Friday of Ace Lord week.**')
    st.write("Blacksmith : Gear, Gem, Saurgem, Warsigil might, essences, blessing stones")

if event == ace_week_end : # Improve building and research might, train troops
    st.markdown("## ♔ Ace Lord - Ultimate Trial ♔")
    st.write('**Event on the week-end of Ace Lord week.**')
    st.write("Buildings, Research, Troops")

if event == ace_thurday : # Master Trainer
    st.markdown("## ♔ Ace Lord - Master Trainer ♔")
    st.write('**Event on Thursday of Ace Lord week.**')

    promoting = st.checkbox("<-- check this for promoting version")

    tier_before = st.slider("What tier are the troops to promote ?", min_value=1, max_value=11) if promoting else 0
    tier = st.slider("What tier are the troops you are planning to train ?", min_value=tier_before+1, max_value=12)

    if promoting :
        st.write(f"Promoting troops from t{tier_before} to t{tier}!") 
    else:
        st.write(f"Training t{tier} troops!")



    soldiers_batch = st.number_input("Training capacity:", 0)
    nb_batch = st.number_input("How many batches do you want to do ?", 1)






### HERO FRAG EVENT ###
elif event == week2_monday : # Hero frags event
    st.markdown("## ♚ Hero Upgrade ♚")
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
    st.write("You will get {:,} points using your {} cards.".format(sum_points, sum_cards))
    st.write("Including previous points: {:,}.".format(hero_actual+sum_points))

    diff = objective - (hero_actual+sum_points)
    if diff > 0 :
        st.write("You are {:,} point{} away from your objective.".format(
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
    st.write("Potential points from Trial Shop - Hart Frags : {:,}, buying {} frags.".format(trial_tower_points, hart_frags))

    rare_earth = st.number_input("Rare Earth material", 0)
    ryska_frags = rare_earth // 350000
    rare_earth_points = ryska_frags * 20000
    st.write("Potential points from Rare Earth Fields - Ryska frags : {:,}, buying {} frags.".format(rare_earth_points, ryska_frags))

### SPEEDUP EVENT ###
elif event == week2_tuesday_dev : # Speedups event
    st.markdown("## ♚ New Development ♚")
    st.markdown("### Use speedups, get Mark of glory.")
    st.write("Use 1 min of speedup = 15 pts")
    st.write("Get 1 Mark of Glory = 500 pts")
    st.write("Minimum of points to receive rank rewards : 900,000.")

    st.write("---")

    st.write("You've kept all your speedups for this event : **awesome** ! But is it worth spending them *at all* ?")  
    st.write("First, let's have a look in your bag (I promise I won't tell anyone) !")
    
 ### REGULAR SPEEDUPS ###
    st.markdown("### Regular speedup items in your bag")

    reg_total_mins, reg_days, reg_mins = get_bag_min('regular')
    reg_total_points = boosting_points(reg_total_mins)

    write_min_recap('regular', reg_total_mins, reg_days, reg_mins)
    st.write("Potential points you would get *from all your {} speedups* : {:,}.".format('regular', reg_total_points))

 ### RESEARCH SPEEDUPS ###
    st.markdown("### Research speedup items in your bag")

    search_total_mins, search_days, search_mins = get_bag_min('research')
    search_total_points = boosting_points(search_total_mins)

    write_min_recap('research', search_total_mins, search_days, search_mins)
    st.write("Potential points you would get *from all your {} speedups* : {:,}.".format('research', search_total_points))

 ### TRAINING SPEEDUPS ###
    st.markdown("### Training speedup items in your bag")

    train_total_mins, train_days, train_mins = get_bag_min('training')
    train_total_points = boosting_points(train_total_mins)

    write_min_recap('research', train_total_mins, train_days, train_mins)
    st.write("Potential points you would get *from all your {} speedups* : {:,}.".format('training', train_total_points))

 ### BUILDING SPEEDUPS ### 
    st.markdown("### Building speedup items in your bag")

    build_total_mins, build_days, build_mins = get_bag_min('building')
    build_total_points = boosting_points(build_total_mins)

    write_min_recap('research', build_total_mins, build_days, build_mins)
    st.write("Potential points you would get *from all your {} speedups* : {:,}.".format('building', build_total_points))

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
    st.write("Total points you would get *if you use all your speedups* : {:,}.".format(total_points))

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

    st.write("Which would make, including your current poins : {:,}.".format(total_points))
    if total_points < 900000 :
        st.write("**I'm afraid that's not enough to get rank rewards (minimum is *900,000 pts*).**")
    if diff_2 > 0 :
        st.write("You would still need {:,} point{} to get to your objective, equivalent to {} more minute{} of speed-ups.".format(
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
    st.write("Potential points from Arena Shop speedups : {:,}, buying {} speedup{}.".format(
        (arena_coins//300)*60*15, 
        arena_coins//300,
        's' if (arena_coins//300)>1 else ''))
    
    trial_coins = st.number_input('Trial Tower Coins', 0)
    trial_speedups = trial_coins // 12
    if trial_speedups > 99 :
        trial_speedups = 99

    trial_points = trial_speedups*60*15

    st.write("Potential points from Trial Shop speedups : {:,}, buying {} speedup{}.".format(
        trial_points, 
        trial_speedups,
        's' if trial_speedups>1 else ''))

    st.write("-")
    st.write("You can buy **Mark of Glory** items in the Rare Earth Shop")
    rare_earth_coins = st.number_input("Rare Earth items owned :", 0)
    mark_of_glory = rare_earth_coins // 5000
    mark_of_glory_points = mark_of_glory * 500

    st.write("Potential points from Rare Earth Mark of Glory : {:,}, buying {} items.".format(mark_of_glory_points, mark_of_glory))

    st.write("")
    new_total = total_points + (arena_coins//300)*60*15 + trial_points + mark_of_glory_points
    st.write("New total : {:,} points.".format(new_total))

    if new_total < 900000 :
        st.write("**I'm afraid that's not enough to get rank rewards (minimum is *900,000 pts*).**")
    if objective - new_total > 0 :
        st.write("You would still be {:,} point{} away from your objective ({:,} points).".format(
            diff_2,
            's' if diff_2 > 1 else '',
            objective
        ))

### STONE OF BLESSING ###
elif event == week2_tuesday_bless :
    st.markdown("## ♚ Stone of Blessing ♚")
    #st.markdown("### Get Stone of Blessing")
    st.write("Get 1 Stone of Blessing = 1000 pts")
    st.write("Minimum of points to receive rank rewards : 500,000.")

    diamonds = st.number_input("How many diamonds do you have ?",0)

    stones = diamonds // 100
    stone_pts = stones * 1000

    st.write("Potential points : {:,}, buying {} stones.".format(stone_pts, stones))

### SAUROI POWER ###
elif event == week2_thursday :
    st.markdown("## ♚ Sauroi Power ♚")

    st.write("-")
    st.write("**How to earn points**")

    pts_per_rune = 40 / 100
    st.write("Get 100 Runestones - 40 pts")
    st.write('')

    essence_1_pts = 200
    st.write("Get 1★ Saurgem Essence - 200 pts")
    essence_2_pts = 1000
    st.write("Get 2★ Saurgem Essence - 1,000 pts")
    essence_3_pts = 4000
    st.write("Get 3★ Saurgem Essence - 4,000 pts")
    essence_4_pts = 10000    
    st.write("Get 4★ Saurgem Essence - 10,000 pts")
    st.write("Get 5★ Saurgem Essence - 40,000 pts")
    promote_stone_pts = 20000
    st.write("Get 8★ Saurgem Promoter - 20,000 pts")

    st.write("Get 3★ Saurgem - 1,000 pts")
    spinel_pts = 2000
    st.write("Get Saurgem Spinel - 2,000 pts")

    st.write('')

    st.write("Minimum of points to receive rank rewards : 1,500,000.")

    st.write('') 
    current_points = st.number_input("How many points do you have so far?", 0)

    st.write('')
    st.markdown("### What's in your bag ?")
    st.markdown("#### Let's look at your Runestones!")

    eco_500 = st.number_input("500 Economy Runestones", 0)
    eco_2k = st.number_input("2K Economy Runestones", 0)
    eco_10k = st.number_input("10K Economy Runestones", 0)    

    total_eco = 500 * eco_500 + 2000 * eco_2k + 10000 * eco_10k
    total_eco_points = total_eco * pts_per_rune

    st.write("Total of Economy Runestones : {}, granting {:,} points.".format(total_eco, round(total_eco_points)))

    mil_500 = st.number_input("500 Military Runestones", 0)
    mil_2k = st.number_input("2K Military Runestones", 0)
    mil_10k = st.number_input("10K Military Runestones", 0)

    total_mil = 500 * mil_500 + 2000 * mil_2k + 10000 * mil_10k
    total_mil_points = total_mil * pts_per_rune

    st.write("Total of Military Runestones : {}, granting {:,} points.".format(total_mil, round(total_mil_points)))
    st.write("**Total potential points** : {:,}.".format(round(total_eco_points + total_mil_points)))    

    ### CHOICE CHESTS ###
    st.write('')
    st.markdown("#### Let's look at your Choice Chests!")
    essence_chest = st.number_input("How many Essence Choice Chest do you have?", 0)
    essence_chest_pts = essence_chest * essence_1_pts * 100

    st.write("Points from chests : {:,}".format(essence_chest_pts))

    promote_chest = st.number_input("How many Promote Choice Chest do you have?", 0)
    promote_chest_pts = promote_chest * spinel_pts * 10

    st.write("Points from chests : {:,}".format(promote_chest_pts))

    promote_8_chest = st.number_input("How many 8★ Choice Chest do you have?", 0)
    promote_8_chest_pts = promote_8_chest * promote_stone_pts * 1

    st.write("Points from chests : {:,}".format(promote_8_chest_pts))
    
    st.write('')
    ## TOWER OF TRIAL ##
    st.markdown("### Tower of Trial")
    st.markdown("#### First victory rewards")
    trial_coins = st.number_input('Trial Tower Coins', 0)

    trial_spinels = st.slider("Saurgem Spinels available to buy in 1st Victory Items", min_value=0, max_value=500, step=100)
    if trial_spinels > 0 :
        trial_price = st.number_input(f"What's the price for these {trial_spinels} spinels?", 0)
        if trial_price > trial_coins:
            st.write("You don't seem to have enough to buy this...")
            trial_spinels = 0
        else:
            trial_coins = trial_coins - trial_price

    st.write('')
    st.markdown("#### Normal items")
    economy_trial = trial_coins // 8
    if economy_trial > 50 :
        economy_trial = 50
    trial_tower_points = round(economy_trial * 2000 * pts_per_rune + trial_spinels * spinel_pts)

    st.write("Points from Trial Shop : {:,}, buying {} * 2K Runestones & {} spinels.".format(trial_tower_points, economy_trial, trial_spinels))

    ## RARE EARTH SHOP ##
    st.markdown("### Rare Earth Shop")
    rare_earth_coins_start = st.number_input("Rare Earth items owned :", 0)

    rare_price_essence_1 = 500
    rare_max_essence_1 = 200
    # st.write("Essence 1 : {:.1}".format(essence_1_pts / rare_price_essence_1)) 0.4 pts per coin

    rare_price_essence_2 = 2200
    rare_max_essence_2 = 100
    # st.write("Essence 2 : {:.1}".format(essence_2_pts / rare_price_essence_2)) 0.5 pts per coin

    rare_price_essence_3 = 8500
    rare_max_essence_3 = 40
    # st.write("Essence 3 : {:.1}".format(essence_3_pts / rare_price_essence_3)) 0.5 pts per coin

    rare_price_essence_4 = 20000 
    rare_max_essence_4 = 20
    # st.write("Essence 4 : {:.1}".format(essence_4_pts / rare_price_essence_4)) 0.5 pts per coin

    rare_price_spinel = 5000
    rare_max_spinel = 300
    # st.write("Spinel : {:.1}".format(spinel_pts / rare_price_spinel)) 0.4 pts per coin

    st.markdown("#### Worthiest :")
    st.write('')
    rare_essence_4, rare_essence_4_pts, rare_earth_coins = saurgem_rare_earth_shop(rare_earth_coins_start, rare_price_essence_4, rare_max_essence_4, essence_4_pts)  
    st.write("4★ Saurgem Essence : {:,} pts, buying {:,} items.".format(rare_essence_4_pts, rare_essence_4))

    rare_essence_3, rare_essence_3_pts, rare_earth_coins = saurgem_rare_earth_shop(rare_earth_coins, rare_price_essence_3, rare_max_essence_3, essence_3_pts)  
    st.write("3★ Saurgem Essence : {:,} pts, buying {:,} items.".format(rare_essence_3_pts, rare_essence_3))

    rare_essence_2, rare_essence_2_pts, rare_earth_coins = saurgem_rare_earth_shop(rare_earth_coins, rare_price_essence_2, rare_max_essence_2, essence_2_pts)  
    st.write("2★ Saurgem Essence : {:,} pts, buying {:,} items.".format(rare_essence_2_pts, rare_essence_2))

    st.markdown("#### Less Worth it, but do it anyway if you want ;)")
    st.write('')
    rare_essence_1, rare_essence_1_pts, rare_earth_coins = saurgem_rare_earth_shop(rare_earth_coins, rare_price_essence_1, rare_max_essence_1, essence_1_pts)  
    st.write("1★ Saurgem Essence : {:,} pts, buying {:,} items.".format(rare_essence_1_pts, rare_essence_1))

    rare_spinel, rare_spinel_pts, rare_earth_coins = saurgem_rare_earth_shop(rare_earth_coins, rare_price_spinel, rare_max_spinel, spinel_pts)  
    st.write("Saurgem Spinels : {:,} pts, buying {:,} items.".format(rare_spinel_pts, rare_spinel))

    st.markdown("#### Even less worth the spending...")
    st.write('')
    rare_economy = rare_earth_coins // 5000
    rare_earth_coins = rare_earth_coins - rare_economy * 5000
    rare_economy_pts = round(rare_economy * 2000 * pts_per_rune)
    st.write("2K Economy Runestones : {:,} pts, buying {:,} items.".format(rare_economy_pts, rare_economy))    

    rare_earth_points = rare_essence_4_pts + rare_essence_3_pts + rare_essence_2_pts + rare_essence_1_pts + rare_spinel_pts + rare_economy_pts

    st.write('')
    st.write("Points from Rare Earth Shop : {:,}, spending {:,} rare earth items.".format(rare_earth_points, rare_earth_coins_start - rare_earth_coins))

    ## HERO CHAMPIONSHIP SHOP ##
    st.write('-')
    st.write("### Hero Championship Shop")

    championship_coins = st.number_input("How many Championship coins do you own ?", 0)
    
    runes_hero = championship_coins // 60
    if runes_hero > 200 :
        runes_hero = 200
    runes_hero_points = round(runes_hero * 10000 * pts_per_rune)
    st.write("Points from Hero Championship Shop : {:,}, spending {:,} coins.".format(runes_hero_points, runes_hero * 60))

    ## DIAMOND SHOP ##
    st.write('-')
    st.write('### Diamond Shop')
    diamonds = st.number_input("How many diamonds are you willing to spend ?",0)
    diamond_essence_1 = diamonds // 10
    diamond_essence_1_pts = diamond_essence_1 * essence_1_pts
    st.write("Points from Diamond Shop : {:,}, spending {:,} diamonds.".format(diamond_essence_1_pts, diamond_essence_1*10))

    ## TOTAL POINTS ##
    st.write('-')
    total_points = round(
        trial_tower_points + total_eco_points + total_mil_points + runes_hero_points +
        essence_chest_pts + promote_chest_pts + promote_8_chest_pts + current_points + rare_earth_points + diamond_essence_1_pts)
    st.write("**Total potential points** : {:,}.".format(total_points))



### GEM UPGRADE ###
elif event == week2_friday :
    st.markdown("## ♚ Gem Upgrade ♚")
    st.write("-")
    st.write("**How to earn points**")
    essence_1_pts = 100
    st.write("Get 1★ Gem Essence - 100 pts")
    essence_2_pts = 500
    st.write("Get 2★ Gem Essence - 500 pts")
    essence_3_pts = 2000
    st.write("Get 3★ Gem Essence - 2,000 pts")
    essence_4_pts = 5000
    st.write("Get 4★ Gem Essence - 5,000 pts")
    essence_5_pts = 20000
    st.write("Get 5★ Gem Essence - 20,000 pts")
    promote_stone_pts = 20000
    st.write("Get 8★ Gem Promote Stone - 20,000 pts")
    st.write("Get 3★ Gem - 1,000 pts")
    spinel_pts = 1000
    st.write("Get Gem Spinel - 1,000 pts")

    st.write('-')

    current_points = st.number_input("How many points do you have so far?", 0)
    st.write('-')

    ### CHESTS POINTS ###
    st.markdown("### What's in your bag ?")
    st.write("Let's look at your chests !")
    essence_chest = st.number_input("How many Essence Choice Chest do you have?", 0)
    essence_chest_pts = essence_chest * essence_1_pts * 100
    st.write("Max. points from chests : {:,}".format(essence_chest_pts))

    promote_chest = st.number_input("How many Promote Choice Chest do you have?", 0)
    promote_chest_pts = promote_chest * spinel_pts * 10
    st.write("Max. points from chests : {:,}".format(promote_chest_pts))

    promote_8_chest = st.number_input("How many 8★ Choice Chest do you have?", 0)
    promote_8_chest_pts = promote_8_chest * promote_stone_pts * 1
    st.write("Max. points from chests : {:,}".format(promote_8_chest_pts))
    
    chests_pts = essence_chest_pts + promote_chest_pts + promote_8_chest_pts
    st.write("**Total potential points from chests** : {:,}.".format(round(chests_pts)))    

    st.write('-')

    ## TOWER OF TRIAL ##
    st.markdown("### Tower of Trial")
    trial_coins_start = st.number_input('Trial Tower Coins', 0)
    st.markdown("#### First victory rewards")

    trial_spinels_first = st.slider("Gem Spinels available to buy in 1st Victory Items", min_value=0, max_value=500, step=100)
    if trial_spinels_first > 0 :
        trial_price = st.number_input(f"What's the price for these {trial_spinels_first} spinels?", 0)
        if trial_price > trial_coins_start:
            st.write("You don't seem to have enough to buy this...")
            trial_spinels_first = 0
            trial_price = 0
    else :
        trial_price = 0
    trial_coins = trial_coins_start - trial_price

    st.write('')
    st.markdown("#### Normal items")
    trial_price_essence_1 = 1
    trial_max_essence_1 = 1000
    #st.write("Essence 1 : {}".format(essence_1_pts / trial_price_essence_1)) / 100

    trial_price_essence_2 = 2
    trial_max_essence_2 = 400
    #st.write("Essence 2 : {}".format(essence_2_pts / trial_price_essence_2)) / 250

    trial_price_essence_3 = 8
    trial_max_essence_3 = 200
    #st.write("Essence 3 : {}".format(essence_3_pts / trial_price_essence_3)) / 250

    trial_price_spinel = 4
    trial_max_spinel = 600
    #st.write("Spinel : {}".format(spinel_pts / trial_price_spinel)) / 250

    st.markdown("#### Worthiest :")
    st.write('')

    trial_essence_2, trial_essence_2_pts, trial_coins = saurgem_rare_earth_shop(trial_coins, trial_price_essence_2, trial_max_essence_2, essence_2_pts)  
    st.write("2★ Gem Essence : {:,} pts, buying {:,} items.".format(trial_essence_2_pts, trial_essence_2))

    trial_essence_3, trial_essence_3_pts, trial_coins = saurgem_rare_earth_shop(trial_coins, trial_price_essence_3, trial_max_essence_3, essence_3_pts)  
    st.write("3★ Gem Essence : {:,} pts, buying {:,} items.".format(trial_essence_3_pts, trial_essence_3))

    trial_spinels, trial_spinel_pts, trial_coins = saurgem_rare_earth_shop(trial_coins, trial_price_spinel, trial_max_spinel, spinel_pts)  
    st.write("Gem Spinels : {:,} pts, buying {:,} items.".format(trial_spinel_pts, trial_spinels))

    st.markdown("#### Less Worth it, but do it anyway if you want ;)")
    st.write('')
    trial_essence_1, trial_essence_1_pts, trial_coins = saurgem_rare_earth_shop(trial_coins, trial_price_essence_1, trial_max_essence_1, essence_1_pts)  
    st.write("1★ Gem Essence : {:,} pts, buying {:,} items.".format(trial_essence_1_pts, trial_essence_1))

    trial_tower_points = trial_spinels_first * spinel_pts + trial_essence_2_pts + trial_essence_3_pts + trial_spinel_pts + trial_essence_1_pts

    st.write("Points from Trial Shop : {:,}, spending {} coins.".format(trial_tower_points, trial_coins_start - trial_coins))

    ## HERO CHAMPIONSHIP SHOP ##
    st.write('-')
    st.write("### Hero Championship Shop")

    championship_coins = st.number_input("How many Championship coins do you own ?", 0)
    
    gems_hero = championship_coins // 30
    gems_hero_pts = round(gems_hero * spinel_pts)
    st.write("Points from Hero Championship Shop : {:,}, spending {:,} coins.".format(gems_hero_pts, gems_hero * 30))


    ## DIAMOND SHOP ##
    st.write('-')
    st.write('### Diamond Shop')
    diamonds = st.number_input("How many diamonds are you willing to spend ?",0)
    diamond_essence_1 = diamonds // 10
    diamond_essence_1_pts = diamond_essence_1 * essence_1_pts
    st.write("")
    st.write("Points from Diamond Shop : {:,}, spending {:,} diamonds.".format(diamond_essence_1_pts, diamond_essence_1*10))

    ## TOTAL POINTS ##
    st.write('-')
    total_gem_points = round(
        chests_pts + current_points + trial_tower_points + gems_hero_pts +
        diamond_essence_1_pts)
    st.write("**Total potential points** : {:,}.".format(total_gem_points))


    pass

### WARSIGIL ###
elif event == warsigil :

    st.markdown("## ♚ Warsigil Upgrade")
    st.write('Event on Thursday of Ace Lord week.')
    st.write("-")
    st.write("**How to earn points**")
    st.write("Get 1★ Warsigil Essence - 100 pts")
    st.write("Get 2★ Warsigil Essence - 500 pts")
    st.write("Get 3★ Warsigil Essence - 2,000 pts")
    st.write("Get 4★ Warsigil Essence - 5,000 pts")
    st.write("Get 5★ Warsigil Essence - 20,000 pts")
    st.write("Get 8★ Warsigil Promote Stone - 20,000 pts")

    st.write("Get 3★ Warsigil - 10,000 pts")
    st.write("Get 4★ Warsigil - 100,000 pts")
    st.write("Get 5★ Warsigil - 500,000 pts")
    st.write("Get 6★ Warsigil - 1,000,000 pts")

    st.write("Get Warsigil Spinel - 1,000 pts")

    current_points = st.number_input("How many points do you have so far?", 0)

    essence_1_pts = 100
    essence_chest = st.number_input("How many Essence Choice Chest do you have?", 0)
    essence_chest_pts = essence_chest * essence_1_pts * 100

    st.write("Points from chests : {:,}".format(essence_chest_pts))

    spinel_pts = 1000
    promote_chest = st.number_input("How many Promote Choice Chest do you have?", 0)
    promote_chest_pts = promote_chest * spinel_pts * 10

    st.write("Points from chests : {:,}".format(promote_chest_pts))

    promote_stone_pts = 20000
    promote_8_chest = st.number_input("How many 8★ Choice Chest do you have?", 0)
    promote_8_chest_pts = promote_8_chest * promote_stone_pts * 1

    st.write("Points from chests : {:,}".format(promote_8_chest_pts))
    
    st.write("**Total potential points** : {:,}.".format(round(essence_chest_pts + promote_chest_pts + promote_8_chest_pts + current_points)))    

### TIME CONVERTER ###
elif event == time_calculator :

    st.markdown("## ⏳ Time Converter")
    st.write("Do you have enough speedups for this ?")
    st.write('-')

    st.write("*Already planned something ?*")
    previous = st.number_input("Minutes prior to calcul", 0)
 
    prev_days, prev_mins = day_min_from_total(previous)

    st.write("Being {} day{}, {} hour{}, {} min.".format(
    prev_days, 
    's' if prev_days > 1 else '',
    int(prev_mins // 60), 
    's' if (int(prev_mins//60)) >1 else '',
    prev_mins%60))

    st.write("-")
    is_training = st.checkbox("<-- check this for training version")

    if is_training :
        text = "training"
        soldiers_batch = st.number_input("Training capacity:", 0)
        nb_batch = st.number_input("How many batches do you want to do ?", 1)
    else :
        text = "building / research"
        nb_batch = 1

    st.write('-')

    st.write(f"Time for {text}")
    days = 0 if is_training else st.number_input(f"Days of {text}", 0) 
    hours = st.number_input(f"Hours of {text}", 0)
    minutes = st.number_input(f"Minutes of {text}", 0)
    seconds = st.number_input(f"Seconds of {text}", 0)

    total_minutes = round(total_mins_from_time(days, hours, minutes, seconds)*nb_batch)

    st.write("Total time : {:,} min.".format(total_minutes))
    if is_training:
        st.write("Total of soldiers trained : {:,}.".format(soldiers_batch*nb_batch))

    st.write("Total time including previous : {:,} min.".format(total_minutes+previous))

    pass

### Hell event : build might + speedup ###
elif event == might_speed :

    st.markdown("## 🔎 Might + speedups pts")
    st.write("How many points would it bring to speed-build this ?")
    st.write('-')

    st.write("**Hell event**")
    st.write("- Migh improved by 1 via Research - 2 pts")
    st.write("- 1-min Research Speedup - 15 pts")

    text = "building / research"
    st.write("-")
    st.write(f"Time for {text}")
    days = st.number_input(f"Days of {text}", 0) 
    hours = st.number_input(f"Hours of {text}", 0)
    minutes = st.number_input(f"Minutes of {text}", 0)
    seconds = st.number_input(f"Seconds of {text}", 0)

    total_minutes = round(total_mins_from_time(days, hours, minutes, seconds))
    st.write("Total minutes : {:,}.".format(total_minutes))
    speed_up_pts = total_minutes * 15
    st.write("Points from speeding it up : {:,}.".format(speed_up_pts))

    might_build = st.number_input(f"Might added with this {text}", 0)
    might_pts = might_build * 2
    st.write("Points from {} : {:,}.".format(text, might_pts))

    st.write("**Total points** from this {} (speedups + might pts): {:,}.".format(text, speed_up_pts + might_pts))

    pass

###  RESOURCES CALCULATOR ###
elif event == rss_calc :

    rss_str = {
        "food" : "Food :",
        "wood" : "Wood :",
        "iron" : "Iron :",
        "gold" : "Gold :"
    }

    st.markdown("## 🌰 Resources Calculator")
    st.write("What's the most you could get ?")
    st.write("-")
    
    st.markdown("### Territory Overview")
    st.write("Get in your Territory Overview to find the following numbers")
    
    food_held = st.number_input("Food Held", 0)
    food_bag = st.number_input("Total Food (in Bag)", 0)
    
    st.write('')
    wood_held = st.number_input("Wood Held", 0)
    wood_bag = st.number_input("Total Wood (in Bag)", 0)
    
    st.write('')
    iron_held = st.number_input("Iron Held", 0)
    iron_bag = st.number_input("Total Iron (in Bag)", 0)
    
    st.write('')
    gold_held = st.number_input("Gold Held", 0)
    gold_bag = st.number_input("Total Gold (in Bag)", 0)

    amt_current = {
    "food" : food_held + food_bag,
    "wood" : wood_held + wood_bag,
    "iron" : iron_held + iron_bag,
    "gold" : gold_held + gold_bag,
    }

    st.write("*Total held + bag*")
    st.write("{} {:,}.".format(rss_str["food"], amt_current["food"]))
    st.write("{} {:,}.".format(rss_str["wood"], amt_current["wood"]))
    st.write("{} {:,}.".format(rss_str["iron"], amt_current["iron"]))
    st.write("{} {:,}.".format(rss_str["gold"], amt_current["gold"]))

    st.write("-")
    st.markdown("### Resource Chests")
    st.write("**Lesser Resource Chests**")

    less_rss_amt = {
        'food' : 150000,
        'wood' : 150000,
        'iron' : 30000,
        'gold' : 7500,
    }
    rss, new_current = chest_rss("Lesser Resource Chests", less_rss_amt, rss_str, amt_current)

    st.write("-")
    st.write("**Resource Choice Chests**")

    choice_chest_amt = {
        'food' : 150000*10,
        'wood' : 150000*10,
        'iron' : 50000*6,
        'gold' : 25000*3,
    }
    chest_rss("Resource Choice Chests", choice_chest_amt, rss_str, new_current)

    st.write('-')
    st.markdown("### Rare Earth Fields")
    st.write("Promise I'll do that too... Tell me if you need it :)")





st.write('---')
st.write("Specially made for the Mavdalorian. 🥰")
st.write("*This is the way.*")


