class ManageAttendance(tk.Frame):
	def __init__(self,parent,controller):
		tk.Fra
		bt3.pack()
		bt1.pack()
	def showstatus(self,controller):
		try:
			conn=sql.connect("Attend")
			cur=conn.cursor()
			cur.execute('SELECT * FROM attable')
			text=""
			for w in cur:
				if w[2]==0 and w[3]==0:
					per="0"
				else:
					per=w[2]/(w[2]+w[3])
					per=per*100
					per=str(int(per))
				text=text+"sub id "+str(w[0])+" "+w[1]+" "+per+"%\n"
			messagebox.showinfo("status", text)
		except:
			messagebox.showinfo("Alert!", "No Records Found")	
