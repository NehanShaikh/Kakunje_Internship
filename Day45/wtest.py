import tkinter as tk 
import joblib 
 
try: 
    model=joblib.load("weather_model.pkl") 
except: 
    print("Please run train.py first") 
    exit() 
 
def predict(): 
        values=[ 
            float(prec.get()), 
            float(max_temp.get()), 
            float(min_temp.get()), 
            float(wind.get())   ] 
 
        prediction=model.predict([values])[0] 
        result.configure(text=f"Prediction: {prediction}") 
 
root=tk.Tk() 
root.title("Weather Prediction App") 
root.geometry("350x400") 
tk.Label(root, text="Enter Weather Features", font=("Arial", 14, "bold italic")).pack(pady=5) 
 
tk.Label(root,text="Precipitation").pack() 
prec=tk.Entry(root) 
prec.pack() 
 
tk.Label(root, text="Max Temp").pack() 
max_temp=tk.Entry(root) 
max_temp.pack() 
 
tk.Label(root, text="Min Temp").pack() 
min_temp=tk.Entry(root) 
min_temp.pack() 
 
tk.Label(root, text="Wind").pack() 
wind=tk.Entry(root) 
wind.pack() 
 
tk.Button(root,text="Predict",command=predict).pack(pady=10) 
 
result=tk.Label(root,text="",font=("Arial",12)) 
result.pack() 
 
root.mainloop()
