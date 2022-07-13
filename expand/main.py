from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)
@app.route('/index1',methods=['GET','POST'])
def home():
    print("welcome, your server is running")
    if request.method=='POST':
        # Handle POST Request here
     
        payload = {            
         "uid":request.form.get("uid"),
         "uidType":request.form.get("uidType"),
          "bussinessName":request.form.get("bussinessName"),
          "title":request.form.get("title"),
          "dirBvn": request.form.get("dirBvn"),
          "dirFirstName":  request.form.get("dirFirstName"),
         "dirLastName":request.form.get("dirLastName"),
         "userName":request.form.get("userName"),
       "Phone":request.form.get("Phone"),
       "emailId":request.form.get("emailId"),
       "postalCode": request.form.get("postalCode"),
         "city": request.form.get("city"),
           "state":request.form.get("state"),
           "lga":request.form.get("lga"),
           "address":request.form.get("address"),
          "countryOfResidence": request.form.get("countryOfResidence"),
          "customerRiskRating":request.form.get("customerRiskRating"),
           "tier":request.form.get("tier"),
          "accountNumber": request.form.get("accountNumber"),
          "dirDateOfBirth":request.form.get("dirDateOfBirth"),
          "countryOfBirth":request.form.get("countryOfBirth"),
          "stateOfOrigin":request.form.get("stateOfOrigin"),
            "password":request.form.get("password"),
            "remarks":request.form.get("remarks"),
          "instCode": request.form.get("instCode"),
            "referralCode": request.form.get("referralCode"),
           "channel":request.form.get("channel")}
            
        print(payload)
  
        return render_template('index1.html',payload=payload)
    return render_template('index1.html')
        

if __name__=='__main__':
    app.run(port=5000,debug=True)