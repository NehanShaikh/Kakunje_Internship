import tkinter as tk 
import joblib 
 
try: 
    model=joblib.load("car_model.pkl") 
    encoders=joblib.load("encoders.pkl") 
except: 
    print("Run train.py first") 
 
def predict(): 
    brand=encoders["Brand"].transform([b.get()])[0] 
    model_name=encoders["Model"].transform([ml.get()])[0] 
    year=int(yr.get()) 
    engine=float(eng.get()) 
    fuel=encoders["Fuel_Type"].transform([ft.get()])[0] 
    transmission=encoders["Transmission"].transform([tn.get()])[0] 
    mileage=int(mg.get()) 
    doors=int(dr.get()) 
    owner=int(own.get()) 
 
    data=[[brand,model_name,year,engine,fuel,transmission,mileage,doors,owner]] 
 
    prediction=model.predict(data)[0] 
 
    result.configure(text=f"Prediction:{round(prediction,2)}") 
 
 
root=tk.Tk() 
root.title("Car Price Prediction") 
root.geometry("400x500") 
 
tk.Label(root,text="Enter Car Details",font=("Arial",14,"bold italic")).pack(pady=5) 
 
tk.Label(root,text="Brand").pack() 
b=tk.Entry(root) 
b.pack() 
 
tk.Label(root,text="Model").pack() 
ml=tk.Entry(root) 
ml.pack() 
 
tk.Label(root,text="Year").pack() 
yr=tk.Entry(root) 
yr.pack() 
 
tk.Label(root,text="Engine Size").pack() 
eng=tk.Entry(root) 
eng.pack() 
 
tk.Label(root,text="Fuel Type").pack() 
ft=tk.Entry(root) 
ft.pack() 
 
tk.Label(root,text="Transmission").pack() 
tn=tk.Entry(root) 
tn.pack() 
 
tk.Label(root,text="Mileage").pack() 
mg=tk.Entry(root) 
mg.pack() 
 
tk.Label(root,text="Doors").pack() 
dr=tk.Entry(root) 
dr.pack() 
 
tk.Label(root,text="Owner Count").pack() 
own=tk.Entry(root) 
own.pack() 
 
tk.Button(root,text="Predict",command=predict).pack(pady=10) 
 
result=tk.Label(root,text="",font=("Arial",12)) 
result.pack() 
 
root.mainloop()
