from flask import Flask, render_template, request

app= Flask(__name__)

rateUpto50=4.21
rate51to150=5.17
rate151to300=6.55
rateAbove300=6.74
FCArate=0.34
Dutyrate=0.09
chargeupto50=0
chargeupto150=0
chargeupto300=0
chargeabove300=0
fcaCharge=0
DutyCharge=0
#fcaonDuty= unit * dutycharge * 0.34
@app.route("/",methods=["GET","POST"])
def Home():
    if request.method == "GET":
        return render_template("home.html")
    else:
        unit=int(request.form.get("unit"))
        load=int(request.form.get("load"))
        duration=int(request.form.get("duration"))
        days=int(request.form.get("days"))
        if(unit<=50):
            chargeupto50=unit * rateUpto50
            fcaCharge = unit * FCArate
            DutyCharge= (chargeupto50 * Dutyrate) + (unit * Dutyrate * FCArate)
            Urbanfixedcharge=121
            RuralfixedCharge=98
            Urbansubsidy =days * (250 / duration)
            Ruralsubsidy= days * (200 / duration)

            Urbantotalcharge=chargeupto50 +fcaCharge+DutyCharge+Urbanfixedcharge - Urbansubsidy
            Ruraltotalcharge=chargeupto50 +fcaCharge+DutyCharge+RuralfixedCharge - Ruralsubsidy 

            data=[unit,load,duration,days,chargeupto50,fcaCharge,DutyCharge,Urbanfixedcharge,RuralfixedCharge,Urbansubsidy,Ruralsubsidy,Urbantotalcharge,Ruraltotalcharge]
            return render_template("home.html",data=data)

        elif(unit >50 and unit<=150):
            chargeupto50=50 * rateUpto50
            chargeupto150=(unit-50) * rate51to150
            fcaCharge = unit * FCArate
            DutyCharge= (chargeupto50 * Dutyrate) + (unit * Dutyrate * FCArate)
            Urbanfixedcharge=121
            RuralfixedCharge=98
            Urbansubsidy =days * (550 / duration)
            Ruralsubsidy= days * (500 / duration)
            Urbantotalcharge=chargeupto50+chargeupto150 +fcaCharge+DutyCharge+Urbanfixedcharge
            Ruraltotalcharge=chargeupto50+chargeupto150 +fcaCharge+DutyCharge+RuralfixedCharge - Ruralsubsidy 

            data=[unit,load,duration,days,chargeupto50+chargeupto150,fcaCharge,DutyCharge,Urbanfixedcharge,RuralfixedCharge,Urbansubsidy,Ruralsubsidy,Urbantotalcharge,Ruraltotalcharge] 

            return render_template("home.html",data=data)
        elif (unit >150 and unit <=300):
            chargeupto50=50 * rateUpto50
            chargeupto150=100 * rate51to150
            chargeupto300=(unit-150) * rate151to300
            fcaCharge = unit * FCArate
            DutyCharge= (chargeupto50 * Dutyrate) + (unit * Dutyrate * FCArate)
            Urbanfixedcharge=121
            RuralfixedCharge=98
            

            Urbantotalcharge=chargeupto50+chargeupto150+chargeupto300 +fcaCharge+DutyCharge+Urbanfixedcharge - 0
            Ruraltotalcharge=chargeupto50+chargeupto150+chargeupto300 +fcaCharge+DutyCharge+RuralfixedCharge - 0 
 
            data=[unit,load,duration,days,chargeupto50+chargeupto150+chargeupto300,fcaCharge,DutyCharge,Urbanfixedcharge,RuralfixedCharge,0,0,Urbantotalcharge,Ruraltotalcharge]
            return render_template("home.html",data=data)
        else:
            chargeupto50=50 * rateUpto50
            chargeupto150=100 * rate51to150
            chargeupto300=150 * rate151to300
            chargeabove300=(unit-300) * rateAbove300
            fcaCharge = unit * FCArate
            DutyCharge= (chargeupto50 * Dutyrate) + (unit * Dutyrate * FCArate)
            Urbanfixedcharge=121
            RuralfixedCharge=98
            

            Urbantotalcharge=chargeupto50+chargeupto150+chargeupto300+chargeabove300 +fcaCharge+DutyCharge+Urbanfixedcharge -0
            Ruraltotalcharge=chargeupto50+chargeupto150+chargeupto150+chargeabove300 +fcaCharge+DutyCharge+RuralfixedCharge - 0 
 
            data=[unit,load,duration,days,chargeupto50+chargeupto150+chargeupto300+chargeabove300,fcaCharge,DutyCharge,Urbanfixedcharge,RuralfixedCharge,0,0,Urbantotalcharge,Ruraltotalcharge]
            return render_template("home.html",data=data)








if __name__ == "__main__":
    app.run(debug=True)