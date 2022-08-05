# Restaurant Picker

My capstone project, [**Restaurant Picker (V1)**](https://github.com/kellyjadams/RestaurantPicker/blob/main/version1.py) was to create a program to solve a problem. This is a simple program I made for a frequent problem my friends and I encounter. It takes my friends at least 15 minutes to choose any restaurant. To test my Python programming skills, I created a program that randomly chooses a restaurant based on a few criteria.

The user will be able to choose two things:
1. How much you want to spend: cheap, not bad, or expensive (this is all relevant to me and my own budget);
2. The type of cuisine (i.e. American, Mexican, Japanese, etc.) you want based on the list that's avaiable.

With these parameters the program randomly picks a restaurant.

**You can read more about the project in detail [here](https://www.kellyjadams.com/post/restaurant-picker-project).**

## Notes
This program is dead simple. There is no option for the program to ask the user for their own restaurant choice (at least right now though this maybe something I do in the future). Why? Because I made this program for me. To solve a problem I have. I included restaurants I frequent along with what I consider "cheap" or "expensive". I also wanted to complete a project that was challenging yet doable with my current skill level. I may expand this program in the future but this is the first edition. 

There is no option to replay the picker. Because that's the whole dilemma. Once it picks. It's done. That's it. Live with the decision.

## Expansion
I plan on expanding this project in the future. Here are a few features I want to add:
- Let the user input their own choices through a prompt.
- Webscrape restaurant data from Google

## Problems
Below are problems/critiques people have already pointed out to me. I will address these in V2 of the program. 
- Line 99 use print rather than return 
- Use double quotes throughout the entire program
- add `if __name__ == '__main__'do:` in the class
- Resturants are constants so it should be using capitals
- Class object names should be in Pascal case.
