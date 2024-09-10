from .ql_resolver import *

class QueryReq:
	def __init__(self, query: dict[str, dict[str, any]]):
		self.queryType = list(query.keys())[0]
		self.query = list(query[self.queryType].keys())[0]
		self.args = query[self.queryType][self.query]

class QlServer:
	def __init__(self, resolver: Resolver) -> None:
		self.resolver = resolver

	def fetch(self, request: QueryReq, args: dict[str, any] = None) -> dict[str, any]:
		if (request.queryType == "Query" and self.resolver.query is None) or (request.queryType == "Mutation" and self.resolver.mutation is None):
			raise ValueError(f"Invalid query type: {request.queryType}")
		if request.query in list(self.resolver.query.values() if request.queryType == "Query" else self.resolver.mutation.values()):
			if request.queryType == "Query":
				for prop in self.resolver.query.properties:
					if prop.name == request.query and type(prop) == Ql_statement:
						if prop.parameters is not None and args is not None:
							res = []
							for j in (self.resolver[request.queryType][request.query](args)):
								obj = {}
								for i in request.args:
									if j[i] is not None:
										obj[i] = j[i]
								res.append(obj)
							return res
						if prop.parameters is None and args is not None:
							raise ValueError(f"{request.query} does not take any parameters")
						if prop.parameters is not None and args is None:
							raise ValueError(f"{request.query} requires parameters")
						res = []
						for j in (self.resolver[request.queryType][request.query]()):
							obj = {}
							for i in request.args:
								if j[i] is not None:
									obj[i] = j[i]
							res.append(obj)
						return res

			elif request.queryType == "Muation":
				for prop in self.resolver.mutation.properties:
					if prop.name == request.query and type(prop) == Ql_statement:
						if prop.parameters is not None and args is not None:
							res = []
							for j in (self.resolver[request.queryType][request.query](args)):
								obj = {}
								for i in request.args:
									if j[i] is not None:
										obj[i] = j[i]
								res.append(obj)
							return res
						if prop.parameters is None and args is not None:
							raise ValueError(f"{request.query} does not take any parameters")
						if prop.parameters is not None and args is None:
							raise ValueError(f"{request.query} requires parameters")
						res = []
						for j in (self.resolver[request.queryType][request.query]()):
							obj = {}
							for i in request.args:
								if j[i] is not None:
									obj[i] = j[i]
							res.append(obj)
						return res
		else:
			raise ValueError(f"Invalid query: {request.query}")
