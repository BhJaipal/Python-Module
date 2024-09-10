from typing import Union

def ql_str(s: object)-> str:
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
			return s.name if type(s)== QlProperty else "Unknown"

class QlProperty:
	def __init__(self, name: str, type: object, isNullable: bool = True, additional: Union['QlProperty', str, int, float, bool] = None):
		self.name = name
		self.type = type
		if type == list and additional is None:
			raise Exception("List must have a type")
		self.additional = additional
		self.isNullable = isNullable

	def dict(self):
		return {"name": self.name, "type": ql_str(self.type), "additional": self.additional.dict() if self.additional is not None else "null"}

	def __str__(self):
		add = f"[{self.additional.name if self.additional.type == QlProperty else ql_str(self.additional.type)}{'!' if not self.additional.isNullable else ''}]" if self.additional is not None else ""
		return f"{self.name}: {add if self.type == list else ql_str(self.type)}{"!" if not self.isNullable else ''}"

def join(properties: list[QlProperty], s: str):
	out= ""
	for p in range(len(properties)-1):
		out+= properties[p].__str__() + s
	out += properties[-1].__str__()
	return out

class QlType:
	def __init__(self, name: str, properties: list[QlProperty]):
		self.name = name
		self.properties = properties
	def __str__(self):
		return f"{self.name}{' {\n\t'}{join(self.properties, "\n\t") + '\n}'}"

	def values(self):
		return [p.name for p in self.properties]

	def __getitem__(self, index: int):
		return self.data[index]

	def dict(self):
		return {"name": self.name, "properties": [p.dict() for p in self.properties]}
