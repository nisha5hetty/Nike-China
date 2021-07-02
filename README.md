# Nike-China
 Project 4

**Finding Data:**

**Nike Manufacturing Map**

Source: http://manufacturingmap.nikeinc.com/

Nike has data of all the contract factories that manufacture finished goods for the brand. I downloaded the map as an excel file and used Pandas to analyze the data.

**Visualizations:**

1. I wanted to create a table of where all the Nike factories are located around the world. Instead of doing a map, I created a searchable table, specifying what was being manufactured in each of the factories by country. I added a heat map. Though Vietnam is the leading manufacturer, China is the leading producer of footwear and equipment for Nike.

3. I wanted to create a bar graph showing the number of migrant workers and locals workers in six Nike factories in China. I used Pandas and created a new column called 'Migrant Workers,' by multiplying '% Migrant Workers' and 'Line Workers' and dividing by 100.

**Summary of my analysis:**

A few years ago, there was talk that Nike was looking beyond China, specifically to Vietnam. While that's true, China remains a key cog in Nike's wheel. I'm not sure how reliable Nike's data is on the number of migrants working in China though. They listed only percent of migrants working, and I had to calculate the actual number. The factories could also not be reporting the numbers accurately. Unless you conduct an investigation and talk to the factory workers, it's hard to rely on data alone for this story.