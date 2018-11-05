import uuid

class Parcel(object):
	parcels = []
	def create_order(self,destination,recipient,sender,weight):
		self.destination = destination
		self.recipient = recipient
		self.sender = sender
		self.weight = weight

		payload  ={
		"id": uuid.uuid4().int,
		"destination":self.destination,
		"recipient":self.recipient,
		"sender":self.sender,
		"weight":self.weight
		}

		Parcel.parcels.append(payload)

	def get_all(self):
		return Parcel.parcels

	def get_one_parcel(self,id):
		for item in Parcel.parcels:
			if item['id'] ==id:
				return item



