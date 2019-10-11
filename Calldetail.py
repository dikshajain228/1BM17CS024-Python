class CallDetail:
	def __init__(self, caller, callee, duration, typeOfCall):
		self.caller = caller
		self.callee = callee
		self.duration = duration
		self.typeOfCall = typeOfCall
	def getter(self):
		print(self.caller, self.callee, self.duration, self.typeOfCall)
	
class Util:
	def __init__(self):
		self.list_of_call_objects = None
	def parse_customer(self,list_of_call_string):
		self.list_of_call_objects = []
		for i in list_of_call_string:
			caller, callee, duration, typeOfCall=map(str, i.split(","))
			self.list_of_call_objects.append(CallDetail(caller, callee, duration, typeOfCall))
	def getter(self):
		for i in self.list_of_call_objects:
			i.getter()
call = '999,989,23,STD'
call2 = '889,889,24,Local'
call3 = '777,779,2,ISD'
u = Util()
list_of_call_string = [call,call2,call3]
u.parse_customer(list_of_call_string)
u.getter()
