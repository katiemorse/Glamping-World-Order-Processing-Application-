
class page4(tk.Frame):

def __init__(self,
parent, controller):

tk.Frame.__init__(self, parent)



left_frame2 = tk.Frame(self, 
width=200, 
height=350, 
bg="grey")

left_frame2.pack_propagate(0)



right_frame2 = tk.Frame(self, 
width=400, 
height=350, 
bg="lightgrey")

right_frame2.pack_propagate(0)



photo = PhotoImage(file="P:\GWlogo.gif")
# specify the path to your file

label = Label(self, 
image=photo) #put the image in a label to disdaply it in the window

label.image = photo

label.pack(side=tk.TOP)




page_name_label2 = tk.Label(self, 
text="Payment Info", 
fg="black", 
bg="white", 
font=(None, 
15))

page_name_label2.pack(side=tk.TOP, 
expand=1, 
fill=tk.X)


tab12 = tk.Label(left_frame2, text="Login Page",
bg="grey")

tab22 = tk.Label(left_frame2, text="Customer Info Page",
bg="grey")

tab42 = tk.Label(left_frame2, text="Products Page",
bg="grey")

tab52 = tk.Label(left_frame2, text="Payment Info",
bg="grey")

tab62 = tk.Label(left_frame2, text="Order Confirmation",
bg="grey")

backButton = tk.Button(left_frame2, text="Previous Page",
command=lambda: controller.show_frame(page3))

nextButton = tk.Button(left_frame2, text="Next Page",
command=lambda: controller.show_frame(page6))

helpButton = tk.Button(left_frame2, text="HELP")




tab12.pack(side=tk.TOP)

tab22.pack(side=tk.TOP)

tab42.pack(side=tk.TOP)

tab52.pack(side=tk.TOP)

tab62.pack(side=tk.TOP)

helpButton.pack(side=tk.BOTTOM)

nextButton.pack(side=tk.BOTTOM)

backButton.pack(side=tk.BOTTOM)




left_frame2.pack(side=tk.LEFT, 
fill=tk.BOTH)
