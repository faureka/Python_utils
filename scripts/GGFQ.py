from subprocess import call,Popen
import Tkinter
import ttk


class WebsiteWidget(ttk.Frame):
	"""Google,Gmail,Facebook,Quora"""
	def __init__(self, master = None):
		ttk.Frame.__init__(self,master,width = 500,height = 500)
		self.CreateWidget()
		self.address = ["http://www.google.com","http://www.facebook.com","http://www.quora.com","http://www.gmail.com"]
		self.browser = 'firefox.exe'

	def Google(self):
		call([self.browser,'-new-tab',self.address[0]])
	def Facebook(self):
		call([self.browser,'-new-tab',self.address[1]])
	def Quora(self):
		call([self.browser,'-new-tab',self.address[2]])
	def Gmail(self):
		call([self.browser,'-new-tab',self.address[3]])

	def CreateWidget(self):
		
		self.s = ttk.Style()
		self.s.configure('TButton',foreground='#297ACC',highlightthickness='20',font=('Helvetica', 14, 'bold'))
		# self.s.map('TButton', foreground=[('disabled', 'yellow'),('pressed', 'red'),('active', 'blue')],background=[('disabled', 'magenta'),('pressed', '!focus', 'cyan'),('active', 'green')],highlightcolor=[('focus', 'green'),('!focus', 'red')],relief=[('pressed', 'groove'),('!pressed', 'ridge')]


		self.b1 = ttk.Button(root,text ="Gmail",command=self.Gmail)
		self.b2 = ttk.Button(root,text ="Facebook",command=self.Facebook)
		self.b3 = ttk.Button(root,text ="Google",command=self.Google)
		self.b4 = ttk.Button(root,text ="Quora",command=self.Quora)

		self.b1.pack(padx = 5 ,pady = 5)
		self.b2.pack(padx = 5 ,pady = 5)
		self.b3.pack(padx = 5 ,pady = 5)
		self.b4.pack(padx = 5 ,pady = 5)
		

root = Tkinter.Tk()
root.title("Websites")
root.geometry('200x180')
# root.configure(bg='#334353')
app = WebsiteWidget(master = root)
app.mainloop()