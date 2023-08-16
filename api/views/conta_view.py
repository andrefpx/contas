from flask_restful import Resource
from ..schemas import conta_schema
from flask import request,make_response,jsonify
from ..entidades import conta
from ..services import conta_service
from api import api
class ContaList(Resource):
    def post(self):
        cs = conta_schema.ContaSchema()
        validate = cs.validate(request.json) # valida o schema , caso não esteja de acordo a requisição não irá passar.
        if validate:
            return make_response(jsonify(validate),400)
        else:
            nome = request.json["nome"]
            resumo = request.json["resumo"]
            valor = request.json["valor"]
            conta_nova = conta.Conta(nome=nome,resumo=resumo,valor=valor)
            resultado = conta_service.cadastrar_conta(conta_nova)
            return make_response(jsonify(cs.resultado),201)
api.add_resource(ContaList,'/contas')

