from collections.abc import Iterable
from typing import Union
from .ql_types import *

class Ql_statement(QlProperty):
	def __init__(self, name: str, type: object | QlType, isNullable: bool = True, additional: Union['QlProperty', str, int, float, bool] = None, parameters: list['QlProperty']= None):
		super().__init__(name, type, isNullable, additional)
		self.parameters = parameters

	def __str__(self):
		param = f"({join(self.parameters, ', ')})" if self.parameters is not None else ""
		add = f"[{self.additional.name if self.additional.type == QlProperty else _ql_str(self.additional.type)}{'!' if not self.additional.isNullable else ''}]" if self.additional is not None else ""
		return f"{self.name}{param}: {add if self.type == list else _ql_str(self.type)}{"!" if not self.isNullable else ''}"

	def dict(self):
		return {
			"name": self.name,
			"type": self.type.dict() if type(self.type) == QlType else _ql_str(self.type),
			"parameters": [p.dict() for p in self.parameters] if self.parameters is not None else "null"
		}

class QlQuery(QlType):
	def __init__(self, name: str, properties: list[Ql_statement]):
		if (name == "Query" or name == "Mutation"):
			super().__init__(name, properties)
		else:
			raise Exception("Name: must be Query or Mutation")

	def __str__(self):
		return f"{self.name}{' {\n\t'}{_join(self.properties, "\n\t") + '\n}'}"
	def dict(self):
		return {
			"name": self.name,
			"properties": [p.dict() for p in self.properties]
		}

def _join(properties: list[Ql_statement], s: str):
	out= ""
	for p in range(len(properties)-1):
		param = f"({join(properties[p].parameters, ', ')})" if properties[p].parameters is not None else ""
		out+= properties[p].name+ param + ": " + _ql_str(properties[p].type) + s
	param = f"({join(properties[-1].parameters, ', ')})" if properties[-1].parameters is not None else ""
	out += properties[-1].name+ param + ": " + _ql_str(properties[-1].type)
	return out

def _ql_str(s: Union[object, Ql_statement])-> str:
	if s is None:
		return "None"
	else:
		if s == str:
			return "String"
		elif s == list:
			return "Array"
		elif s == int:
			return "Int"
		elif s == float:
			return "Float"
		elif s == bool:
			return "Boolean"
		else:
			return s.name if type(s)== QlType else "Unknown"
