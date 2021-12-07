"""
Contains the methods to be used in the main app
"""

# What I love
"""
Summary: 
Given a source list (skillshare), show my interests using a bubble chart or so, showing its evolution over time

Inputs: 
Source list (item type: string), 
Dataframe (Columns - interest items (string), strength of interest (float: define the scale with examples), Year)

Outputs: 
The key takeaways printed in a template string, and the plotly bubble chart object is returned
"""

# What I'm good at
"""
Summary: 
Given a source list (skillshare/kaggle), show my projects, what I did and what I achieved

Inputs: 
Source list: Skillshare/LinkedIn/Kaggle
Dataframe (Columns: Project value proposition, What I did, What I achieved - quantifiable, Organization, Year)

Outputs: 
Plots, pictures, network graph showing my conceptual connections and trajectory
"""

# What I can be paid for
"""
Summary: 
Given a report/public dataset (skillshare), showcase the pay range distributions, and pay range I'm okay with

Inputs: 
Database containing pay scale distributions for the skills I possess and what's the pay rate (hourly)
How much time do you take for these projects/tasks (Dataframe)

Outputs: 
Pay range plots, marking my acceptable range for the skills/projects selected and expected time taken
"""

# What the world needs
"""
Summary: 
Show your curation - resources, people, websites. Research from 80,000 hours, EA community, World Economic Forum etc.

Inputs: 
Dataframe containing curation, category, time to read, audience, what they'll do differently after reading this

Outputs:
Interactive charts based on the info in the dataframe
"""