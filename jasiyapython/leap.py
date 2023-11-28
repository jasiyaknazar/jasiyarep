import dataeime
current_year=dataeime.date.today().year
#Get the final year from the user
final_year=int(input("enter the final year:"))
if final_year<current_year:
    print("Final year must be greater than or equal to the current yeaar")
else:
    print(f"Leap years from (current_year)to(final_year)
          for year in range(current_year,final_year+1):
          if(year%4==0andyear%100!=0)or(year%400==0):
            print(year)
