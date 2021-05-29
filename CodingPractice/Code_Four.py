def area_of_country(name, area):
    area1=area/1
    area2=round((area1/148940000)*100,2)
    print("{} is {}% of the total world's landmass".format(name,area2))



area_of_country("Russia",17098242)