from flask import request, make_response,jsonify
from flask_restful import Resource, Api
from SendIT_App.api.Version1.models.parcel import Parcel
from SendIT_App.api.Version1 import bp


parcels_bp = Api(bp)

class AllParcels(Resource):
	def get(self):
		par1 = Parcel()
		all_p = par1.get_all()

		payload = {
			"Status":"Ok",
			"Parcels": all_p
		}
		answ= make_response(jsonify(payload),200)
		answ.content_type = 'application/json;charset=utf-8'
		return answ



	def post(self):
		data = request.get_json() or {}

		par1 = Parcel()
		all_p = par1.create_order(
			data["destination"] = destination,
			data["recipient"] = recipient,
			data["sender"] = sender,
			data["weight"] = weight
			)

		payload = {
			"Status":"created",
			
		}
		answ= make_response(jsonify(payload),204)
		answ.content_type = 'application/json;charset=utf-8'
		return answ


	parcels_bp.add_resource(AllParcels,"/parcels")
