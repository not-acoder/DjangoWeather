from django.shortcuts import render

def home(request):
	import json
	import requests

	if request.method == "POST":
		zipcode = request.POST['zipcode']
		api_requests=requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" +zipcode+"&distance=25&API_KEY=FA15703C-A597-4B82-9598-1FB275AEF5F5")
		try:
			api=json.loads(api_requests.content)
		except Exception as e:
			api="Error..."

		

		if api[0]['Category']['Name'] == "Good":
			category_description =	"Description : 0 to 50 Air quality is considered satisfactory, and air pollution poses little or no risk."  
			category_color = "good"


		elif api[0]['Category']['Name'] == "Moderate":
			category_description = "Description : 51 to 100	Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."
			category_color = "moderate"
			  
		elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
	 		category_description = " Description :101 to 150 Members of sensitive groups may experience health effects. The general public is not likely to be affected."
	 		category_color = "Unhealthyforsensitivegroups"
		 	
		elif api[0]['Category']['Name'] == "Unhealthy":	
			category_description = "Description : 151 to 200 Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
			category_color = "Unhealthy" 

		elif api[0]['Category']['Name'] == "Very Unhealthy":
			category_description = "Description : 201 to 300 Health alert: everyone may experience more serious health effects."
			category_color = "veryunhealthy"

		elif api[0]['Category']['Name'] == "Hazardous":
			category_description = "Description :301 to 500 Health warnings of emergency conditions. The entire population is more likely to be affected."
			category_color = "hazardous"
	 	  
	 	

		return render(request, 'home.html',{'api': api, 'category_description' : category_description , 'category_color' : category_color})		

	else:
		api_requests=requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=FA15703C-A597-4B82-9598-1FB275AEF5F5")
		try:
			api=json.loads(api_requests.content)
		except Exception as e:
			api="Error..."

		

		if api[0]['Category']['Name'] == "Good":
			category_description =	"Description : 0 to 50 Air quality is considered satisfactory, and air pollution poses little or no risk."  
			category_color = "good"

		elif api[0]['Category']['Name'] == "Moderate":
			category_description = "Description : 51 to 100	Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution."
			category_color = "moderate"
			  
		elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
	 		category_description = " Description :101 to 150 Members of sensitive groups may experience health effects. The general public is not likely to be affected."
	 		category_color = "Unhealthyforsensitivegroups"
		 	
		elif api[0]['Category']['Name'] == "Unhealthy":	
			category_description = "Description : 151 to 200 Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
			category_color = "Unhealthy" 

		elif api[0]['Category']['Name'] == "Very Unhealthy":
			category_description = "Description : 201 to 300 Health alert: everyone may experience more serious health effects."
			category_color = "veryunhealthy"

		elif api[0]['Category']['Name'] == "Hazardous":
			category_description = "Description :301 to 500 Health warnings of emergency conditions. The entire population is more likely to be affected."
			category_color = "hazardous"
	 	  
	 	

		return render(request, 'home.html',{'api': api, 'category_description' : category_description , 'category_color' : category_color})

def about(request):
	return render(request, 'about.html',{})






# Create your views here.
