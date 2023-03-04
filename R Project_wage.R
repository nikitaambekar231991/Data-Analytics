#install.packages("ggplot2")
# install.packages("dplyr")
#install.packages("ISLR")

library(ggplot2) #data visualization
library(dplyr) #data manipulation
library(ISLR)

Wage = select(Wage, age, maritl, education, jobclass, wage)
View(Wage)
head(Wage, 3)

str(Wage)

ggplot(data = Wage, aes(x = age, y = wage)) 

ggplot(data = Wage, mapping = aes(x = age, y = wage)) + 
  geom_point()

ggplot(data = Wage, mapping = aes(x = age, y = wage)) +
  geom_density_2d() +
  geom_point()

ggplot(data = Wage, mapping = aes(x = age, y = wage)) +
  geom_bin2d() +
  geom_point()
# Inside the geoms you can fine tune your visualization:

ggplot(data = Wage, mapping = aes(x = age, y = wage)) +
  geom_point(alpha = 0.1, color = "blue", size = 5)+ geom_density_2d(color = "red") 

ggplot(data = Wage, mapping = aes(x = age, y = wage)) +
  geom_point(alpha = 0.5) +
  geom_smooth()

ggplot(data = Wage, mapping = aes(x = age, y = wage, color = maritl)) +
  geom_point()

ggplot(data = Wage, mapping = aes(x = age, y = wage, color = education)) +
  geom_point()+geom_smooth()

ggplot(data = Wage, mapping = aes(x = age, y = wage, color = education)) +
  geom_point()

ggplot(data = Wage, mapping = aes(x = age, y = wage)) +
  geom_point() +
  geom_smooth(aes(color = education)) 

ggplot(data = Wage, mapping = aes(x = age, y = wage)) +
  geom_point() +
  geom_smooth(aes(color = education)) +
  facet_wrap( ~ education)

ggplot(data = Wage, mapping = aes(x = age, y = wage)) +
  geom_point() +
  geom_smooth(aes(color = maritl)) +
  facet_wrap(~ maritl)

ggplot(data = Wage, mapping = aes(x = age, y = wage)) +
  geom_point() +
  geom_smooth(aes(color = jobclass)) +
  facet_wrap(~education)

ggplot(Wage, aes(x = age)) +
  geom_histogram(bins = 10)


